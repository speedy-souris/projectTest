from . import requests
from . import pytest
from . import get_mockreturn
from . import expected_result_mock
from . import google_api


# ~ @pytest.mark.skip()
class TestGoogleMapAPI:
    # ~ @staticmethod
    # ~ def expected_result_mock(
        # ~ get_candidate_places=False, about_a_place=False, get_wikipedia_places=False):
        # ~ """expected result for the mock return"""
        # ~ if get_candidate_places:
            # ~ #  'openClassrooms'
            # ~ return {
                # ~ 'candidates': [{
                    # ~ 'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}],
                    # ~ 'status': 'OK'},
        # ~ if about_a_place:
            # ~ #  'openClassrooms > placeid > ChIJIZX8lhRu5kcRGwYk8Ce3Vc8' 
            # ~ return {
                # ~ 'html_attributions': [],
                # ~ 'result': {
                    # ~ 'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                    # ~ 'geometry': {
                        # ~ 'location': {'lat': 48.8975156, 'lng': 2.3833993},
                        # ~ 'viewport': {
                            # ~ 'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                            # ~ 'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}}}},
                # ~ 'status': 'OK'}
        # ~ if get_wikipedia_places:
            # ~ {
                # ~ "batchcomplete": True,
                # ~ "query": {
                    # ~ "pages": [{
                        # ~ "pageid": 4338589,
                        # ~ "ns": 0,
                        # ~ "title": "OpenClassrooms",
                        # ~ "extract": "OpenClassrooms est un site web de formation..."}]}
            # ~ }
        # ~ return {}

    def test_get_placeid(self, monkeypatch):
        get_candidate_places = expected_result_mock(get_candidate_places=True)
        monkeypatch.setattr(
            requests, 'get', get_mockreturn(candidate_places_result=get_candidate_places))

        assert get_candidate_places == \
            google_api.get_placeid_from_address('openClassrooms')

    #@pytest.mark.skip()
    def test_get_address_api_from_placeid(self, monkeypatch):
        about_a_place = expected_result_mock(about_a_place=True)
        monkeypatch.setattr(
            requests, 'get', get_mockreturn(about_a_place_result=about_a_place))

        assert about_a_place == \
            google_api.get_address_api_from_placeid('ChIJIZX8lhRu5kcRGwYk8Ce3Vc8')
