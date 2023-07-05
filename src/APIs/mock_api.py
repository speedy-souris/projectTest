def get_mockreturn(
    result_googleMap_placeid, result_googleMap_address, result_wikipedia_page):
    """mock template call"""
    def mock_get(url, params):
        """Mock function on api object"""
        class JsonResponse:
            """mock result in JSON format"""
            @staticmethod
            def json():
                """Json method"""
                if url == "https://maps.googleapis.com/maps/api/place/findplacefromtext/json":
                    result = result_googleMap_placeid
                elif url == "https://maps.googleapis.com/maps/api/place/details/json":
                    result = result_googleMap_address
                else:
                    result = {}
                return result
        return JsonResponse()
    return mock_get


# --------------------------------------------------
# -- user's incomprehension  Mock--
# --------------------------------------------------
def get_user_incomprehension_googleMap_api_mockreturn():
    """mock template call"""
    def mock_get(url, params):
        """Mock function on api object"""
        class JsonResponse:
            """mock result in JSON format"""
            @staticmethod
            def json():
                """Json method"""
                return {
                    'candidates': [], 'status': 'INVALID_REQUEST'}
        return JsonResponse()
    return mock_get



