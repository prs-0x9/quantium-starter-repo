import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# The path to the formatted sales data
DATA_PATH = "./formatted_sales.csv"

# Load the data and sort it by date
data = pd.read_csv(DATA_PATH)
data['date'] = pd.to_datetime(data['date'])
data = data.sort_values(by="date")

# Initialize the Dash app
app = Dash(__name__)

# Generate the line chart using Plotly Express
def create_sales_chart(data):
    return px.line(data, x='date', y='sales', title='Pink Morsel Sales')

# Define the app layout using a more modular approach
app.layout = html.Div(
    children=[
        html.Header(
            children=[
                html.H1('Pink Morsel Sales Visualizer', id='header')
            ]
        ),
        html.Main(
            children=[
                dcc.Graph(
                    id='sales-chart',
                    figure=create_sales_chart(data)
                )
            ]
        )
    ]
)

# Only run the server if the script is executed directly
if __name__ == '__main__':
    app.run_server(debug=True)
