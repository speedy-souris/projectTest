"""management of wikimedia APIs settings"""
import requests
import unicodedata
from . import google_api


def get_localization_data(latitude, longitude):
    """localization data"""
    data = {
        'format': 'json',
        'list': 'geosearch',
        'gscoord': f'{latitude}|{longitude}',
        'gslimit': '10',
        'gsradius': '10000',
        'action': 'query'}
    return data


def get_page_data(title):
    """wiki page data"""
    data = {
       'action': 'query',
       'titles': f'{title}',
       'prop': 'extracts',
       'formatversion': '2',
       'format': 'json',
       'exsentences': '2',
       'exlimit': '1',
       'explaintext': '1'}
    return data


def get_url_json(url, params):
    """conversion of the address found in JSON format"""
    request = requests.get(url=url, params=params)
    url = request.json()
    return url


def get_page_url(title):
    """wikipedia API (Wikimedia) history search
    {
        "batchcomplete": True,
        "query": {
            "pages": [{
                "pageid": 4338589,
                "ns": 0,
                "title": "OpenClassrooms",
                "extract": "OpenClassrooms est un site web de formation..."
    }]}}"""
    params = get_page_data(title)
    url = 'https://fr.wikipedia.org/w/api.php'
    params = get_page_data(title)
    page_url = get_url_json(url=url, params=params)
    # ~ print(f'page_url = {page_url}')
    if page_url['query']['pages'][0]['extract'] != '':
        return page_url['query']['pages'][0]['extract']
    if page_url[3] != []:
        return page_url[3]
    else:
        return ['',[], [], []]


def get_address_url(latitude, longitude):
    """{
    'batchcomplete': '', 
    'query': {
        'geosearch': [{
            'pageid': 3120618, 'ns': 0, 'title': 'Quai de la Charente',
            'lat': 48.895636, 'lon': 2.384586, 'dist': 226.3, 'primary': ''}]}}"""
    url = 'https://fr.wikipedia.org/w/api.php'
    params = get_localization_data(latitude, longitude)
    address_url = get_url_json(url=url, params=params)
    return address_url


def search_address_to_wiki(user_request_parsed):
    # DONE WIKIPEDIA API calling
    """call of the WikiPedia APIs according to the user's request"""
    googleMap_data = google_api.search_address_to_gMap(user_request_parsed)
    try:
        latitude = \
            googleMap_data['result']['geometry']['location']['lat']
        longitude = \
            googleMap_data['result']['geometry']['location']['lng']
    except KeyError:
        wiki_pages = {}
    else:
        wiki_pages= get_address_url(latitude, longitude)
    wiki_result = None
    try:
        title = wiki_pages['query']['geosearch'][0]['title']
        print(f'title = {title}')
        print(f"googleMap_data = {googleMap_data['result']['formatted_address']}")
        formatted_address = googleMap_data['result']['formatted_address']
        
    except (KeyError, IndexError):
        pass
    else:
        title = normalize_text(title)
        formatted_address = normalize_text(formatted_address)
        print(f'title2 = {title}')
        print(f'formatted_address2 = {formatted_address}')
        # ~ wiki_result = get_page_url(user_request_parsed)
        print(f'user_request = {user_request_parsed}')
        user_request_parsed = normalize_text(user_request_parsed)
        print(f'user_request2 = {user_request_parsed}')
        print(f'title = {title} formatted_address2 = {formatted_address}-> {title in formatted_address}')
        title_as_set = set(title.split(' '))
        formatted_address_as_set = set(formatted_address.split(' '))
        title_as_set.isdisjoint(formatted_address_as_set) 
        if not title_as_set.isdisjoint(formatted_address_as_set):
            wiki_result = get_page_url(user_request_parsed)
        else:
            wiki_result = 'le wiki est vide !'
    result_apis = {
        'googleMap_data': googleMap_data,
        'wiki_page_result': wiki_result
    }
    return result_apis


def normalize_text(text):
    text = text.replace('-', ' ')
    text = text.replace(',', ' ')
    text = text.replace('.', ' ')
    text = ''.join(
        (c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))
    return text.lower()
    

if __name__ == '__main__':
    import google_api
    address = get_page_url('paris')
    print(f'url_address = {address}')
