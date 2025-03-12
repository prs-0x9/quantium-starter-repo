import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import os

# Get absolute path to data file
current_dir = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(current_dir, "formatted_sales.csv")

# App color scheme
DATA_PATH = "./formatted_sales.csv"
COLORS = {
    "primary": "#FEDBFF",
    "secondary": "#D598EB",
    "font": "#522A61"
}

# Load the data
data = pd.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# Initialize the Dash app
app = Dash(__name__)

# Create the figure generation function
def generate_figure(chart_data):
    line_chart = px.line(chart_data, x="date", y="sales", title="Pink Morsel Sales")
    line_chart.update_layout(
        plot_bgcolor=COLORS["secondary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"]
    )
    return line_chart

# Layout of the app
app.layout = html.Div(
    [
        html.H1("Pink Morsel Visualizer", id="header", style={
            "background-color": COLORS["secondary"],
            "color": COLORS["font"],
            "border-radius": "20px"
        }),
        dcc.Graph(id="visualization", figure=generate_figure(data)),
        dcc.RadioItems(
            id="region_picker",
            options=[{"label": region, "value": region} for region in ["north", "east", "south", "west", "all"]],
            value="north",
            inline=True
        )
    ],
    style={
        "textAlign": "center",
        "background-color": COLORS["primary"],
        "border-radius": "20px"
    }
)