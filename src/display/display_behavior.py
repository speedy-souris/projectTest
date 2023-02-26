"""module of display of the user behavior  """
from . import RedisDataManagement


# def read_grandpy_answer(chat_session, grandpy_code) -> str:
#     grandpy_answer = chat_session.grandpy_code
#     return grandpy_answer


def display_grandpy_status_code_to_home(chat_session):
    """billing of answers of grandpy for status home"""
    # grandpy_status_code = 'home'
    chat_session.grandpy_status_code = 'home'
    grandpy_response = chat_session.__class__.grandpy_status_code_value['home']
    display_grandpy_status(chat_session, grandpy_response )


def display_grandpy_status_code_to_benevolent(chat_session):
    """billing of answers of grandpy for status benevolent"""
    # grandpy_status_code = 'benevolent'
    chat_session.grandpy_status_code = 'benevolent'
    chat_session.level = 2
    grandpy_response = \
        display_grandpy_status(chat_session, chat_session.__class__.grandpy_status_code_value['benevolent'])


def display_grandpy_status_code_to_response(chat_session):
    """billing of answers of grandpy for status response"""
    # grandpy_status_code = 'response'
    chat_session.grandpy_status_code = 'response'
    grandpy_response = chat_session.__class__.grandpy_status_code_value['response']
    display_grandpy_status(chat_session, grandpy_response )


def display_grandpy_status_code_to_tired(chat_session):
    """billing of answers of grandpy for status tired"""
    # grandpy_status_code = 'tired'
    chat_session.grandpy_status_code = 'tired'
    grandpy_response = \
        display_grandpy_status(chat_session, chat_session.__class__.grandpy_status_code_value['tired'])


def display_grandpy_status_code_to_response_limit(chat_session):
    """billing of answers of grandpy for status response_limit"""
    chat_session.grandpy_status_code = 'response_limit'
    grandpy_response = chat_session.__class__.grandpy_status_code_value['response_limit']
    display_grandpy_status(chat_session, grandpy_response, following_billing=False)

def display_grandpy_status_code_to_incomprehension(chat_session):
    """billing of answers of grandpy for status incomprehension"""
    # grandpy_status_code = 'incomprehension'
    chat_session.grandpy_status_code = 'incomprehension'
    grandpy_response = \
        display_grandpy_status(chat_session, chat_session.__class__.grandpy_status_code_value['incomprehension'])


def display_grandpy_status_code_to_mannerless(chat_session):
    """billing of answers of grandpy for status mannerless"""
    # grandpy_status_code = 'mannerless'
    chat_session.grandpy_status_code = 'mannerless'
    grandpy_response = chat_session.__class__.grandpy_status_code_value['mannerless']
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_disrespectful(chat_session):
    """billing of answers of grandpy for status disrespectful"""
    # grandpy_status_code = 'disrespectful'
    chat_session.grandpy_status_code = 'disrespectful'
    grandpy_response = chat_session.__class__.grandpy_status_code_value['disrespectful']
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_incivility_limit(chat_session):
    """billing of answers of grandpy for status incivility_limit"""
    # grandpy_status_code = 'incivility_limit'
    chat_session.grandpy_status_code = 'incivility_limit'
    grandpy_response = chat_session.__class__.grandpy_status_code_value['incivility_limit']
    display_grandpy_status(chat_session, grandpy_response, following_billing=False)


def display_grandpy_status_code_to_indecency_limit(chat_session):
    """billing of answers of grandpy for status indecency_limit"""
    # grandpy_status_code = 'indecency_limit'
    chat_session.grandpy_status_code = 'indecency_limit'
    grandpy_response = chat_session.__class__.grandpy_status_code_value['indecency_limit']
    display_grandpy_status(chat_session, grandpy_response, following_billing=False)


def display_grandpy_status_code_to_incomprehension_limit(chat_session):
    """billing of answers of grandpy for status limit_incomprehension"""
    # grandpy_status_code = 'incomprehension_limit'
    chat_session.grandpy_status_code = 'incomprehension_limit'
    grandpy_response = chat_session.__class__.grandpy_status_code_value['incomprehension_limit']
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
    if 1 <= number_of_user_entries <= 4:
        print(f' Utilisateur correct: {chat_session.user_entry}')
        print(f' Réponse de Grandpy (1-4): {response_grandpy}')
    # number_of_user_entries == 5
    elif number_of_user_entries == 5:
        print(f'Utilisateur correct: {chat_session.user_entry}')
        print(f'Réponse de Grandpy faiblesse: {response_grandpy}')
    # if number_of_entries == 6 to 9
    elif 6 <= number_of_user_entries <= 10:
        # grandpy_status_code= 'response'
        print(f'Utilisateur correct: {chat_session.user_entry}')
        # ~ print('Réponse de Grandpy (6-9) : '
              # ~ f'{display_grandpy_status_code_to_response(chat_session)}')


# def display_last_user_request(chat_session, response_grandpy):
#     """display of the last user's request before a 24 hours break"""
#     print(f'Utilisateur fin: {chat_session.user_entry}')
#     print(f'Réponse de Grandpy pre_fin: {response_grandpy}')
#     print(f'Réponse de Grandpy fin: {display_grandpy_status_code_to_exhausted(chat_session)}')
#     # has_fatigue_quotas_of_grandpy expire to 120 secondes (in theory 24h00)
#     data_expiration(
#         chat_session.__class__.get_user_behavior_key(
#             'has_fatigue_quotas_of_grandpy'), chat_session.db_number)


def display_behavior_user_request(chat_session, response_grandpy):
    """display of the user's understanding"""
    # if number_of_user_entries == 1 to 9
    number_of_user_entries = chat_session.number_of_user_entries
    number_of_user_incivility = chat_session.number_of_user_incivility
    if 1 < number_of_user_entries < 9:
        display_correct_user_request_1_to_9(chat_session, response_grandpy)
    # if has_user_indecency_status == True
    if chat_session.has_user_indecency_status:
        print(f'Utilisateur grossier : {chat_session.user_entry}')
        print(f'Réponse de grandpy (indecency): {response_grandpy}')
    # if has_user_incomprehension_status == True
    if chat_session.has_user_incomprehension_status:
        print(f'Utilisateur incomprehensible : {chat_session.user_entry}')
        print(f'Réponse de grandpy (incomprehension): {response_grandpy}')
    # if has_user_incivility_status == True
    if chat_session.has_user_incivility_status:
        print(f'Utilisateur malpolis: {chat_session.user_entry}')
        print(f'Réponse de Grandpy (incivility): {response_grandpy}')
    # if grandpy_status_code == 'benevolent'
    if chat_session.grandpy_status_code == 'benevolent':
        print(f'Utilisateur correct : {chat_session.user_entry}')
        print(f'Réponse de Grandpy (benevolent): {response_grandpy}')
    # ~ else:
        # ~ print(f'Réponse de Grandpy (home): {response_grandpy}')


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
