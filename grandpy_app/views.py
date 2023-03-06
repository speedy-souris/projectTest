import time
from . import Flask, render_template
from main import main
from src.redis_utilities import RedisDataManagement


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
    redis.database_init_by_default()
    return 'DataRedis initialized'


# Initialization of general parameters
@app.route('/index/<reflection>/<user_request>')
def answer_gp(reflection, user_request):
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
    chat_session = main(user_request)
    # sending parameters
    data_send = {
       'grandpy_code': chat_session.grandpy_status_code,
            # ~ 'map_status': {
            # ~ 'address': dataDiscussion.get('address', ''),
            # ~ 'map': dataDiscussion.get('map', ''),
            # ~ 'history': dataDiscussion.get('history', '')
        # ~ }
    }
    return data_send


if __name__ == '__main__':
    pass
