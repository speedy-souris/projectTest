#!/usr/bin/env python
"""module of counting of the behaviour of the user """
from redis_utilities import data_expiration


def display_grandpy_status_code_to_user_question(chat_session):
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
        chat_session.__class__.get_grandpy_status_key(1)
    grandpy_status = chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]
    user_question = chat_session.__class__.read_grandpy_answer(grandpy_status)
    return user_question


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
    grandpy_status = chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]
    grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
    return grandpy_response


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
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
        chat_session.__class__.get_grandpy_status_key(10)
    grandpy_status = chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]
    grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
    return grandpy_response


def display_grandpy_status(chat_session, response_grandpy, following_billing=True):
    """billing of status of grandpy just before its repose of 24 h 00"""
    if not following_billing:
        chat_session.set_has_fatigue_quotas_of_grandpy(True)
        print(f'Utilisateur : {chat_session.user_entry}')
        print(f'Réponse de Grandpy : {response_grandpy}')
        print(f'Réponse de Grandpy : {display_grandpy_status_code_to_exhausted(chat_session)}')
        # fatigue_quotas_of_grandpy expire to 120 secondes (in theory 24h00)
        fatigue_quotas_of_grandpy = chat_session.__class__.get_user_behavior_key(3)
        data_expiration(fatigue_quotas_of_grandpy, chat_session.db_number)
    elif following_billing:
        chat_session.set_has_fatigue_quotas_of_grandpy(False)
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
        elif 6 <= chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] <= 9:
            # user_behavior['grandpy_status_code']= 'response'
            print(f'Utilisateur : {chat_session.user_entry}')
            print('Réponse de Grandpy (6-9) : '
                  f'{display_grandpy_status_code_to_response(chat_session)}')
        else:
            if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(0)]:
                print(f'3) Utilisateur : {chat_session.user_entry}')
                print(f'4) Réponse de Grandpy (incivility): {response_grandpy}')
        #     elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(2)]:
        #         print('Réponse de grandpy (indecency): '
        #               f'{display_grandpy_status_code_to_incomprehension(chat_session)}')
        # user_behavior['grandpy_status_code']= 'user_question'
        print('5) Réponse de Grandpy (fin) : '
              f'{display_grandpy_status_code_to_user_question(chat_session)}')


# 3) DONE create max_number_of_incivility
def max_number_of_user_incivility(chat_session):
    # DONE max_incivlity counter
    """restoration of grandpy's status since a number of user incivility equal to 3"""
    chat_session.set_has_user_incivility_status(True)
    display_grandpy_status_code_to_limit_incivility(chat_session)


def max_number_of_user_indecency(chat_session):
    # DONE max_indecency counter
    """restoration of grandpy's status since a number of user indecency equal to 3"""
    chat_session.has_user_indecency_status(True)
    display_grandpy_status_code_to_limit_indecency(chat_session)


def max_number_of_user_incomprehension(chat_session):
    # DONE max_incomprehension_counter
    """restoration of grandpy's status since a number of user incomprehension equal to 3"""
    chat_session.has_user_incomprehension_status(True)
    display_grandpy_status_code_to_limit_incomprehension(chat_session)


def number_of_user_entries_X1_to_X4(chat_session):
    """restore the grandpy status from correct user request between 1 and 4"""
    # if user_behavior[' number_of_user_entries'] == 1 to 4
    if 1 <= chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] <= 4:
        # user_behavior['grandpy_status_code'] = 'response'
        display_grandpy_status_code_to_response(chat_session)


def number_of_user_entries_to_X5(chat_session):
    # DONE user_entries X5
    """restore grandpy status from correct user request count of 5"""
    # user_behavior['grandpy_status_code'] = 'tired'
    display_grandpy_status_code_to_tired(chat_session)


def number_of_user_entries_X6_to_X9(chat_session):
    """restore the grandpy status from correct user request between 6 and 9"""
    # if user_behavior[' number_of_user_entries'] == 6 to 9
    if 6 <= chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] <= 9:
        # user_behavior['grandpy_status_code'] = 'response'
        display_grandpy_status_code_to_response(chat_session)


def max_number_of_user_entries(chat_session):
    # DONE max_user_entries counter
    """restoration of grandpy's status
    since a maximum number of correct requests from the user equal to 10"""
    # user_behavior['grandpy_status_code'] = 'response'
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
        chat_session.__class__.get_grandpy_status_key(2)
    grandpy_status = chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]
    grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
    display_grandpy_status(chat_session, grandpy_response, following_billing=False)


# DONE create a behaviour of discourtesy for the user
def user_incivility_count(chat_session):
    """discount of user's discourtesy"""
    print('2) user_incivility_status count = '
          f'{chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(0)]}')
    # has_user_incivility_status
    if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(0)]:
        # grandpy_status_code == 'mannerless'
        display_grandpy_status_code_to_mannerless(chat_session)
        # number_of_user_incivility
        if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(5)] < 3:
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(5)] += 1
        elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(5)] >= 3:
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(5)] = 3
            max_number_of_user_incivility(chat_session)
    elif not chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(0)]:
        # grandpy_status_code == 'user_question'
        chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] =\
            chat_session.__class__.get_grandpy_status_key(1)
    print('6) number_incivility count = '
          f'{chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(5)]}')


# TODO create a behaviour of indecency for the user
def user_indecency_count(chat_session):
    """count of user's rudenness"""
    # has_user_indecency_status
    if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(1)]:
        # grandpy_code_status_code == 'disrespectful'
        display_grandpy_status_code_to_disrespectful(chat_session)
        # number_of_user_indecency
        if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(6)] < 3:
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(6)] += 1
        elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(6)] >= 3:
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(6)] = 3
            max_number_of_user_indecency(chat_session)
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(1)]:
        # grandpy_status_code == 'user_question'
        chat_session.user_behavior[chat_session.get_user_behavior_key(4)] = \
            chat_session.__class__.get_grandpy_status_key(1)


def user_incomprehension_count(chat_session):
    """discount of user's incomprehension"""
    # has_user_incomprehension_status
    if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(2)]:
        # number_of_user_incivility
        if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(7)] < 3:
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(7)] += 1
        elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(7)] >= 3:
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(7)] = 3
            max_number_of_user_incomprehension(chat_session)
    else:
        # grandpy_status_code == 'user_question'
        chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] =\
            chat_session.__class__.get_grandpy_status_key(1)


def user_question_answer_count(chat_session):
    # DONE create a simple dialogue (a question, an answer)
    """grandpy receives the user politely, the user answers politely then he asks a question
     has grandpy. Grandpy answers him with one address of googleMap and a review of the quarter
    on Wikipedia"""
    if 1 <= chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] <= 4:
        number_of_user_entries_X1_to_X4(chat_session)
    # if user_behavior['number_of_number_of_user_entries'] == 5
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] == 5:
        number_of_user_entries_to_X5(chat_session)
    elif 6 <= chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] <= 9:
        number_of_user_entries_X6_to_X9(chat_session)
    # if user_behavior['number_of_number_of_user_entries'] == 10
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] == 10:
        max_number_of_user_entries(chat_session)

