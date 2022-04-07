#!/usr/bin/env python
"""module of counting of the behaviour of the user """


def display_grandpy_status(
        chat_session, status_found, data_expiration, db_number, following_billing=1
):
    """billing of status of grandpy just before its repose of 24 h 00"""
    if following_billing == 1:
        chat_session.has_fatigue_quotas_of_grandpy(True)
        print(
            'Réponse de Grandpy : '
            f'{chat_session.__class__.read_grandpy_answer(status_found)}'
        )
        grandpy_exhausted_for_24_hours = chat_session.__class__.get_grandpy_status_key(10)
        print(
            'Réponse de Grandpy : '
            f'{chat_session.__class__.read_grandpy_answer(grandpy_exhausted_for_24_hours)}'
        )
    elif following_billing != 1:
        chat_session.has_fatigue_quotas_of_grandpy(False)
        print(
            'Réponse de Grandpy : '
            f'{chat_session.__class__.read_grandpy_answer(status_found)}'
        )
    # fatigue_quotas_of_grandpy expire dans 120 secondes (en théorie 24h00)
    fatigue_quotas_of_grandpy = \
        chat_session.user_behavior[chat_session.__class__.get_grandpy_status_key(3)]
    data_expiration(fatigue_quotas_of_grandpy, db_number)


# 3) DONE create max_number_of_incivility
def max_number_of_incivility(chat_session, data_expiration, db_number):
    # DONE max_incivlity counter
    """restoration of grandpy's status since a number of user incivility equal to 3"""
    incivility_limit_found = chat_session.__class__.get_grandpy_status_key(7)
    chat_session.has_user_incivility_status(True)
    display_grandpy_status(chat_session, incivility_limit_found, data_expiration, db_number)


def max_number_of_indecency(chat_session, data_expiration, db_number):
    # DONE max_indecency counter
    """restoration of grandpy's status since a number of user indecency equal to 3"""
    indecency_limit_found = chat_session.__class__.get_grandpy_status_key(8)
    chat_session.has_user_indecency_status(True)
    display_grandpy_status(chat_session, indecency_limit_found, data_expiration, db_number)


def max_number_of_incomprehension(chat_session, data_expiration, db_number):
    # DONE max_indecency counter
    """restoration of grandpy's status since a number of user incomprehension equal to 3"""
    incomprehension_limit_found = chat_session.__class__.get_grandpy_status_key(9)
    chat_session.has_user_incomprehension_status(True)
    display_grandpy_status(chat_session, incomprehension_limit_found, data_expiration, db_number)


def number_of_user_entries_to_X5(chat_session):
    # DONE user_entries X5
    """restore grandpy status from correct user request count of 5"""
    tired_limit_found = chat_session.__class__.get_grandpy_status_key(3)
    # grandpy_status_code takes the tired value
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
        chat_session.__class__.get_grandpy_status_key(3)
    # number_of_user_entries incremente of 1
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] += 1
    display_grandpy_status(chat_session, tired_limit_found, following_billing=0)


def user_incivility_count(chat_session, data_expiration, db_number):
    """discount of user's discourtesy"""
    # has_user_incivility_status
    if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(0)]:
        # number_of_user_incivility
        if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(5)] < 3:
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(5)] += 1
            # grandpy_status_code == 'mannerless'
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] = \
                chat_session.__class__.read_grandpy_answer(5)
        elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(5)] >= 3:
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(5)] = 3
            max_number_of_incivility(chat_session, data_expiration, db_number)
    elif not chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(0)]:
        # grandpy_status_code == 'user_question'
        chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] =\
            chat_session.__class__.get_grandpy_status_key(1)


def user_indecency_count(chat_session, data_expiration, db_number):
    """count of user's rudenness"""
    # has_user_indecency_status
    if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(1)]:
        # number_of_user_indecency
        if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(6)] < 3:
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(6)] += 1
        elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(6)] >= 3:
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(6)] = 3
            max_number_of_indecency(chat_session, data_expiration, db_number)
    else:
        # grandpy_status_code == 'user_question'
        chat_session.user_behavior[chat_session.get_user_behavior_key(4)] = \
            chat_session.__class__.get_grandpy_status_key(1)


def user_incomprehension_count(chat_session, data_expiration, db_number):
    """discount of user's incomprehension"""
    # has_user_incomprehension_status
    if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(2)]:
        # number_of_user_incivility
        if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(7)] < 3:
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(7)] += 1
        elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(7)] >= 3:
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(7)] = 3
            max_number_of_incomprehension(chat_session, data_expiration, db_number)
    else:
        # grandpy_status_code == 'user_question'
        chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] =\
            chat_session.__class__.get_grandpy_status_key(1)


def user_question_answer_count(chat_session, db_number):
    # TODO create a simple dialogue (a question, an answer)
    """grandpy receives the user politely, the user answers politely then he asks a question
     has grandpy. Grandpy answers him with one address of googleMap and a review of the quarter
    on Wikipedia"""
    print(
        'grandpy status counting ='
        f" {chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]}"
    )
    print(
        'number_of_ user entries counting ='
        f" {chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)]}"
    )

