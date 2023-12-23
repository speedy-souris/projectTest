from . import requests
from . import pytest
from . import get_mockreturn
from . import expected_result_mock
from . import wikipedia_api


class TestWikipediaApi:
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
