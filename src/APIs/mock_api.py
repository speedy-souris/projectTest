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


# ------------------------
# -- GoogleMap API  Mock--
# ------------------------
def get_place_id_googleMap_api_mockreturn(result):
    """mock template call"""
    def mock_get(address, params):
        """Mock function on api object"""
        class JsonResponse:
            """mock result in JSON format"""
            @staticmethod
            def json():
                """Json method"""
                return result
        return JsonResponse()
    return mock_get


def get_address_googleMap_api_mockreturn(result):
    """mock template call"""
    def mock_get(placeid, params):
        """Mock function on api object"""
        class JsonResponse:
            """mock result in JSON format"""
            @staticmethod
            def json():
                """Json method"""
                return result
        return JsonResponse()
    return mock_get
