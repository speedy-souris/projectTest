"""google api config management menu"""
import os
import requests


def google_api_keys():
    """Internal Key Management Local / Production
         HEROKU_KEY_API_MAP / HEROKU_KEY_API_STATIC_MAP
         contain the private keys of GoogleMap APIs used in production environment .
         KEY_API_MAP / KEY_API_STATIC_MAP
         contain the private keys of GoogleMap APIs used in local environment"""
    if os.environ.get('HEROKU_KEY_API_MAP') is None:  # local internal key
        key_map = os.getenv('KEY_API_MAP')
        key_static_map = os.getenv('KEY_API_STATIC_MAP')
        has_status_prod = False
    else:  # internal production key
        key_map = os.getenv('HEROKU_KEY_API_MAP')
        key_static_map = os.getenv('HEROKU_KEY_API_STATIC_MAP')
        has_status_prod = True
    return key_map, key_static_map, has_status_prod


def get_url_from_json(url, params):
    """conversion of the address found in JSON format"""
    request = requests.get(url, params)
    url_json = request.json()
    return url_json


def get_settings_for_placeid_api(address):
    """determining placeid for the address found"""
    key = google_api_keys()[0]
    parameters = {'input': f'{address}', 'inputtype': 'textquery', 'key': f'{key}'}
    return parameters


def get_settings_for_address_api(placeid):
    """determining the localized address for the found placeid"""
    key = google_api_keys()[0]
    parameters ={
        'placeid': f'{placeid}', 
        'fields': 'formatted_address,geometry', 'key': f'{key}'}
    return parameters


def get_settings_for_map_static_api(location, address):
    """determination of the static map for the address found"""
    key = google_api_keys()[1]
    latitude = location['lat']
    longitude = location['lng']
    print(f'latitude = {latitude}')
    markers_data =\
     f"color:red|label:A|{latitude},{longitude}"
    parameters = {
        'center': f"{address}", 'zoom': '18.5',
        'size': '600x300', 'maptype': 'roadmap',
        'markers': f'{markers_data}', 'key': f'{key}'
    }
    return parameters


def get_placeid_from_address(address):
    """Google map API place_id search function
    Result ok with address to 'openClassrooms'
        {
            'candidates': [
                {
                     'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
                }
           ],
           'status' : 'OK'
        }"""
    url_api =\
     'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
    parameter_data = get_settings_for_placeid_api(address)
    placeid_value = get_url_from_json(url_api, parameter_data)
    return placeid_value


def get_address_api_from_placeid(placeid) -> object:
    """Google map API address search with place_id function
    Result OK with place_id 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
        {
            'html_attributions': [],
                'result': {
                    'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                    'geometry': {
                        'location': {'lat': 48.8975156, 'lng': 2.3833993},
                        'viewport': {
                            'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                            'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}}}},
                'status': 'OK'
        }"""
    url_api = 'https://maps.googleapis.com/maps/api/place/details/json'
    parameter_data = get_settings_for_address_api(placeid)
    address_api_value = get_url_from_json(url_api, parameter_data)
    return address_api_value


def get_static_map_from_address_api(json_from_wikipedia):
    """Display of the static map at the user's request"""
    location = json_from_wikipedia['result']['geometry']['location']
    address = json_from_wikipedia['result']['formatted_address']
    print(f'location = {location}')
    print(f'address = {address}')
    url_api = 'https://maps.googleapis.com/maps/api/staticmap'
    parameter_data = get_settings_for_map_static_api(location, address)
    map_static_api = requests.get(url=url_api, params=parameter_data)
    return map_static_api


def search_address_to_gMap(user_question_request):
    # DONE GoogleMap API calling
    """call of the GoogleMap APIs according to the user's request"""
    gmap_api_placeid_value = get_placeid_from_address(user_question_request)
    place_id = gmap_api_placeid_value['candidates'][0]['place_id']
    googleMap_data = get_address_api_from_placeid(place_id)
    return googleMap_data


if __name__ == '__main__':
    pass
