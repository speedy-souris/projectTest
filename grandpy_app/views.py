import time
import base64
from . import Flask, render_template
from main import main
from src.redis_utilities import RedisDataManagement
from src.APIs import wikipedia_api, google_api


app = Flask(__name__)

# main function for displaying answers
@app.route('/')
def index():
    """
        Initialization of the index.html page
        single home page
    """
    return render_template('index.html')


# initialization DataRedis
@app.route('/init')
def init():
    """
        Initialization of the dataRedis
    """
    redis = RedisDataManagement(db_number=0)
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
    chat_session = main(user_question_request)
    wiki_response = wikipedia_api.search_address_to_wiki(chat_session.user_entry)
    static_map_display = google_api.get_static_map_from_address_api(
        wiki_response['googleMap_data'])
    # sending parameters
    data_send = {
        'grandpy_status_code': chat_session.grandpy_status_code,
        'address': user_question_request,
        'map': base64.b64encode(static_map_display).decode('utf-8'),
        'history': wiki_response['wiki_page_result']
    }
    # ~ print(f'data_send = {data_send}')
    return data_send


if __name__ == '__main__':
    pass
