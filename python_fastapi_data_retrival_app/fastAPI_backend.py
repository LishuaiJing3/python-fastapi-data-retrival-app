from fastapi import FastAPI, HTTPException  
from pydantic import BaseModel  
from typing import Optional, List  
import pandas as pd  
import pyodbc  
from datetime import datetime  
from datetime import datetime as dt
from fastapi.responses import FileResponse  
  
app = FastAPI()  
  
  
class Filter(BaseModel):  
    start_date: str  
    end_date: str  
    columns: List[str]  
  
@app.post("/data/")  
async def get_data(filter: Filter):  
    # Define your databricks SQL connection here  
    # Replace <table-name> with the name of the database table to query.
    table_name = "active_fw_table"
    date_column = "RUN_DATE"
    # convert input to datetime
    print(filter.start_date)
    print(filter.end_date)
    #date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    date_format = "%Y-%m-%d"
    start_date = dt.strptime(filter.start_date, date_format)
    end_date = dt.strptime(filter.end_date, date_format)
    # Connect to the SQL warehouse by using the
    # Data Source Name (DSN) that you created when setting up odbc databricks connector.
    conn = pyodbc.connect("DSN=Databricks_Cluster", autocommit=True)
    # Define your SQL query here  
    sql_query = f"""  
    SELECT {', '.join(filter.columns)}  
    FROM {table_name}  
    WHERE {date_column} BETWEEN '{start_date}' AND '{end_date}'  
    """  
  
    try:  
        data = pd.read_sql(sql_query, conn)  
    except Exception as e:  
        raise HTTPException(status_code=400, detail=str(e))  
  
    # Here you can do your data processing  
    # data = your_data_processing_function(data)  
  
    # Save dataframe to csv  
    data.to_csv('data/data.csv', index=False)  
  
    return {"message": "Data processed and saved to data.csv"}  
  
@app.get("/download/")  
async def download_csv():  
    return FileResponse('data/data.csv', filename='data/data.csv')  


'''
start_date =  "2023-10-01T08:00:07.859Z"
start_date = dt.strptime(start_date, '%Y-%m-%d')
'''