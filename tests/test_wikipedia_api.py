from . import requests
from . import pytest
from . import get_mockreturn
from . import wikipedia_api


class TestWikipediaApi:
    def test_get_address_url(self, monkeypatch):
        expected_result = {
            'batchcomplete': '', 
            'query': {
                'geosearch': [
                    {'pageid': 3120618, 'ns': 0, 'title': 'Quai de la Charente', 
                        'lat': 48.895636, 'lon': 2.384586, 'dist': 226.3, 'primary': ''}]}}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_result))

        assert expected_result == wikipedia_api.get_address_url(48.8975156, 2.3833993)

    # ~ @pytest.mark.skip()
    def test_get_page_url(self, monkeypatch):
        expected_result = {
        "batchcomplete": True,
        "query": {
            "pages": [{
                "pageid": 4338589, "ns": 0, "title": "OpenClassrooms",
                'extract': "OpenClassrooms est un site web de formation en ligne," \
                    "créé en 1999 sous le nom de Site du Zéro."\
                    " Il propose à ses membres des cours certifiants et des parcours"\
                    " débouchant sur des métiers en croissance."}]}}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_result))

        assert expected_result['query']['pages'][0]['extract'] == wikipedia_api.get_page_url('OpenClassrooms')
