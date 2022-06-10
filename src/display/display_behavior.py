"""module of display of the user behavior  """
from . import data_expiration


def display_grandpy_status_code_to_home(chat_session):
    """billing of answers of grandpy for status home"""
    # user_behavior['grandpy_status_code'] = 'home'
    chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
        = chat_session.__class__.get_grandpy_status_key('home')
    grandpy_response = chat_session.__class__.read_grandpy_answer('home')
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_benevolent(chat_session):
    """billing of answers of grandpy for status benevolent"""
    # user_behavior['grandpy_status_code'] = 'benevolent'
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
        = chat_session.__class__.get_grandpy_status_key('benevolent')
    grandpy_response = chat_session.__class__.read_grandpy_answer('benevolent')
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_response(chat_session):
    """billing of answers of grandpy for status response"""
    # user_behavior['grandpy_status_code'] = 'response'
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
        = chat_session.__class__.get_grandpy_status_key('response')
    grandpy_response = chat_session.__class__.read_grandpy_answer('response')
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_tired(chat_session):
    """billing of answers of grandpy for status tired"""
    # user_behavior['grandpy_status_code'] = 'tired'
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
        = chat_session.__class__.get_grandpy_status_key('tired')
    grandpy_response = chat_session.__class__.read_grandpy_answer('tired')
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_inconsistency(chat_session):
    """billing of answers of grandpy for status incomprehension"""
    # user_behavior['grandpy_status_code'] = 'inconsistency'
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
        = chat_session.__class__.get_grandpy_status_key('inconsistency')
    grandpy_response = chat_session.__class__.read_grandpy_answer('inconsistency')
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_mannerless(chat_session):
    """billing of answers of grandpy for status mannerless"""
    # user_behavior['grandpy_status_code'] = 'mannerless'
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
        = chat_session.__class__.get_grandpy_status_key('mannerless')
    grandpy_response = chat_session.__class__.read_grandpy_answer('mannerless')
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_disrespectful(chat_session):
    """billing of answers of grandpy for status disrespectful"""
    # user_behavior['grandpy_status_code'] = 'disrespectful'
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
        = chat_session.__class__.get_grandpy_status_key('disrespectful')
    grandpy_response = chat_session.__class__.read_grandpy_answer('disrespectful')
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_incivility_limit(chat_session):
    """billing of answers of grandpy for status incivility_limit"""
    # user_behavior['grandpy_status_code'] = 'incivility_limit'
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
        = chat_session.__class__.get_grandpy_status_key('incivility_limit')
    grandpy_response = chat_session.__class__.read_grandpy_answer('incivility_limit')
    display_grandpy_status(chat_session, grandpy_response, following_billing=False)


def display_grandpy_status_code_to_indecency_limit(chat_session):
    """billing of answers of grandpy for status indecency_limit"""
    # user_behavior['grandpy_status_code'] = 'indecency_limit'
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
        = chat_session.__class__.get_grandpy_status_key('indecency_limit')
    grandpy_response = chat_session.__class__.read_grandpy_answer('indecency_limit')
    display_grandpy_status(chat_session, grandpy_response, following_billing=False)


def display_grandpy_status_code_to_incomprehension_limit(chat_session):
    """billing of answers of grandpy for status limit_incomprehension"""
    # user_behavior['grandpy_status_code'] = 'incomprehension_limit'
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
        = chat_session.__class__.get_grandpy_status_key('incomprehension_limit')
    grandpy_response = chat_session.__class__.read_grandpy_answer('incomprehension_limit')
    display_grandpy_status(chat_session, grandpy_response, following_billing=False)


def display_grandpy_status_code_to_exhausted(chat_session):
    """billing of answers of grandpy for status exhausted"""
    # user_behavior['grandpy_status_code'] = 'exhausted'
    grandpy_response = chat_session.__class__.read_grandpy_answer('exhausted')
    return grandpy_response


def display_correct_user_request_1_to_9(chat_session, response_grandpy):
    """billing of answers of grandpy X9 answer correct"""
    # user_behavior['number_of_user_entries'] == 1 to 4
    if 1 <= chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('number_of_user_entries')] <= 4:
        print(f' Utilisateur : {chat_session.user_entry}')
        print(f' Réponse de Grandpy (1-4): {response_grandpy}')
    # if user_behavior['number_of_user_entries'] == 5
    elif chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('number_of_user_entries')] == 5:
        print(f'Utilisateur (5) : {chat_session.user_entry}')
        print(f'Réponse de Grandpy (5-1): {response_grandpy}')
    # if user_behavior['number_of_entries'] == 6 to 9
    elif 6 <= chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('number_of_user_entries')] <= 9:
        # user_behavior['grandpy_status_code']= 'response'
        print(f'Utilisateur : {chat_session.user_entry}')
        print('Réponse de Grandpy (6-9) : '
              f'{display_grandpy_status_code_to_response(chat_session)}')


def display_last_user_request(chat_session, response_grandpy):
    """display of the last user's request before a 24 hours break"""
    print(f'Utilisateur fin: {chat_session.user_entry}')
    print(f'Réponse de Grandpy pre_fin: {response_grandpy}')
    print(f'Réponse de Grandpy fin: {display_grandpy_status_code_to_exhausted(chat_session)}')
    # has_fatigue_quotas_of_grandpy expire to 120 secondes (in theory 24h00)
    data_expiration(
        chat_session.__class__.get_user_behavior_key(
            'has_fatigue_quotas_of_grandpy'), chat_session.db_number)


def display_behavior_user_request(chat_session, response_grandpy):
    """display of the user's understanding"""
    # if user_behavior['number_of_user_entries'] == 1 to 9
    if 1 <= chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('number_of_user_entries')] <= 9:
        display_correct_user_request_1_to_9(chat_session, response_grandpy)
    # if user_behavior['has_user_indecency_status'] == True
    elif chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('has_user_indecency_status')]:
        print(f'Utilisateur 2 : {chat_session.user_entry}')
        print(f'Réponse de grandpy (indecency): {response_grandpy}')
    # if user_behavior['has_user_incomprehension_status'] == True
    elif chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('has_user_incomprehension_status')]:
        print(f'Utilisateur 3 : {chat_session.user_entry}')
        print(f'Réponse de grandpy (incomprehension): {response_grandpy}')
    # if user_behavior['has_user_incivility_status'] == True
    elif chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('has_user_incivility_status')]:
        print(f'Utilisateur 1: {chat_session.user_entry}')
        print(f'Réponse de Grandpy (incivility): {response_grandpy}')
    # if user_behavior['grandpy_status_code'] == 'benevolent'
    elif chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('benevolent'):
        print(f'Utilisateur : {chat_session.user_entry}')
        print(f'Réponse de Grandpy (benevolent): {response_grandpy}')


def display_grandpy_status(chat_session, response_grandpy, following_billing=True):
    """billing of status of grandpy just before its repose of 24 h 00"""
    # Termination of user requests (for 24H00)
    if not following_billing:
        chat_session.set_has_fatigue_quotas_of_grandpy(True)
        display_last_user_request(chat_session, response_grandpy)
    # Continue user queries
    elif following_billing:
        chat_session.set_has_fatigue_quotas_of_grandpy(False)
        display_behavior_user_request(chat_session, response_grandpy)
