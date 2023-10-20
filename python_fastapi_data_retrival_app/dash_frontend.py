import dash  
from dash import dcc  
from dash import html  
from dash.dependencies import Output, Input  
import requests  
from datetime import datetime as dt
  
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']  
  
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)  
  
app.layout = html.Div([  
    dcc.DatePickerRange(  
        id='my-date-picker-range',  
        min_date_allowed=dt(2023, 1, 1),  
        max_date_allowed=dt(2023, 10, 19),  
        initial_visible_month=dt(2023, 10, 1),  
        end_date=dt(2023, 10, 10)  
    ),  
    html.Button('Submit', id='submit-button', n_clicks=0),  
    html.Div(id='output-container-date-picker-range')  
])  
  
@app.callback(  
    Output('output-container-date-picker-range', 'children'),  
    [Input('submit-button', 'n_clicks')],  
    [dash.dependencies.State('my-date-picker-range', 'start_date'),  
     dash.dependencies.State('my-date-picker-range', 'end_date')]  
)  
def get_data(n_clicks, start_date, end_date):  
    if n_clicks > 0:  
        response = requests.post('http://localhost:8000/data', json={"start_date": start_date, "end_date": end_date, "columns": ["HOME_ID", "DEV_ID"]})  
        if response.status_code == 200:  
            return 'Data downloaded successfully.'  
        else:  
            return 'Error downloading data.'  
  
if __name__ == '__main__':  
    app.run_server(debug=True)  




