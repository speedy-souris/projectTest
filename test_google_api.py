#!/usr/bin/env python
import requests
from mock_api import get_mockreturn
import google_api


def test_get_placeid(monkeypatch):
    place_id = google_api.get_placeid_from_address('openClassrooms')
    expected_result = {
        'candidates': [{'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}],
        'status' : 'OK'
    }
    mock_result = expected_result
    mockreturn = get_mockreturn(mock_result)
    monkeypatch.setattr(requests, 'get', mockreturn)
    result = place_id
    assert expected_result == result


def test_get_address_api_from_placeid(monkeypatch):
    address_placeid = google_api.get_address_api_from_placeid('ChIJIZX8lhRu5kcRGwYk8Ce3Vc8')
    expected_result = {
        'html_attributions': [],
        'result': {
            'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
            'geometry': {
                'location': {'lat': 48.8975156, 'lng': 2.3833993},
                'viewport': {
                    'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                    'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}
                }
            }
        },
        'status': 'OK'
    }
    mock_result = expected_result
    mockreturn = get_mockreturn(mock_result)
    monkeypatch.setattr(requests, 'get', mockreturn)
    result = address_placeid
    assert expected_result == result
