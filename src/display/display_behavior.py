"""module of display of the user behavior  """
from . import RedisDataManagement


# def read_grandpy_answer(chat_session, grandpy_code) -> str:
#     grandpy_answer = chat_session.grandpy_code
#     return grandpy_answer


def display_grandpy_status_code_to_home(chat_session):
    """billing of answers of grandpy for status home"""
    # grandpy_status_code = 'home'
    chat_session.grandpy_status_code = 'home'
    grandpy_response = chat_session.__class__.home
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_benevolent(chat_session):
    """billing of answers of grandpy for status benevolent"""
    # grandpy_status_code = 'benevolent'
    chat_session.grandpy_status_code = 'benevolent'
    grandpy_response = chat_session.__class__.benevolent
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_response(chat_session):
    """billing of answers of grandpy for status response"""
    # grandpy_status_code = 'response'
    chat_session.grandpy_status_code = 'response'
    grandpy_response = chat_session.__class__.response
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_tired(chat_session):
    """billing of answers of grandpy for status tired"""
    # grandpy_status_code = 'tired'
    chat_session.grandpy_status_code = 'tired'
    grandpy_response = chat_session.__class__.tired
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_incomprehension(chat_session):
    """billing of answers of grandpy for status incomprehension"""
    # grandpy_status_code = 'incomprehension'
    chat_session.grandpy_status_code = 'incomprehension'
    grandpy_response = chat_session.__class__.incomprehension
    display_grandpy_status(chat_session, grandpy_response)


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
    grandpy_response = chat_session.__class__.disrespectful
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_incivility_limit(chat_session):
    """billing of answers of grandpy for status incivility_limit"""
    # grandpy_status_code = 'incivility_limit'
    chat_session.grandpy_status_code = 'incivility_limit'
    grandpy_response = chat_session.__class__.incivility_limit
    display_grandpy_status(chat_session, grandpy_response, following_billing=False)


def display_grandpy_status_code_to_indecency_limit(chat_session):
    """billing of answers of grandpy for status indecency_limit"""
    # grandpy_status_code = 'indecency_limit'
    chat_session.grandpy_status_code = 'indecency_limit'
    grandpy_response = chat_session.__class__.indecency_limit
    display_grandpy_status(chat_session, grandpy_response, following_billing=False)


def display_grandpy_status_code_to_incomprehension_limit(chat_session):
    """billing of answers of grandpy for status limit_incomprehension"""
    # grandpy_status_code = 'incomprehension_limit'
    chat_session.grandpy_status_code = 'incomprehension_limit'
    grandpy_response = chat_session.__class__.incomprehension_limit
    display_grandpy_status(chat_session, grandpy_response, following_billing=False)


def display_grandpy_status_code_to_exhausted(chat_session):
    """billing of answers of grandpy for status exhausted"""
    # grandpy_status_code = 'exhausted'
    chat_session.grandpy_status_code = 'exhausted'
    grandpy_response = chat_session.__class__.exhausted
    return grandpy_response


def display_correct_user_request_1_to_9(chat_session, response_grandpy):
    """billing of answers of grandpy X9 answer correct"""
    # number_of_user_entries == 1 to 4
    number_of_user_entries = chat_session.number_of_user_entries
    if 1 <= number_of_user_entries <= 4:
        print(f' Utilisateur : {chat_session.user_entry}')
        print(f' Réponse de Grandpy (1-4): {response_grandpy}')
    # number_of_user_entries == 5
    elif number_of_user_entries == 5:
        print(f'Utilisateur (5) : {chat_session.user_entry}')
        print(f'Réponse de Grandpy (5-1): {response_grandpy}')
    # if number_of_entries == 6 to 9
    elif 6 <= number_of_user_entries <= 9:
        # grandpy_status_code= 'response'
        print(f'Utilisateur : {chat_session.user_entry}')
        print('Réponse de Grandpy (6-9) : '
              f'{display_grandpy_status_code_to_response(chat_session)}')


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
    print(f"[display_incivility] avant le if = {chat_session.number_of_user_incivility}")
    number_of_user_entries = chat_session.number_of_user_entries
    print(f'user_entries [display_user_request] = {number_of_user_entries}')
    number_of_user_incivility = chat_session.number_of_user_incivility
    print(f'[display_behavior] number_of_user_indivility = {number_of_user_incivility}')
    if 1 < number_of_user_entries < 9:
        print(f"[display_incivility apres] = {number_of_user_incivility}")
        display_correct_user_request_1_to_9(chat_session, response_grandpy)
    # if has_user_indecency_status == True
    if chat_session.has_user_indecency_status:
        print(f'Utilisateur 2 : {chat_session.user_entry}')
        print(f'Réponse de grandpy (indecency): {response_grandpy}')
    # if has_user_incomprehension_status == True
    if chat_session.has_user_incomprehension_status:
        print(f'Utilisateur 3 : {chat_session.user_entry}')
        print(f'Réponse de grandpy (incomprehension): {response_grandpy}')
    # if has_user_incivility_status == True
    if chat_session.has_user_incivility_status:
        print(f'Utilisateur 1: {chat_session.user_entry}')
        print(f'Réponse de Grandpy (incivility): {response_grandpy}')
    # if grandpy_status_code == 'benevolent'
    if chat_session.grandpy_status_code == 'benevolent':
        print(f'Utilisateur : {chat_session.user_entry}')
        print(f'Réponse de Grandpy (benevolent): {response_grandpy}')
    print(f"[display_incivility hors condition] = {number_of_user_incivility}")


def display_grandpy_status(chat_session, response_grandpy, following_billing=True, db_number=0):
    """billing of status of grandpy just before its repose of 24 h 00"""
    db_session = RedisDataManagement(bd_number=db_number)
    # Termination of user requests (for 24H00)
    if not following_billing:
        print(f"display status = {chat_session.user_behavior['grandpy_status_code']}")
        chat_session.user_behavior['has_fatigue_quotas_of_grandpy'] = True
        print(f'Utilisateur fin: {chat_session.user_entry}')
        print(f'Réponse de Grandpy pre_fin: {response_grandpy}')
        print(f'Réponse de Grandpy fin: {display_grandpy_status_code_to_exhausted(chat_session)}')
        # has_fatigue_quotas_of_grandpy expire to 120 secondes (in theory 24h00)
        db_session.data_expiration('has_fatigue_quotas_of_grandpy')
    # Continue user queries
    elif following_billing:
        print(f"number incivility [display_behavior] = {chat_session.number_of_user_incivility}")
        chat_session.has_fatigue_quotas_of_grandpy = False
        display_behavior_user_request(chat_session, response_grandpy)
