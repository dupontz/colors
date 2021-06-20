import os
import requests
import pytest
from openapi_spec_validator import validate_spec_url


def test_color_get_all(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'color')
    response = requests.get(endpoint)
    assert response.status_code == 200
    json = response.json()

    # duck-typed:
    assert hasattr(json, "__getitem__")
    assert isinstance(json, (list, tuple))


@pytest.mark.parametrize("test_input,expected",
                         [("1", "red"), ("2", "green"), ("3", "blue"), ("4", "cyan"), ("5", "magenta"), ("6", "yellow"),
                          ("7", "black")])
def test_color_has_initial_values(api_v1_host, test_input, expected):
    endpoint = os.path.join(api_v1_host, 'color', test_input)
    response = requests.get(endpoint)
    assert response.status_code == 200
    json = response.json()
    assert json['color'] == expected


def test_color_create(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'color/')
    payload = {'color': 'white', 'value': '#fff'}
    response = requests.post(endpoint, json=payload)
    assert response.status_code == 201

# TODO: check if spec is compatible with open API

# def test_swagger_specification(host):
#     endpoint = os.path.join(host, 'api', 'swagger.json')
#     validate_spec_url(endpoint)
#     # use https://editor.swagger.io/ to fix issues
