#!/usr/bin/env python
import requests
import google_api


def get_mockreturn(result):
    """mock template call"""
    def mock_get(url, params):
        """Mock function on api object"""
        class JsonResponse:
            """mock result in JSON format"""
            @staticmethod
            def json():
                """Json method"""
                return result
        return JsonResponse()
    return mock_get


class TestGoogleApi:
    def setup_method(self):
        self.place_id = google_api.get_placeid_from_address('openClassrooms')

    def test_get_placeid(self, monkeypatch):
        expected_result = {
            'candidates': [
                {
                     'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
                }
           ],
           'status' : 'OK'
        }
        mock_result = expected_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        result = self.place_id
        assert expected_result == result
