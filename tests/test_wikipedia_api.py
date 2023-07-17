from . import requests
from . import pytest
from . import get_mockreturn
from . import expected_result_mock
from . import wikipedia_api


class TestWikipediaApi:
    # ~ @pytest.mark.skip()
    # ~ def test_get_address_url(self, monkeypatch):
        # ~ expected_result = {
            # ~ 'batchcomplete': '', 
            # ~ 'query': {
                # ~ 'geosearch': [
                    # ~ {'pageid': 3120618, 'ns': 0, 'title': 'Quai de la Charente', 
                        # ~ 'lat': 48.895636, 'lon': 2.384586, 'dist': 226.3, 'primary': ''}]}}
        # ~ monkeypatch.setattr(requests, 'get', get_mockreturn(expected_result))

        # ~ assert expected_result == wikipedia_api.get_address_url(48.8975156, 2.3833993)

    # ~ @pytest.mark.skip()
    @staticmethod
    def test_get_page_url(monkeypatch):
        get_wikipedia_places = expected_result_mock(get_wikipedia_places=True)
        monkeypatch.setattr(
            requests, 'get', get_mockreturn(wikipedia_places_result=get_wikipedia_places))
        print(f'[test get_wikipedia_places] = {get_wikipedia_places}')
        print()
        print(f"[test wikipedia_api.get_page_url] = {wikipedia_api.get_page_url('OpenClassrooms')}")
        assert get_wikipedia_places == wikipedia_api.get_page_url('OpenClassrooms')
