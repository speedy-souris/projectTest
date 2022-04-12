#!/usr/bin/env python
"""main module"""
from conversation import Conversation
from redis_utilities import erasing_data
import counting_behaviour




# TODO create a behaviour incomprehension for the user
# TODO create the beginning of tiredness for grandpy

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

def main(user_request, db_number=0):
    """question answer between user and Grandpy"""
    # 6) DONE Create test_main.py module
    # 8) DONE correct query creation X1
    chat_session = conversation_between_user_and_grandpy(user_request, db_number=db_number)
    # if user_behavior['grandpy_status_code'] == 'home'
    grandpy_status = \
        chat_session.read_grandpy_answer(
            chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)])
    if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] == \
        chat_session.__class__.get_grandpy_status_key(0):
        print(f'1) Grandpy (home) main= {grandpy_status}')
        chat_session.calculate_the_incivility()
        print(f'7) Réponse de Grandpy = {grandpy_status}')
        print(f'8) status_code apres grandpy = '
              f'{chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)]}')
    # if user_behavior['grandpy_status_code'] == 'user_question'
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] == \
        chat_session.__class__.get_grandpy_status_key(1):
        if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(0)]:
            chat_session.calculate_the_incivility()
        else:
            chat_session.calculate_the_indecency()
    else:
        print('je suis number_user_entry = '
              f'{chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)]}')
        chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(8)] += 1
        counting_behaviour.user_question_answer_count(chat_session)
    #     if chat_session.__class__.read_grandpy_answer(
    #             chat_session.__class__.get_grandpy_status_key(7)
    #     )\
    #         == chat_session.__class__.get_grandpy_status_key(7):
    #         max_number_of_incivility(chat_session)
    #     else:
    #         # user_behavior['grandpy_status_code'] == 'user_question'
    #         chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] =\
    #             chat_session.__class__.get_grandpy_status_key(1)
    # # if user_behavior['grandpy_status_code'] == 'user_question'
    # elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] == \
    #     chat_session.__class__.get_grandpy_status_key(1):
    #     print(
    #             'user_incivility ='
    #             f' {chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(0)]}'
    #     )
    # question_answer(chat_session)

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
    erasing_data(1)
    main('bonjour', db_number=1)
    main('openclassroom', db_number=1)
    main('openclassroom', db_number=1)
    main('openclassroom', db_number=1)
    main('openclassroom', db_number=1)
    main('openclassroom', db_number=1)


