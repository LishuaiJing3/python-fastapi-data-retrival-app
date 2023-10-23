import os

import gradio as gr
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()


def retrieve_data(start_date: str, end_date: str):
    cols_to_retrieve = os.getenv("COLUMNS").split(",")
    response = requests.post(
        "http://localhost:8000/data", json={"start_date": start_date, "end_date": end_date, "columns": cols_to_retrieve}
    )
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df, "Data retrieved from the server successfully."
    else:
        return pd.DataFrame(), "Error downloading data."


iface = gr.Interface(
    fn=retrieve_data,
    inputs=[
        gr.Textbox(lines=1, placeholder="Start date", label="Start date", default="2023-10-01"),
        gr.Textbox(lines=1, placeholder="End date", label="End date", default="2023-10-02"),
    ],
    outputs=[gr.DataFrame(), "text"],
)


if __name__ == "__main__":
    iface.launch()
