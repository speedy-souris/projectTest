#!/usr/bin/env python
"""module of counting of the behaviour of the user """
from display_behaviour import display_grandpy_status_code_to_limit_incivility
from display_behaviour import display_grandpy_status_code_to_response, display_grandpy_status
from display_behaviour import display_grandpy_status_code_to_limit_indecency
from display_behaviour import display_grandpy_status_code_to_limit_incomprehension
from display_behaviour import display_grandpy_status_code_to_tired
from display_behaviour import display_grandpy_status_code_to_mannerless
from display_behaviour import display_grandpy_status_code_to_user_question
from display_behaviour import display_grandpy_status_code_to_disrespectful


def max_number_of_user_incomprehension(chat_session):
    # DONE max_incomprehension_counter
    """restoration of grandpy's status since a number of user incomprehension equal to 3"""
    chat_session.set_has_fatigue_quotas_of_grandpy(True)
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
    # if user_behavior['has_user_incivility_status'] = True
    if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(0)]:
        # user_behavior['grandpy_status_code'] = 'mannerless'
        display_grandpy_status_code_to_mannerless(chat_session)
        # if user_behavior['number_of_user_incivility'] < 3
        if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(5)] < 3:
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(5)] += 1
        # if user_behavior['number_of_user_incivility'] == 3
        elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(5)] >= 3:
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(5)] = 3
            # user_behavior['grandpy_status_code'] = 'incivility_limit'
            display_grandpy_status_code_to_limit_incivility(chat_session)
    # if user_behavior['has_user_incivility_status'] = False
    elif not chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(0)]:
        # user_behavior['grandpy_status_code'] = 'user_question'
        display_grandpy_status_code_to_user_question(chat_session)


# TODO create a behaviour of indecency for the user
def user_indecency_count(chat_session):
    """count of user's rudenness"""
    # user_behavior['has_user_indecency_status'] = True
    if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(1)]:
        # user_behavior['grandpy_status_code'] = 'disrespectful'
        display_grandpy_status_code_to_disrespectful(chat_session)
        # if user_behavior['number_of_user_indecency'] < 3
        if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(6)] < 3:
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(6)] += 1
        # if user_behavior['number_of_user_indecency'] == 3
        elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(6)] >= 3:
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(6)] = 3
            # user_behavior['grandpy_status_code'] = 'indecency_limit'
            display_grandpy_status_code_to_limit_indecency(chat_session)
    elif not chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(1)]:
        # user_behavior['grandpy_status_code'] = 'user_question'
        display_grandpy_status_code_to_user_question(chat_session)


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
    counting = ""
    # if user_behavior['number_of_user_entries'] == 1 à 4
    if 1 <= chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] <= 4:
        counting = True
        number_of_user_entries_X1_to_X4(chat_session)
    # if user_behavior['number_of_number_of_user_entries'] == 5
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] == 5:
        counting = True
        number_of_user_entries_to_X5(chat_session)
    elif 6 <= chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] <= 9:
        counting = True
        number_of_user_entries_X6_to_X9(chat_session)
    # if user_behavior['number_of_number_of_user_entries'] == 10
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] == 10:
        counting = False
        max_number_of_user_entries(chat_session)
    return counting

