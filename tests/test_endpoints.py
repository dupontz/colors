import os
import requests
import pytest
import json
from openapi_spec_validator import validate_spec_url


def test_color_get_colors(test_client, init_database):
    # endpoint = os.path.join(api_v1_host, 'color')
    # response = requests.get(endpoint)
    response = test_client.get('api/color/')
    assert response.status_code == 200
    json_response = json.loads(response.data)

    # duck-typed:
    assert hasattr(json_response, "__getitem__")
    assert isinstance(json_response, (list, tuple))


@pytest.mark.parametrize("test_input,expected",
                         [("1", "red"), ("2", "green"), ("3", "blue"), ("4", "cyan"), ("5", "magenta"), ("6", "yellow"),
                          ("7", "black")])
def test_color_has_initial_values(test_client, init_database, test_input, expected):
    # endpoint = os.path.join(api_v1_host, 'color', test_input)
    # response = requests.get(endpoint)

    response = test_client.get('api/color/' + test_input)

    assert response.status_code == 200
    json_response = json.loads(response.data)
    assert json_response['color'] == expected


def test_color_create(test_client, init_database, ):
    # endpoint = os.path.join(api_v1_host, 'color/')
    payload = {'color': 'white', 'value': '#fff'}
    # response = requests.post(endpoint, json=payload)
    response = test_client.post('api/color/', json=payload)
    assert response.status_code == 201

# TODO: check if spec is compatible with open API

# def test_swagger_specification(host):
#     endpoint = os.path.join(host, 'api', 'swagger.json')
#     validate_spec_url(endpoint)
#     # use https://editor.swagger.io/ to fix issues
