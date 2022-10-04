"""module of counting of the behaviour of the user
bad behavior (incivility, indecency, incomprehension) --> X3 ... good behavior --> X10"""


# DONE create a behaviour of discourtesy for the user
def user_incivility_count(chat_session):
    """discount of user's discourtesy - counting up to 3 user incivilities"""
    # if grandpy_status_code = 'mannerless'
    if chat_session.grandpy_status_code == 'mannerless':
        if chat_session.number_of_user_incivility >= 3:
            chat_session.number_of_user_incivility = 3
        else:
            chat_session.number_of_user_incivility += 1


# DONE create a behaviour of indecency for the user
def user_indecency_count(chat_session):
    """count of user's rudeness in level 1 (presentation) / level 2 (chat_session)
    counting up to 3 of user indecencies"""
    # if grandpy_status_code = 'disrespectful'
    if chat_session.grandpy_status_code == 'disrespectful':
        if chat_session.number_of_user_indecency >= 3:
            chat_session.number_of_user_indecency = 3
        else:
            chat_session.number_of_user_indecency += 1


def user_incomprehension_count(chat_session):
    """discount of user's incomprehension in level 1 (presentation) / level 2 (chat_session)
    counting up to 3 of user indecencies"""
    # if grandpy_status_code == 'incomprehension'
    if chat_session.grandpy_status_code == 'incomprehension':
        if chat_session.number_of_user_incomprehension >= 3:
            chat_session.number_of_user_incomprehension = 3
        else:
            chat_session.number_of_user_incomprehension += 1


def user_question_answer_count(chat_session):
    # DONE create a simple dialogue (a question, an answer)
    """grandpy receives the user politely, the user answers politely then he asks a question
     has grandpy. Grandpy answers him with one address of googleMap and a review of the quarter
    on Wikipedia"""
    # if grandpy_status_code == 'incomprehension'
    if chat_session.grandpy_status_code == 'benevolent':
        if chat_session.number_of_user_entries >= 10:
            chat_session.number_of_user_entries = 10
        else:
            chat_session.number_of_user_entries += 1
