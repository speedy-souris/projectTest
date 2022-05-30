"""module of counting of the behaviour of the user """
from . import display_behaviour


def max_number_of_user_entries(chat_session):
    # DONE max_user_entries counter
    """restoration of grandpy's status
    since a maximum number of correct requests from the user equal to 10"""
    # user_behavior['grandpy_status_code'] = 'response'
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('status')] = \
        chat_session.__class__.get_grandpy_status_key('discomfort')
    grandpy_status = chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('status')]
    grandpy_response = chat_session.__class__.read_grandpy_answer(grandpy_status)
    display_behaviour.display_grandpy_status(
        chat_session, grandpy_response, following_billing=False)


# DONE create a behaviour of discourtesy for the user
def user_incivility_count(chat_session):
    """discount of user's discourtesy - counting up to 3 user incivilities"""
    # user_behavior['grandpy_status_code'] = 'mannerless'
    display_behaviour.display_grandpy_status_code_to_mannerless(chat_session)
    # if user_behavior['number_of_user_incivility'] = 1 to 2
    if 0 <= chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('number_of_user_incivility')] <= 2:
        chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('number_of_user_incivility')] += 1
    # if user_behavior['number_of_user_incivility'] == 3
    elif chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('number_of_user_incivility')] >= 3:
        chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('number_of_user_incivility')] = 3
        # user_behavior['grandpy_status_code'] = 'incivility_limit'
        display_behaviour.display_grandpy_status_code_to_incivility_limit(chat_session)


# DONE create a behaviour of indecency for the user
def user_indecency_count(chat_session, level, behavior_level):
    """count of user's rudeness in presentation / chat_session counting up to 3 of user indecencies
    example : if arg level == 'presentation' then number_of_user_incivility is used
    else if arg level == 'chat_session' then it is number_of_user_incivility2 which is used"""
    chat_session.level_status(level, behavior_level, True)
    number_of_user_indecency = chat_session.level_user_name(level, behavior_level)
    display_behaviour.display_grandpy_status_code_to_disrespectful(chat_session)
    # if user_behavior['number_of_user_indecency' / 'number_of_user_indecency2'] 1 to 2
    if 0 <= chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key(number_of_user_indecency)] <= 2:
        chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key(number_of_user_indecency)] += 1
    # if user_behavior['number_of_user_indecency' / 'number_of_user_indecency2'] == 3
    elif chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key(number_of_user_indecency)] >= 3:
        chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key(number_of_user_indecency)] = 3
        # user_behavior['grandpy_status_code'] = 'indecency_limit'
        display_behaviour.display_grandpy_status_code_to_indecency_limit(chat_session)


def user_incomprehension_count(chat_session, level, behavior_level):
    """discount of user's incomprehension in presentation / chat_session
    example : if arg level == 'presentation' then number_of_user_incomprehension is used
    else if arg level == 'chat_session' then it is number_of_user_incomprehension2 which is used"""
    chat_session.level_status(level, behavior_level, True)
    number_of_user_incomprehension = chat_session.level_user_name(level, behavior_level)
    display_behaviour.display_grandpy_status_code_to_incomprehension(chat_session)
    # user_behavior['number_of_user_incomprehension' / 'number_of_user_incomprehension2'] = 1 to 2
    if 0 <= chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key(number_of_user_incomprehension)] < 3:
        chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key(number_of_user_incomprehension)] += 1
    # user_behavior['number_of_user_incomprehension' / 'number_of_user_incomprehension2'] == 3
    elif chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key(number_of_user_incomprehension)] >= 3:
        chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key(number_of_user_incomprehension)] = 3
        # user_behavior['grandpy_status_code'] = 'incomprehension_limit'
        display_behaviour.display_grandpy_status_code_to_incomprehension_limit(chat_session)


def user_question_answer_count(chat_session):
    # DONE create a simple dialogue (a question, an answer)
    """grandpy receives the user politely, the user answers politely then he asks a question
     has grandpy. Grandpy answers him with one address of googleMap and a review of the quarter
    on Wikipedia"""
    user_request_increment_data = True
    if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('status')]\
            == chat_session.__class__.get_grandpy_status_key('benevolent'):
        display_behaviour.display_grandpy_status_code_to_response(chat_session)
    if 1 <= chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('nb_entries')] <= 4:
        display_behaviour.display_grandpy_status_code_to_response(chat_session)
    # if user_behavior['number_of_number_of_user_entries'] == 5
    elif chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('nb_entries')] == 5:
        # user_behavior['grandpy_status_code'] = 'tired'
        display_behaviour.display_grandpy_status_code_to_tired(chat_session)
    # if user_behavior['number_of_number_of_user_entries'] == 10
    elif chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('nb_entries')] == 10:
        max_number_of_user_entries(chat_session)
        user_request_increment_data = False
    # if user_behavior['grandpy_status_code'] = 'response'
    # ==> if user_request_increment_data = user_behavior['number_of_number_of_user_entries'] += 1
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('status')]\
            == chat_session.__class__.get_grandpy_status_key('benevolent'):
        if user_request_increment_data:
            chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('nb_entries')] += 1
