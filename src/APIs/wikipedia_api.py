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
        'gslimit': '50',
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
    print(f'[wikipedia_as_page_url = {page_url}]')
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


def search_address_to_wiki(chat_object_connect, user_request_parsed):
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
    # ~ print(f'wiki_pages = {wiki_pages}')
    wiki_pages_list = [] # [{'score': 2, 'wikipedia_title':'rue shomberg'}]  
    score_list = [] # [0,1,0,1,2,...]
    if 'query' not in wiki_pages:
        return {'googleMap_data': {},
                    'wiki_page_result': ['', [], [], []]}
    for index, dict_of_pages in enumerate(wiki_pages['query']['geosearch']):
        wikipedia_title = dict_of_pages["title"]
        title_as_set = set(normalize_text(wikipedia_title).split(' '))
        formatted_address_as_set = \
            set(normalize_text(googleMap_data['result']['formatted_address']).split(' '))
        wiki_pages_list.append(
            {'score': len(title_as_set & formatted_address_as_set),
            'wikipedia_title': wikipedia_title})
        score_list.append(wiki_pages_list[index]['score'])
        # ~ print(f'title_as_set = {title_as_set }\nformatted_address_as_set = {formatted_address_as_set}')
        # ~ print(f"interception d'ensemble = {title_as_set & formatted_address_as_set}\n")
    # ~ print(f'wiki_pages_list = {wiki_pages_list}')
    # ~ print(f'score_list = {score_list}')
    score_max = max(score_list)
    index_score = [
        index for index, value_score in enumerate(score_list)
        if value_score == score_max
    ]
    print(wiki_pages_list[index_score[0]])
    # ~ score_max = max(score_list[]['score'])
    # ~ index_score_max_in_score_list = [i for i, j in enumarate(score_list) if j == score_max]
    # ~ best_page_wikipedia = score_list[index_score_max_in_score_list]
    # ~ print(best_page_wikipedia)
    try:
        # ~ title_as_set = title_as_set & formatted_address_as_set
        title = wiki_pages['query']['geosearch'][0]['title']
        # ~ print(f"test_wiki = {wiki_pages['query']['geosearch']}") 
        # ~ print(f'title = {title}')
        # ~ print(f"googleMap_data = {googleMap_data['result']['formatted_address']}")
        # ~ best_title = wiki_pages_list[index_score[0]]
        formatted_address = googleMap_data['result']['formatted_address']
        
    except (KeyError, IndexError):
        pass
    else:
        title = normalize_text(title)
        formatted_address = normalize_text(formatted_address)
        # ~ print(f'title2 = {title}')
        # ~ print(f'formatted_address2 = {formatted_address}')
        wiki_result = get_page_url(user_request_parsed)
        # ~ print(f'user_request = {user_request_parsed}')
        user_request_parsed = normalize_text(user_request_parsed)
        # ~ print(f'user_request2 = {user_request_parsed}')
        # ~ print(f'title = {title} formatted_address2 = {formatted_address}-> {title in formatted_address}')
        title_as_set = set(title.split(' '))
        formatted_address_as_set = set(formatted_address.split(' '))
        title_as_set.isdisjoint(formatted_address_as_set) 
        user_request_as_set = user_request_parsed.split(' ')
        # ~ print(f'[for wiki_result] title_as_set = {title_as_set} ')
        # ~ print(f'[for wiki_result] formatted_address_as_set = {formatted_address_as_set} ')
        # ~ print(f'[for wiki_result] user_request_as_set = {user_request_as_set}')
        if not title_as_set.isdisjoint(user_request_as_set ):
            wiki_result = get_page_url(user_request_parsed)
        elif not title_as_set.isdisjoint(formatted_address_as_set):
            wiki_result = get_page_url(formatted_address)
        else:
            wiki_result = wiki_result = get_page_url(title)
    result_apis = {
        'googleMap_data': googleMap_data,
        'wiki_page_result': wiki_result}
    return result_apis


def normalize_text(text):
    text = text.replace('-', ' ')
    text = text.replace(',', ' ')
    text = text.replace('.', ' ')
    text = text.lower()
    text = ''.join(
        (c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))
    unnecessary_as_set = frozenset({'le','la','les','de','du','des'})
    list_of_word_text = text.split()
    list_of_keyword = [
        w for w in list_of_word_text
        if w.lower() not in unnecessary_as_set]
    text = ' '.join(list_of_keyword)
    return text
    

if __name__ == '__main__':
    import google_api
    address = get_page_url('paris')
    print(f'url_address = {address}')
