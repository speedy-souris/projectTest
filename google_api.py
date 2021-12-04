#!/usr/bin/env python
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
        status_prod = False
    else:  # internal production key
        key_map = os.getenv('HEROKU_KEY_API_MAP')
        key_static_map = os.getenv('HEROKU_KEY_API_STATIC_MAP')
        status_prod = True
    return key_map, key_static_map, status_prod


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
    url_api = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
    parameter_data = get_settings_for_placeid_api(address)
    placeid_value = get_url_from_json(url_api, parameter_data)
    return placeid_value


