def get_mockreturn(
    candidate_places_result={}, about_a_place_result={}, wikipedia_places_result={}):
    """mock template call"""
    def mock_get(url, params):
        """Mock function on api object"""
        class JsonResponse:
            """mock result in JSON format"""
            @staticmethod
            def json():
                """Json method"""
                if url == "https://maps.googleapis.com/maps/api/place/findplacefromtext/json":
                    result = candidate_places_result
                elif url == "https://maps.googleapis.com/maps/api/place/details/json":
                    result = about_a_place_result
                elif url == "https://fr.wikipedia.org/w/api.php":
                    result = wikipedia_places_result
                else:
                    result = {}
                return result
        return JsonResponse()
    return mock_get


# --------------------------------------------------
# -- user's incomprehension  Mock--
# --------------------------------------------------
# ~ def get_user_incomprehension_googleMap_api_mockreturn():
    # ~ """mock template call"""
    # ~ def mock_get(url, params):
        # ~ """Mock function on api object"""
        # ~ class JsonResponse:
            # ~ """mock result in JSON format"""
            # ~ @staticmethod
            # ~ def json():
                # ~ """Json method"""
                # ~ return {
                    # ~ 'candidates': [], 'status': 'INVALID_REQUEST'}
        # ~ return JsonResponse()
    # ~ return mock_get


def expected_result_mock(
    get_candidate_places=False, about_a_place=False, get_wikipedia_places=False):
    """expected result for the mock return"""
    if get_candidate_places:
        #  'openClassrooms'
        return {
            'candidates': [{
                'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}],
                'status': 'OK'},
    if about_a_place:
        #  'openClassrooms > placeid > ChIJIZX8lhRu5kcRGwYk8Ce3Vc8' 
        return {
            'html_attributions': [],
            'result': {
                'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                'geometry': {
                    'location': {'lat': 48.8975156, 'lng': 2.3833993},
                    'viewport': {
                        'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                        'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}}}},
            'status': 'OK'}
    if get_wikipedia_places:
        return {
            # ~ "batchcomplete": True,
            "query": {
                "pages": [{
                    "pageid": 4338589,
                    "ns": 0,
                    "title": "OpenClassrooms",
                    "extract": "OpenClassrooms est un site web de formation..."}]
            }
        }
    return {}

