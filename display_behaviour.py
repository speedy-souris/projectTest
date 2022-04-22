#!/usr/bin/env python
"""module of pisplay of the behaviour of the user """
from redis_utilities import data_expiration


def display_grandpy_status_code_to_home(chat_session):
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
        chat_session.__class__.get_grandpy_status_key(0)
    grandpy_status = chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]
    grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_benevolent(chat_session):
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
        chat_session.__class__.get_grandpy_status_key(1)
    grandpy_status = chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]
    grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
    display_grandpy_status(chat_session, grandpy_response)


# def display_grandpy_status_code_to_user_question(chat_session):
#     chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
#         chat_session.__class__.get_grandpy_status_key(2)
#     grandpy_status = chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]
#     grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
#     return grandpy_response


def display_grandpy_status_code_to_response(chat_session):
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
        chat_session.__class__.get_grandpy_status_key(2)
    grandpy_status = chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]
    grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_tired(chat_session):
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
        chat_session.__class__.get_grandpy_status_key(3)
    grandpy_status = chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]
    grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_incomprehension(chat_session):
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
        chat_session.__class__.get_grandpy_status_key(4)
    print('incomprehension (display) = '
          f'{chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(2)]}')
    grandpy_status = chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]
    grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_mannerless(chat_session):
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
        chat_session.__class__.get_grandpy_status_key(5)
    grandpy_status = chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]
    grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_disrespectful(chat_session):
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
        chat_session.__class__.get_grandpy_status_key(6)
    grandpy_status = chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]
    grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
    display_grandpy_status(chat_session, grandpy_response)


def display_grandpy_status_code_to_limit_incivility(chat_session):
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
        chat_session.__class__.get_grandpy_status_key(7)
    grandpy_status = chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]
    grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
    display_grandpy_status(chat_session, grandpy_response, following_billing=False)


def display_grandpy_status_code_to_limit_indecency(chat_session):
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
        chat_session.__class__.get_grandpy_status_key(8)
    grandpy_status = chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]
    grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
    display_grandpy_status(chat_session, grandpy_response, following_billing=False)


def display_grandpy_status_code_to_limit_incomprehension(chat_session):
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
        chat_session.__class__.get_grandpy_status_key(9)
    grandpy_status = chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]
    grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
    display_grandpy_status(chat_session, grandpy_response, following_billing=False)


def display_grandpy_status_code_to_exhausted(chat_session):
    # chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
    #     chat_session.__class__.get_grandpy_status_key(10)
    grandpy_status = chat_session.__class__.get_grandpy_status_key(10)
    grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
    return grandpy_response


def display_correct_user_request_1_to_X9(chat_session, response_grandpy):
    # user_behavior['number_of_user_entries'] == 1 to 4
    if 1 <= chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] <= 4:
        print(f' Utilisateur : {chat_session.user_entry}')
        print(f' Réponse de Grandpy (1-4): {response_grandpy}')
    # if user_behavior['number_of_user_entries'] == 5
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] == 5:
        print(f'Utilisateur : {chat_session.user_entry}')
        print(f'Réponse de Grandpy (5): {response_grandpy}')
        # user_behavior['grandpy_status_code']= 'response'
        print('Réponse de Grandpy (5) : '
              f'{display_grandpy_status_code_to_response(chat_session)}')
    # if user_behavior['number_of_entries'] == 6 to 9
    elif 6 <= chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] <= 9:
        # user_behavior['grandpy_status_code']= 'response'
        print(f'Utilisateur : {chat_session.user_entry}')
        print('Réponse de Grandpy (6-9) : '
              f'{display_grandpy_status_code_to_response(chat_session)}')


def Display_last_user_request(chat_session, response_grandpy):
    """display of the last user's request before a 24 hours break"""
    print(f'Utilisateur : {chat_session.user_entry}')
    print(f'Réponse de Grandpy : {response_grandpy}')
    print(f'Réponse de Grandpy : {display_grandpy_status_code_to_exhausted(chat_session)}')
    # has_fatigue_quotas_of_grandpy expire to 120 secondes (in theory 24h00)
    data_expiration(chat_session.__class__.get_user_behavior_key(3), chat_session.db_number)


def display_behaviour_user_request(chat_session, response_grandpy):
    """display of the user's understanding"""
    # if user_behavior['number_of_user_entries'] == 1 to 9
    if 1 <= chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] <= 9:
        display_correct_user_request_1_to_X9(chat_session, response_grandpy)
    # if user_behavior['has_user_indecency_status'] == True
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(1)]:
        print(f'Utilisateur 2 : {chat_session.user_entry}')
        print(f'Réponse de grandpy (indecency): {response_grandpy}')
    # if user_behavior['has_user_incomprehension_status'] == True
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(2)]:
        print(f'Utilisateur 3 : {chat_session.user_entry}')
        print(f'Réponse de grandpy (incomprehension): {response_grandpy}')
    # if user_behavior['has_user_incivility_status'] == True
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(0)]:
        print(f'Utilisateur 1: {chat_session.user_entry}')
        print(f'Réponse de Grandpy (incivility): {response_grandpy}')
    # if user_behavior['grandpy_status_code'] == 'benevolent'
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] == \
            chat_session.__class__.get_grandpy_status_key(1):
        print(f'Utilisateur : {chat_session.user_entry}')
        print(f'Réponse de Grandpy (benevolent): {response_grandpy}')
    # print("Réponse de grandpy (question) = "
    #       f"{display_grandpy_status_code_to_user_question(chat_session)}")


def display_grandpy_status(chat_session, response_grandpy, following_billing=True):
    """billing of status of grandpy just before its repose of 24 h 00"""
    # Termination of user requests (for 24H00)
    if not following_billing:
        chat_session.set_has_fatigue_quotas_of_grandpy(True)
        print("user_behavior['has_fatigue_quotas_of_grandpy'] display_status = "
              f"{chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(3)]}")
        Display_last_user_request(chat_session, response_grandpy)
    # Continue user queries
    elif following_billing:
        chat_session.set_has_fatigue_quotas_of_grandpy(False)
        display_behaviour_user_request(chat_session, response_grandpy)

        # else:
        #     # user_behavior['grandpy_status_code']= 'home'
        #     print(f'Accueil de Grandpy (home): {response_grandpy}')
        #     # if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] == \
        #     #         chat_session.__class__.get_grandpy_status_key(0):
        #     #     # print(f'Utilisateur 1 : {chat_session.user_entry}')
        #     #     pass
