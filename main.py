#!/usr/bin/env python3
"""main module"""
from . import Conversation
from . import counting_behavior
from . import RedisDataManagement
# from . import user_question_answer_count
# from . import display_grandpy_status_code_to_response


def conversation_between_user_and_grandpy(user_request, db_session):
    # DONE conversation object
    """creation of the chat_session conversation object according to the user's request"""
    print('avant la condition [main]')
    if not db_session.scan_database_redis():
        chat_session = Conversation(user_request, db_session)
        chat_session.database_init_by_default()
    level = db_session.byte_to_int_conversion(db_session.read_access_conversation_data('level'))
    has_user_incivility_status = db_session.byte_to_boolean_conversion(
        db_session.read_access_conversation_data('has_user_incivility_status'))
    number_of_user_incivility = db_session.byte_to_int_conversion(
        db_session.read_access_conversation_data('number_of_user_incivility'))
    has_user_indecency_status = db_session.byte_to_boolean_conversion(
        db_session.read_access_conversation_data('has_user_indecency_status'))
    number_of_user_indecency = db_session.byte_to_int_conversion(
        db_session.read_access_conversation_data('number_of_user_indecency'))
    has_user_incomprehension_status = db_session.byte_to_boolean_conversion(
        db_session.read_access_conversation_data('has_user_incomprehension_status'))
    number_of_user_incomprehension = db_session.byte_to_int_conversion(
        db_session.read_access_conversation_data('number_of_user_incomprehension'))
    number_of_user_entries = db_session.byte_to_int_conversion(
        db_session.read_access_conversation_data('number_of_user_entries'))
    has_fatigue_quotas_of_grandpy = db_session.byte_to_boolean_conversion(
        db_session.read_access_conversation_data('has_fatigue_quotas_of_grandpy'))
    grandpy_status_code = db_session.byte_to_string_conversion(
        db_session.read_access_conversation_data('grandpy_status_code'))

    args = {
        'level': level,
        'has_user_incivility_status': has_user_incivility_status,
        'number_of_user_incivility': number_of_user_incivility,
        'has_user_indecency_status': has_user_indecency_status,
        'number_of_user_indecency': number_of_user_indecency,
        'has_user_incomprehension_status': has_user_incomprehension_status,
        'number_of_user_incomprehension': number_of_user_incomprehension,
        'number_of_user_entries': number_of_user_entries,
        'has_fatigue_quotas_of_grandpy': has_fatigue_quotas_of_grandpy,
        'grandpy_status_code': grandpy_status_code}
    chat_session = Conversation(user_request, db_session, **args)
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
    db_session = RedisDataManagement(db_number)
    chat_session = conversation_between_user_and_grandpy(user_request, db_session)
    chat_session.set_attributes_from_database()
    chat_session.calculate_the_incivility_status()
    counting_behavior.user_incivility_count(chat_session)
    # chat_session.calculate_the_indecency_status(chat_session)
    # counting_behavior.user_indecency_count(chat_session)
    # chat_session.calculate_the_incomprehension_status(chat_session)
    # counting_behavior.user_incomprehension_count(chat_session)
    chat_session.update_database()
    return chat_session


if __name__ == '__main__':
    pass
