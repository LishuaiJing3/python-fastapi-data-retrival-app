import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import pandas as pd
import requests
from datetime import datetime as dt

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [html.H2("Download data example", style={"text-align": "center"})]
                )
            ]
        ),
        dcc.DatePickerRange(
            id='my-date-picker-range',
            min_date_allowed=dt(2023, 1, 1),
            max_date_allowed=dt(2023, 10, 19),
            initial_visible_month=dt(2023, 10, 1),
            start_date=dt(2023, 10, 1),
            end_date=dt(2023, 10, 2)
        ),
        html.Button('Submit', id='submit-button', n_clicks=0),
        html.Div(id='output-container-date-picker-range'),
        dcc.Download(id="download"),
        dash_table.DataTable(
            id='table',
            page_size=10,
            style_table={"overflowX": "auto"},
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Dropdown(
                            options=[
                                {"label": "Excel file", "value": "excel"},
                                {"label": "CSV file", "value": "csv"},
                            ],
                            id="dropdown",
                            placeholder="Choose download file type. Default is CSV format!",
                        )
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Button(
                            "Download Data", id="btn_csv"
                        ),
                    ]
                ),
            ]
        ),
    ]
)

@app.callback(  
    [Output('output-container-date-picker-range', 'children'),    
     Output('table', 'data'),    
     Output('table', 'columns')],    
    Input('submit-button', 'n_clicks'),    
    [State('my-date-picker-range', 'start_date'),    
     State('my-date-picker-range', 'end_date')]  
)    
def get_data(n_clicks, start_date, end_date):  
    if n_clicks > 0:    
        response = requests.post('http://localhost:8000/data',    
                                 json={"start_date": start_date, "end_date": end_date,    
                                       "columns": ["HOME_ID", "DEV_ID"]})    
        if response.status_code == 200:    
            data = response.json()  
            df = pd.DataFrame(data)    
            print(df.head(2))
            columns = [{"name": i, "id": i} for i in df.columns]    
            return 'Data retrived from server successfully.', df.to_dict('records'), columns    
        else:    
            return 'Error downloading data.', [], []    
    #return '', [], []  # Empty string and empty lists as default return values  


@app.callback(
    Output("download", "data"),
    Input("btn_csv", "n_clicks"),
    State("dropdown", "value"),
    State('my-date-picker-range', 'start_date'),
    State('my-date-picker-range', 'end_date'),
    prevent_initial_call=True,
)
def func(n_clicks_btn, download_type, start_date, end_date):
    if n_clicks_btn:
        response = requests.post('http://localhost:8000/data',
                                 json={"start_date": start_date, "end_date": end_date,
                                       "columns": ["HOME_ID", "DEV_ID"]})
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            print('download data now')
            print(df.head(2))
            if download_type == "csv":
                return dcc.send_data_frame(df.to_csv, "mydf.csv")
            else:
                return dcc.send_data_frame(df.to_excel, "mydf.xlsx")
    return None

if __name__ == "__main__":
    app.run_server(debug=True)

