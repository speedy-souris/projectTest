def get_mockreturn(result_placeid, result_address):
    """mock template call"""
    def mock_get(url, params):
        """Mock function on api object"""
        class JsonResponse:
            """mock result in JSON format"""
            @staticmethod
            def json():
                """Json method"""
                if url == "https://maps.googleapis.com/maps/api/place/findplacefromtext/json":
                    #  'openClassrooms'
                    result_place_id = {
                        'candidates': [
                                            {
                                                'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
                                            }
                                            ],
                        'status' : 'OK'}
                    result = result_place_id
                elif url == "https://maps.googleapis.com/maps/api/place/details/json":
                     #  'openClassrooms > placeid > ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
                    result_address = {
                        'html_attributions': [],
                        'result': {
                                        'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                                        'geometry': {
                                                            'location': {'lat': 48.8975156, 'lng': 2.3833993},
                                                            'viewport': {
                                                                                'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                                                                                'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}}}},
                        'status': 'OK'}
                    result = result_address
                else:
                    result = {}
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

