#!/usr/bin/env python3
"""main module"""
from src.session.conversation import Conversation
# from src import display_behavior
from src.display import counting_behavior
from src.redis_utilities import read_access_conversation_data, get_database_access
from src.redis_utilities import write_access_conversation_data, erasing_data
from src.redis_utilities import byte_to_boolean_conversion, byte_to_int_conversion
from src.redis_utilities import value_to_string_conversion, scan_database_redis
# from . import user_question_answer_count
# from . import display_grandpy_status_code_to_response


def initialization_database_redis(db_session):
    """initialization of the redis database with the default attribute values"""
    list_attribut_names = (
        'level', 'has_user_incivility_status', 'number_of_user_incivility',
        'has_user_indecency_status', 'number_of_user_indecency', 'has_user_incomprehension_status',
        'number_of_user_incomprehension', 'number_of_user_entries', 'has_fatigue_quotas_of_grandpy',
        'grandpy_status_code')
    #TODO create db_number for avoid hard-coded
    chat_session = Conversation('', 1)
    erasing_data(db_session)
    for names in list_attribut_names:
        print(f'initialization redis [main] = name --> {names}')
        write_access_conversation_data(names, chat_session, db_session)
        print("affichage data redis [main] "
              f"{read_access_conversation_data(names, db_session)}")


def conversation_between_user_and_grandpy(user_request, db_session, db_number):
    # DONE conversation object
    """creation of the chat_session conversation object according to the user's request"""
    print('avant la condition [main]')
    if not scan_database_redis(db_session):
        initialization_database_redis(db_session)
    args = {
        'level':
            read_access_conversation_data('level', db_session),
        'has_user_incivility_status':
            read_access_conversation_data('has_user_incivility_status', db_session),
        'number_of_user_incivility':
            read_access_conversation_data('number_of_user_incivility',  db_session),
        'has_user_indecency_status':
            read_access_conversation_data('has_user_indecency_status', db_session),
        'number_of_user_indecency':
            read_access_conversation_data('number_of_user_indecency', db_session),
        'has_user_incomprehension_status':
            read_access_conversation_data(
                'has_user_incomprehension_status', db_session),
        'number_of_user_incomprehension':
            read_access_conversation_data('number_of_user_incomprehension', db_session),
        'number_of_user_entries':
            read_access_conversation_data('number_of_user_entries', db_session),
        'has_fatigue_quotas_of_grandpy':
            read_access_conversation_data('has_fatigue_quotas_of_grandpy', db_session),
        'grandpy_status_code':
            read_access_conversation_data('grandpy_status_code', db_session)}
    chat_session = Conversation(user_request, db_number, **args)
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





def main(user_request, db_number=0):
    """question answer between user and Grandpy"""
    # 6) DONE Create test_main.py module
    # 8) DONE correct query creation X1
    print('[main]...')
    db_session = get_database_access(db_number)
    chat_session = conversation_between_user_and_grandpy(user_request, db_session, db_number)
    print(f'number_incivility avant set_attribut[main] = {chat_session.number_of_user_incivility}')
    chat_session.set_attributes_from_database()
    print(f"number incivility avant calculate dans main = {chat_session.number_of_user_incivility}")
    # chat_session.user_behavior_initialization()
    chat_session.calculate_the_incivility_status()
    print("number incivility avant counting behavior dans main ="
          f" {chat_session.number_of_user_incivility}")
    counting_behavior.user_incivility_count(chat_session)
    print("number incivility apres counting behavior dans main ="
          f" {chat_session.number_of_user_incivility}")
    # chat_session.calculate_the_indecency_status(chat_session)
    # counting_behavior.user_indecency_count(chat_session)
    # chat_session.calculate_the_incomprehension_status(chat_session)
    # counting_behavior.user_incomprehension_count(chat_session)
    chat_session.update_database()
    return chat_session


if __name__ == '__main__':
    pass
