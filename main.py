"""main module"""
from src.redis_utilities import RedisDataManagement
from src.session.conversation import Conversation
from src.display import counting_behavior
from src.display import display_behavior
from src.APIs import google_api
from src.APIs import wikipedia_api


def conversation_between_user_and_grandpy(user_request, database_redis_number):
    """creation of the chat_connect_object conversation object according to the user's request"""
    database_redis_connect_object = \
        RedisDataManagement(database_redis_number=database_redis_number)
    # has_fatigue_quotas_of_grandpy'data  expired inside redis
    if database_redis_connect_object.database_connect.ttl(
        'has_fatigue_quotas_of_grandpy') == -2:
        database_redis_connect_object.redis_database_init_by_default()
    number_of_user_entries = database_redis_connect_object.byte_to_int_conversion(
        database_redis_connect_object.read_redis_database_decoding(
            'number_of_user_entries',database_redis_connect_object.decode_int_to_byte(0)))
    has_fatigue_quotas_of_grandpy = \
        database_redis_connect_object.byte_to_boolean_conversion(
        database_redis_connect_object.read_redis_database_decoding(
        'has_fatigue_quotas_of_grandpy',
        database_redis_connect_object.decode_string_to_byte(False)))
    grandpy_status_code = database_redis_connect_object.byte_to_string_conversion(
        database_redis_connect_object.read_redis_database_decoding(
            'grandpy_status_code',
            database_redis_connect_object.decode_string_to_byte('home')))
    has_user_incomprehension_status = \
        database_redis_connect_object.byte_to_boolean_conversion(
        database_redis_connect_object.read_redis_database_decoding(
            'has_user_incomprehension_status',
            database_redis_connect_object.decode_string_to_byte(False)))
    args = {
        'number_of_user_entries': number_of_user_entries,
        'has_fatigue_quotas_of_grandpy': has_fatigue_quotas_of_grandpy,
        'grandpy_status_code': grandpy_status_code}

    chat_connect_object = Conversation(user_request, database_redis_number, **args)
    return chat_connect_object, database_redis_connect_object

def management_of_incomprehension_behavior(chat_connect_object):
    coordinates_googleMap_API = \
        chat_connect_object.calculate_the_incomprehension_status()
    if chat_connect_object.has_user_incomprehension_status:
        display_behavior.display_grandpy_status_code_to_incomprehension(
                chat_connect_object)
    return coordinates_googleMap_API


def management_of_correct_behavior(chat_connect_object):
    if chat_connect_object.number_of_user_entries == 10:
        display_behavior.display_grandpy_status_code_to_response_limit(chat_connect_object)
    else:
        display_behavior.display_grandpy_status_code_to_response(chat_connect_object)
        counting_behavior.user_question_answer_count(chat_connect_object)
        chat_connect_object.get_user_request_parser()


def main(user_request, database_redis_number=0):
    """question answer between user and Grandpy"""
    print('Main')
    coordinates_googleMap_API = {'candidates': [], 'status': 'ZERO_RESULTS'}
    connection_object = \
        conversation_between_user_and_grandpy(user_request, database_redis_number)
    chat_connect_object = connection_object[0]
    database_redis_connect_object = connection_object[1]
    chat_connect_object.get_user_request_parser()
    # management level 1
    if  database_redis_connect_object.database_connect.ttl(
            'has_fatigue_quotas_of_grandpy') == -1:
        management_of_correct_behavior(chat_connect_object)
        coordinates_googleMap_API = \
            management_of_incomprehension_behavior(chat_connect_object)
        if not chat_connect_object.has_user_incomprehension_status:
            management_of_correct_behavior(chat_connect_object)
        elif chat_connect_object.has_user_incomprehension_status:
            management_of_incomprehension_behavior(chat_connect_object)
            chat_connect_object.number_of_user_entries -= 1
    database_redis_connect_object.update_redis_database(chat_connect_object)
    chat_connect_object.coordinates_api = coordinates_googleMap_API
    print(f'[main] = {chat_connect_object.coordinates_api}')
    return chat_connect_object


if __name__ == '__main__':
    pass

