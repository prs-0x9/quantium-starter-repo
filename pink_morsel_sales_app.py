import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Path to the formatted data
DATA_PATH = "./formatted_sales.csv"
COLORS = {
    "background": "#F0E0FF",
    "highlight": "#C16BDB",
    "text": "#3E145F"
}

# Load the dataset and sort by date
data = pd.read_csv(DATA_PATH)
data['date'] = pd.to_datetime(data['date'])
data = data.sort_values(by="date")

# Initialize Dash app
app = Dash(__name__)

# Function to generate the figure
def create_figure(filtered_data):
    fig = px.line(filtered_data, x="date", y="sales", title="Pink Morsel Sales Over Time")
    fig.update_layout(
        plot_bgcolor=COLORS["highlight"],
        paper_bgcolor=COLORS["background"],
        font_color=COLORS["text"],
        title={'x': 0.5, 'xanchor': 'center'},
        xaxis_title="Date",
        yaxis_title="Sales"
    )
    return fig

# Create the line chart component
chart = dcc.Graph(
    id="sales-chart",
    figure=create_figure(data)
)

# Header Section
header = html.H1(
    "Pink Morsel Sales Dashboard",
    id="app-header",
    style={
        "background-color": COLORS["highlight"],
        "color": COLORS["text"],
        "padding": "15px",
        "border-radius": "10px"
    }
)

# Region selection (radio buttons)
region_selector = dcc.RadioItems(
    options=[
        {"label": "North", "value": "north"},
        {"label": "East", "value": "east"},
        {"label": "South", "value": "south"},
        {"label": "West", "value": "west"},
        {"label": "All Regions", "value": "all"}
    ],
    value="all",
    id="region-selector",
    inline=True
)

# Wrapper for the region selector
region_selector_wrapper = html.Div(
    [
        html.Label("Choose Region:"),
        region_selector
    ],
    style={
        "font-size": "120%",
        "margin-top": "20px"
    }
)

# Callback to update the chart based on selected region
@app.callback(
    Output(chart, "figure"),
    Input(region_selector, "value")
)
def update_chart(region):
    if region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["region"] == region]

    return create_figure(filtered_data)

# Layout of the app
app.layout = html.Div(
    [
        header,
        region_selector_wrapper,
        chart
    ],
    style={
        "textAlign": "center",
        "background-color": COLORS["background"],
        "border-radius": "15px",
        "padding": "20px"
    }
)

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)