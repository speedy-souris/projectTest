"""module of counting of the behaviour of the user
     good behavior --> X10"""


def user_question_answer_count(chat_session):
    # DONE create a simple dialogue (a question, an answer)
    """grandpy receives the user politely, the user answers politely then he asks a question
     has grandpy. Grandpy answers him with one address of googleMap and a review of the quarter
    on Wikipedia"""
    # if grandpy_status_code == 'response'
    if chat_session.number_of_user_entries < 10:
        chat_session.number_of_user_entries += 1
        if chat_session.number_of_user_entries >= 10:
            chat_session.number_of_user_entries = 10

