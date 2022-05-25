from . import requests
from . import pytest
from . import get_mockreturn
from . import google_api


# @pytest.mark.skip()
class TestGoogleMapAPI:
    def test_get_placeid(self, monkeypatch):
        expected_result = {
            'candidates': [{
                'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}],
            'status': 'OK'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_result))

        assert expected_result == google_api.get_placeid_from_address('openClassrooms')

    def test_get_address_api_from_placeid(self, monkeypatch):
        expected_result = {
            'html_attributions': [],
            'result': {
                'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                'geometry': {
                    'location': {'lat': 48.8975156, 'lng': 2.3833993},
                    'viewport': {
                        'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                        'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}}}},
            'status': 'OK'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_result))

        assert expected_result == \
               google_api.get_address_api_from_placeid('ChIJIZX8lhRu5kcRGwYk8Ce3Vc8')
