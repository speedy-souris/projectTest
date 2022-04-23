#!/usr/bin/env python
"""main module"""
from conversation import Conversation
# from redis_utilities import erasing_data
from counting_behaviour import user_question_answer_count
from display_behaviour import display_grandpy_status_code_to_home
from display_behaviour import display_grandpy_status_code_to_benevolent


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
    gmap_api_placeId_value = chat_session.get_placeid_from_address(user_request_parsed)
    print(f"placeid value = {gmap_api_placeId_value}")
    gmap_api_address_value = chat_session.get_address_api_from_placeid(gmap_api_placeId_value)
    return gmap_api_address_value


# 5) TODO management of the call to the WikiPedia API
def search_address_to_wiki():
    # DONE WIKIPEDIA API calling
    """call of the WikiPedia APIs according to the user's request"""
# ---------------------------


def user_presentation_management(chat_session):
    """management of the presentation of the user"""
    # if user_behavior['grandpy_status_code'] = 'home'
    if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] ==\
            chat_session.__class__.get_grandpy_status_key(0):
        display_grandpy_status_code_to_home(chat_session)
        chat_session.calculate_the_incivility()
        chat_session.calculate_the_indecency()
        chat_session.calculate_the_incomprehension()
    # if user_behavior['grandpy_status_code'] = 'mannerless'
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] ==\
            chat_session.__class__.get_grandpy_status_key(5):
        chat_session.calculate_the_incivility()
    # if user_behavior['grandpy_status_code'] = 'disrespectful'
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] ==\
            chat_session.__class__.get_grandpy_status_key(6):
        chat_session.calculate_the_indecency()
    # if user_behavior['grandpy_status_code'] = 'incomprehension'
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] ==\
            chat_session.__class__.get_grandpy_status_key(4):
        chat_session.calculate_the_incomprehension()
    else:
        display_grandpy_status_code_to_benevolent(chat_session)


def main(user_request, db_number=0):
    """question answer between user and Grandpy"""
    # 6) DONE Create test_main.py module
    # 8) DONE correct query creation X1
    chat_session = conversation_between_user_and_grandpy(user_request, db_number=db_number)
    # if user_behavior['grandpy_status_code'] = 'home'
    if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(0)] == 0:
        user_presentation_management(chat_session)
        if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] == \
                chat_session.__class__.get_grandpy_status_key(1):
            chat_session.calculate_the_indecency()
            user_question_answer_count(chat_session)
    elif chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key(4)] != 'benevolent':
        if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] == 0:
            user_presentation_management(chat_session)
    # if user_behavior['grandpy_status_code'] = 'benevolent'
    # elif chat_session.user_behavior[chat_session.get_user_behavior_key(4)] ==\
    #         chat_session.get_grandpy_status_key(1):
    #     chat_session.calculate_the_indecency()
    #     print('je suis ici')

    # TODO create the beginning of tiredness for grandpy
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
