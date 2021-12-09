#!/usr/bin/env python


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