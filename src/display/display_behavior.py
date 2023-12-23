"""module of display of the user behavior  """
from . import RedisDataManagement


def display_grandpy_status_code_to_home(chat_session):
    """billing of answers of grandpy for status home"""
    # grandpy_status_code = 'home'
    chat_session.grandpy_status_code = 'home'
    grandpy_response = chat_session.__class__.grandpy_status_code_value['home']
    display_grandpy_status(chat_session, grandpy_response )


def display_grandpy_status_code_to_response(chat_session):
    """billing of answers of grandpy for status response"""
    # grandpy_status_code = 'response'
    chat_session.grandpy_status_code = 'response'
    grandpy_response = chat_session.__class__.grandpy_status_code_value['response']
    display_grandpy_status(chat_session, grandpy_response )


def display_grandpy_status_code_to_response_limit(chat_session):
    """billing of answers of grandpy for status response_limit"""
    chat_session.grandpy_status_code = 'response_limit'
    grandpy_response = chat_session.__class__.grandpy_status_code_value['response_limit']
    display_grandpy_status(chat_session, grandpy_response, following_billing=False)


def display_grandpy_status_code_to_exhausted(chat_session):
    """billing of answers of grandpy for status exhausted"""
    # grandpy_status_code = 'exhausted'
    chat_session.grandpy_status_code = 'exhausted'
    grandpy_response = chat_session.__class__.grandpy_status_code_value['exhausted']
    return grandpy_response


def display_correct_user_request_1_to_9(chat_session, response_grandpy):
    """billing of answers of grandpy X9 answer correct"""
    # number_of_user_entries == 1 to 4
    number_of_user_entries = chat_session.number_of_user_entries
    if 1 <= number_of_user_entries <= 9:
        print(f' Utilisateur correct: {chat_session.user_entry}')
        print(f' Réponse de Grandpy (1-9): {response_grandpy}')


def display_behavior_user_request(chat_session, response_grandpy):
    """display of the user's understanding"""
    # if number_of_user_entries == 1 to 9
    number_of_user_entries = chat_session.number_of_user_entries
   
    if 1 < number_of_user_entries < 9:
        display_correct_user_request_1_to_9(chat_session, response_grandpy)


def display_grandpy_status(chat_session, response_grandpy, following_billing=True):
    """billing of status of grandpy just before its repose of 24 h 00"""
    # Termination of user requests (for 24H00)
    if not following_billing:
        print(f'limite atteinte = {chat_session.grandpy_status_code}')
        chat_session.has_fatigue_quotas_of_grandpy = True
        print(f'Utilisateur fin: {chat_session.user_entry}')
        print(f'Réponse de Grandpy pre_fin: {response_grandpy}')
        print(f'Réponse de Grandpy fin: {display_grandpy_status_code_to_exhausted(chat_session)}')
        # has_fatigue_quotas_of_grandpy expire to 120 secondes (in theory 24h00)
        # ~ chat_session.db_session.data_expiration()
    # Continue user queries
    elif following_billing:
        # ~ chat_session.has_fatigue_quotas_of_grandpy = False
        display_behavior_user_request(chat_session, response_grandpy)
