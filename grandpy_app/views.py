import logging
from logging.handlers import RotatingFileHandler
import time
import base64
from . import Flask, render_template
from flask import request
from main import main
from src.redis_utilities import RedisDataManagement
from src.APIs import wikipedia_api, google_api
from wikimarkup.parser import Parser


app = Flask(__name__)

# Configuration du niveau de journalisation (DEBUG pour tous les niveaux)
app.logger.setLevel(logging.DEBUG)
# Configuration d'un gestionnaire RotatingFileHandler pour les logs
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
# Ajout du gestionnaire à l'enregistreur par défaut de l'application Flask
app.logger.addHandler(handler)

# main function for displaying answers
@app.route('/')
def index():
    """
        Initialization of the index.html page
        single home page
    """
    # Récupérer l'URL de la requête en cours
    current_url = request.url
    app.logger.debug(f"URL de la requête : {current_url}")

    return render_template('index2.html')


# initialization DataRedis
@app.route('/init')
def init():
    """
        Initialization of the dataRedis
    """
    redis = RedisDataManagement(database_redis_number=0)
    redis.redis_database_init_by_default()
    return 'DataRedis initialized'


# Initialization of general parameters
@app.route('/index/<reflection>/<user_question_request>')
def answer_gp(reflection, user_question_request):
    """grandpy's response display function
        setting the parameter for grandpy's responses
        general variable to count grandpy's responses
        and the state of civility in the questions
        as well as the different coordinates for the display of the map
            - quotas_api
            - civility
            - decency
            - nb_request
            - comprehension
            - address (answer and data map)
            - history
            - location"""
    # grandpy's reflection time to answer questions
    time_reflection = time.sleep(int(reflection))
    # exchange between the user and grandpy
    chat_connect_object = main(user_question_request)
    print(f'[views1] = {chat_connect_object.parsed_user_entry}' )
    coordinates_googleMap_API = chat_connect_object.coordinates_api
    print(f'[views1.5] = { coordinates_googleMap_API}')
   
    wiki_response = \
        wikipedia_api.search_address_to_wiki(
            chat_connect_object, chat_connect_object.parsed_user_entry, 
            coordinates_googleMap_API)
    print(f'[views2] = {wiki_response}')
    
    try:
        wiki_response['wiki_page_result'] = \
            wiki_response['wiki_page_result']['query']['pages'][0]['extract']
    except TypeError:
        wiki_response['wiki_page_result'] = 'page wiki vide'
    print(f'[views.py] = {wiki_response}')
    static_map_display = google_api.get_static_map_from_address_api(
        wiki_response['googleMap_data'])
# sending parameters
    parser = Parser()
    data_send = {
        'grandpy_status_code': chat_connect_object.grandpy_status_code,
        'address': user_question_request,
        'map': base64.b64encode(static_map_display).decode('utf-8'),
        'history': parser.parse(wiki_response['wiki_page_result'])
    }
    return data_send


if __name__ == '__main__':
    pass
