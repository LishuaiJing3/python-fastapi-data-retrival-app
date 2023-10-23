
#%%
import os
import dotenv

import requests
import pandas as pd
import numpy as np

import streamlit as st


dotenv.load_dotenv()

#%%
st.title('Single user data retrival app')


#poetry run streamlit run python_fastapi_data_retrival_app/st_frontend.py
#%%
@st.cache_data
def get_data(start_date, end_date,cols_to_retrieve):
    start_date = str(start_date)
    end_date = str(end_date)
    
    response = requests.post('http://localhost:8000/data',    
                                json={"start_date": start_date, "end_date": end_date,    
                                    "columns": cols_to_retrieve})    
    if response.status_code == 200:    
        data = response.json()  
        df = pd.DataFrame(data)    
        print(df.head(2))
        columns = [{"name": i, "id": i} for i in df.columns]    
        return 'Data retrived from server successfully.', df.to_dict('records'), columns    
    else:    
        return 'Error downloading data.', [], []

# Create a session state object
if 'retrived_data' not in st.session_state:
    st.session_state.retrived_data = None

start_date = st.sidebar.date_input("Start date", value=pd.to_datetime('2023-10-01'))
end_date = st.sidebar.date_input("End date", value=pd.to_datetime('2023-10-02'))
cols_to_retrieve = os.getenv("COLUMNS").split(',')

# show a table with the data
st.write('## Data retrival')
if st.button('Submit'):
    message, data, columns = get_data(start_date, end_date, cols_to_retrieve)
    st.session_state.retrived_data = pd.DataFrame(data)
    st.write(pd.DataFrame(data))
    st.write(message)

# Button to download the retrieved data
if st.button("Download Data"):
    if st.session_state.retrived_data is not None:
        # Save the DataFrame to a CSV file in the 'downloads' folder
        st.session_state.retrived_data.to_csv('data/retrieved_data.csv', index=False)
        st.success("Data downloaded successfully to 'data/retrieved_data.csv'.")
    else:
        st.warning("No data to download. Please retrieve data first.")