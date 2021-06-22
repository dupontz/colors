import pytest
import json


def test_color_get_colors(test_client, init_database):
    response = test_client.get('api/color/')
    assert response.status_code == 200
    json_response = json.loads(response.data)


    assert isinstance(json_response, (list, tuple))
    # duck-typed:
    assert hasattr(json_response, "__getitem__")


@pytest.mark.parametrize("test_input,expected",
                         [("1", "red"), ("2", "green"), ("3", "blue"), ("4", "cyan"), ("5", "magenta"), ("6", "yellow"),
                          ("7", "black")])
def test_color_has_initial_values(test_client, init_database, test_input, expected):

    response = test_client.get('api/color/' + test_input)

    assert response.status_code == 200
    json_response = json.loads(response.data)
    assert json_response['color'] == expected


def test_color_create(test_client, init_database, ):
    payload = {'color': 'white', 'value': '#fff'}
    response = test_client.post('api/color/', json=payload)
    assert response.status_code == 201


