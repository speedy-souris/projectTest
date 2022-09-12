"""module of counting of the behaviour of the user """
from . import display_behavior


def max_number_of_user_entries(chat_session):
    # DONE max_user_entries counter
    """restoration of grandpy's status
    since a maximum number of correct requests from the user equal to 10"""
    # user_behavior['grandpy_status_code'] = 'response'
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
        = chat_session.__class__.get_grandpy_status_key('response_limit')
    grandpy_status = chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('grandpy_status_code')]
    grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
    display_behavior.display_grandpy_status(
        chat_session, grandpy_response, following_billing=False)


# DONE create a behaviour of discourtesy for the user
def user_incivility_count(chat_session):
    """discount of user's discourtesy - counting up to 3 user incivilities"""
    # if grandpy_status_code = 'mannerless'
    if chat_session.grandpy_status_code == 'mannerless':
        if chat_session.number_of_user_incivility >= 3:
            chat_session.number_of_user_incivility = 3
            display_behavior.display_grandpy_status_code_to_incivility_limit(chat_session)
        print(f"number incivility [incivility count] = {chat_session.number_of_user_incivility}")


# DONE create a behaviour of indecency for the user
def user_indecency_count(chat_session):
    """count of user's rudeness in level 1 (presentation) / level 2 (chat_session)
     counting up to 3 of user indecencies"""
    # if user_behavior['grandpy_status_code'] == 'disrespectful'
    if chat_session.user_behavior['grandpy_status_code'] == 'disrespectful':
        if chat_session.user_behavior['number_of_user_indecency'] >= 3:
            chat_session.user_behavior['number_of_user_indecency'] = 3
            display_behavior.display_grandpy_status_code_to_indecency_limit(chat_session)


def user_incomprehension_count(chat_session):
    """discount of user's incomprehension in level 1 (presentation) / level 2 (chat_session)
    counting up to 3 of user indecencies"""
    # if user_behavior['grandpy_status_code'] == 'incomprehension'
    if chat_session.user_behavior['grandpy_status_code'] == 'incomprehension':
        if chat_session.user_behavior['number_of_user_incomprehension'] >= 3:
            chat_session.user_behavior['number_of_user_incomprehension'] = 3
            # user_behavior['grandpy_status_code'] = 'incomprehension_limit'
            display_behavior.display_grandpy_status_code_to_incomprehension_limit(chat_session)


def user_question_answer_count(chat_session):
    # DONE create a simple dialogue (a question, an answer)
    """grandpy receives the user politely, the user answers politely then he asks a question
     has grandpy. Grandpy answers him with one address of googleMap and a review of the quarter
    on Wikipedia"""
    user_request_increment_data = True
    # if user_behavior['grandpy_status_code'] == 'benevolent'
    # ==> user_behavior['grandpy_status_code'] == 'response'
    if chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('benevolent'):
        display_behavior.display_grandpy_status_code_to_response(chat_session)
        chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('number_of_user_entries')] = 1
        user_request_increment_data = False
    # if user_behavior['grandpy_status_code'] = 'response'
    elif chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('response'):
        # if user_behavior['number_of_number_of_user_entries'] == 5
        if chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('number_of_user_entries')] == 5:
            # user_behavior['grandpy_status_code'] = 'tired'
            display_behavior.display_grandpy_status_code_to_tired(chat_session)
            display_behavior.display_grandpy_status_code_to_response(chat_session)
        # if user_behavior['number_of_number_of_user_entries'] == 10
        elif chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('number_of_user_entries')] >= 10:
            chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('number_of_user_entries')] = 10
            max_number_of_user_entries(chat_session)
            user_request_increment_data = False

    if user_request_increment_data:
        chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('number_of_user_entries')] += 1
