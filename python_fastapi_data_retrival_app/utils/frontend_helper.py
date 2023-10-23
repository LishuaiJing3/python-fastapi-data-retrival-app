import os

import dotenv
import requests

dotenv.load_dotenv()


def get_data(n_clicks, start_date, end_date):
    if n_clicks > 0:
        cols_to_retrieve = os.getenv("COLUMNS").split(",")
        response = requests.post(
            "http://localhost:8000/data",
            json={"start_date": start_date, "end_date": end_date, "columns": cols_to_retrieve},
        )
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            print(df.head(2))
            columns = [{"name": i, "id": i} for i in df.columns]
            return "Data retrived from server successfully.", df.to_dict("records"), columns
        else:
            return "Error downloading data.", [], []
