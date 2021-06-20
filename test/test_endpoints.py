import os
import requests
from openapi_spec_validator import validate_spec_url


def test_color_get_all(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'color')
    response = requests.get(endpoint)
    assert response.status_code == 200
    json = response.json()

    assert json is not None

