import requests

API_URL = 'http://localhost:5000/celsius'

def test_api_converts_fahrenheit():
    degrees_f = 32
    degrees_c = 0
    path = '{}?fahrenheit={}'.format(API_URL, degrees_f)
    response = requests.get(path)
    assert float(response.content) == degrees_c


def test_api_rounds_down():
    degrees_f = 100
    degrees_c = 37  # rounded down
    path = '{}?fahrenheit={}'.format(API_URL, degrees_f)
    response = requests.get(path)
    assert float(response.content) == degrees_c


def test_api_returns_error_if_no_degrees():
    response = requests.get(API_URL)
    assert 'No degrees' in response.content
