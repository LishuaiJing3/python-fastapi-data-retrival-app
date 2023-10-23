from typing import List

import pandas as pd
import pyodbc
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

# import the normalize_date_format function from backend_helper.py
from python_fastapi_data_retrival_app.utils.backend_helper import normalize_date_format

app = FastAPI()


class Filter(BaseModel):
    start_date: str
    end_date: str
    columns: List[str]


@app.post("/data/")
async def get_data(filter: Filter):
    # Define your databricks SQL connection here
    table_name = "active_fw_table"
    date_column = "RUN_DATE"
    # convert input to datetime
    start_date = normalize_date_format(filter.start_date)
    end_date = normalize_date_format(filter.end_date)
    # Data Source Name (DSN) that you created when setting up odbc databricks connector.
    conn = pyodbc.connect("DSN=Databricks_Cluster", autocommit=True)
    # Define your SQL query here
    sql_query = f"""  
    SELECT {', '.join(filter.columns)}  
    FROM {table_name}  
    WHERE {date_column} BETWEEN '{start_date}' AND '{end_date}'  
    """
    print(sql_query)
    try:
        data = pd.read_sql(sql_query, conn)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Here you can do your data processing
    # data = your_data_processing_function(data)

    # Save dataframe to csv
    data.to_csv("data/data.csv", index=False)

    # Convert the DataFrame to a dictionary and return API call
    return data.to_dict("records")


@app.get("/download/")
async def download_csv():
    return FileResponse("data/data.csv", filename="data/data.csv")
