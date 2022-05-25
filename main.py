#!/usr/bin/env python3
"""main module"""
from . import Conversation
from . import display_grandpy_status_code_to_home
from . import user_incivility_count
from . import user_indecency_count
from . import user_incomprehension_count
# from . import user_question_answer_count
# from . import display_grandpy_status_code_to_response
# from . import display_grandpy_status_code_to_benevolent


def conversation_between_user_and_grandpy(user_request, db_number):
    # DONE conversation object
    """creation of the chat_session conversation object according to the user's request"""
    chat_session = Conversation(user_request, db_number)
    return chat_session


# ---------------------------
# 4) DONE management of the call to the GoogleMap API
def search_address_to_gMap(chat_session, user_request_parsed):
    # DONE GoogleMap API calling
    """call of the GoogleMap APIs according to the user's request"""
    gmap_api_placeid_value = chat_session.get_placeid_from_address(user_request_parsed)
    print(f"placeid value = {gmap_api_placeid_value}")
    gmap_api_address_value = chat_session.get_address_api_from_placeid(gmap_api_placeid_value)
    return gmap_api_address_value


# 5) TODO management of the call to the WikiPedia API
def search_address_to_wiki():
    # DONE WIKIPEDIA API calling
    """call of the WikiPedia APIs according to the user's request"""
    pass


# ---------------------------
def user_presentation_management(chat_session):
    """management of the presentation of the user"""
    display_grandpy_status_code_to_home(chat_session)
    chat_session.calculate_the_incivility_status()
    user_incivility_count(chat_session)
    chat_session.calculate_the_indecency_status()
    user_indecency_count(chat_session)
    chat_session.calculate_the_incomprehension_status()
    user_incomprehension_count(chat_session)
    # if user_behavior['grandpy_status_code'] = 'mannerless'
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('mannerless'):
        user_presentation_management(chat_session)
    # if user_behavior['grandpy_status_code'] = 'disrespectful'
    elif chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('disrespectful'):
        user_presentation_management(chat_session)
    # if user_behavior['grandpy_status_code'] = 'incomprehension'
    elif chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('incomprehension'):
        user_presentation_management(chat_session)
    else:
        print("status benevolent (main) avant = "
              f"{chat_session.user_behavior['grandpy_status_code']}")
        chat_session.user_behavior['grandpy_status_code']\
            = chat_session.__class__.get_grandpy_status_key('benevolent')
        print("status benevolent (main) apres = "
              f"{chat_session.user_behavior['grandpy_status_code']}")


def main(user_request, db_number=0):
    """question answer between user and Grandpy"""
    # 6) DONE Create test_main.py module
    # 8) DONE correct query creation X1
    chat_session = conversation_between_user_and_grandpy(user_request, db_number=db_number)
    # if user_behavior['grandpy_status_code'] = 'home'
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('home'):
        user_presentation_management(chat_session)

    # elif chat_session.user_behavior[
    #         chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
    #         == chat_session.__class__.get_grandpy_status_key('benevolent'):
    #     display_grandpy_status_code_to_benevolent(chat_session)
    #     user_presentation_management(chat_session)
    # if user_behavior['number_of_user_entries'] = 1 to 4
    # elif 1 <= chat_session.user_behavior[
    #         chat_session.__class__.get_user_behavior_key('nb_entries')] <= 10:
    #     chat_session.get_request_parser()
    #     user_question_answer_count(chat_session)
    #     chat_session.calculate_the_indecency()
    #     user_question_answer_count(chat_session)
    # elif chat_session.user_behavior[
    #         chat_session.__class__.get_user_behavior_key(4)] != 'benevolent':
    #     if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] == 0:
    #         user_presentation_management(chat_session)
    # if user_behavior['grandpy_status_code'] = 'benevolent'
    # elif chat_session.user_behavior[chat_session.get_user_behavior_key(4)] ==\
    #         chat_session.get_grandpy_status_key(1):
    #     chat_session.calculate_the_indecency()
    #     print('je suis ici')

    # TODO create the beginning of tired for grandpy
    # 10) TODO correct query creation X10
    # 12) TODO incivility query creation X1
    # 14) TODO incivility query creation X3
    # 16) TODO indecency query creation X1
    # 18) TODO indecency query creation X3
    # 20) TODO incomprehension query creation X1
    # 22) TODO incomprehension query creation X3
    # 24) TODO Add incivility conditional statements
    # 26) TODO Add indecency conditional statements
    # 28) TODO Add incomprehension conditional statements
    chat_session.update_database()
    return chat_session


if __name__ == '__main__':
    pass
