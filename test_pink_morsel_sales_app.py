import pytest
from dash.testing.application_runners import import_app

@pytest.fixture
def app():
    return import_app("pink_morsel_sales_app")

def test_header_exists(dash_duo, app):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=5)

def test_visualization_exists(dash_duo, app):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#visualization", timeout=5)

def test_region_picker_exists(dash_duo, app):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region_picker", timeout=5)