"""main module"""
from src.redis_utilities import RedisDataManagement
from src.session.conversation import Conversation
from src.display import counting_behavior
from src.display import display_behavior
from src.APIs import google_api
from src.APIs import wikipedia_api


def conversation_between_user_and_grandpy(user_request, database_redis_number):
    # DONE conversation object
    """creation of the chat_session conversation object according to the user's request"""
    database_object_redis_connect = \
        RedisDataManagement(database_redis_number=database_redis_number)
    if database_object_redis_connect.db_session.ttl('has_fatigue_quotas_of_grandpy') == -2:
        database_object_redis_connect.redis_database_init_by_default()
    level = database_object_redis_connect.byte_to_int_conversion(
        database_object_redis_connect.read_redis_database_decoding(
        'level',db_session.decode_int_to_byte(1)))
    has_user_incivility_status = \
        database_object_redis_connect.byte_to_boolean_conversion(
        database_object_redis_connect.read_redis_database_decoding(
            'has_user_incivility_status',
            database_object_redis_connect.decode_string_to_byte(False)))
    number_of_user_incivility = database_object_redis_connect.byte_to_int_conversion(
        database_object_redis_connect.read_redis_database_decoding(
            'number_of_user_incivility',
            database_object_redis_connect.decode_int_to_byte(0)))
    has_user_indecency_status = \
        database_object_redis_connect.byte_to_boolean_conversion(
        database_object_redis_connect.read_redis_database_decoding(
            'has_user_indecency_status',
            database_object_redis_connect.decode_string_to_byte(False)))
    number_of_user_indecency = database_object_redis_connect.byte_to_int_conversion(
        database_object_redis_connect.read_redis_database_decoding(
            'number_of_user_indecency',
            database_object_redis_connect.decode_int_to_byte(0)))
    has_user_incomprehension_status = \
        database_object_redis_connect.byte_to_boolean_conversion(
        database_object_redis_connect.read_redis_database_decoding(
            'has_user_incomprehension_status',
            database_object_redis_connect.decode_string_to_byte(False)))
    number_of_user_incomprehension = \
        database_object_redis_connect.byte_to_int_conversion(
        database_object_redis_connect.read_redis_database_decoding(
            'number_of_user_incomprehension',
            database_object_redis_connect.decode_int_to_byte(0)))
    number_of_user_entries = database_object_redis_connect.byte_to_int_conversion(
        db_session.read_redis_database_decoding(
            'number_of_user_entries',database_object_redis_connect.decode_int_to_byte(0)))
    has_fatigue_quotas_of_grandpy = \
        database_object_redis_connect.byte_to_boolean_conversion(
        database_object_redis_connect.read_redis_database_decoding(
        'has_fatigue_quotas_of_grandpy',
        database_object_redis_connect.decode_string_to_byte(False)))
    grandpy_status_code = database_object_redis_connect.byte_to_string_conversion(
        database_object_redis_connect.read_redis_database_decoding(
            'grandpy_status_code',
            database_object_redis_connect.decode_string_to_byte('home')))
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

    chat_object_connect = Conversation(user_request, db_number, **args)
    return chat_object_connect, database_object_redis_connect


# ---------------------------
# 4) DONE management of the call to the GoogleMap API
def search_address_to_gMap(user_request):
    # DONE GoogleMap API calling
    """call of the GoogleMap APIs according to the user's request"""
    gmap_api_placeid_value = google_api.get_placeid_from_address(user_request)
    place_id = gmap_api_placeid_value['candidates'][0]['place_id']
    googleMap_data = google_api.get_address_api_from_placeid(place_id)
    return googleMap_data


def management_of_incivility_behavior(chat_object_connect):
    chat_object_connect.calculate_the_incivility_status()
    if chat_object_connect.has_user_incivility_status:
        if chat_object_connect.number_of_user_incivility < 3:

            display_behavior.display_grandpy_status_code_to_mannerless(chat_object_connect)
            counting_behavior.user_incivility_count(chat_object_connect)
        else:
            display_behavior.display_grandpy_status_code_to_incivility_limit(chat_object_connect)
    else:
        chat_object_connect.from_level1_to_level2()

def management_of_indecency_behavior(chat_session):
    chat_session.calculate_the_indecency_status()
    if chat_session.has_user_indecency_status:
        if chat_session.number_of_user_indecency < 3:
             display_behavior.display_grandpy_status_code_to_disrespectful(chat_session)
             counting_behavior.user_indecency_count(chat_session)
        else:
             display_behavior.display_grandpy_status_code_to_indecency_limit(chat_session)


def management_of_incomprehension_behavior(chat_session):
    chat_session.calculate_the_incomprehension_status()
    if chat_session.has_user_incomprehension_status:
        if chat_session.number_of_user_incomprehension < 3:
            display_behavior.display_grandpy_status_code_to_incomprehension(chat_session)
            counting_behavior.user_incomprehension_count(chat_session)
        else:
            display_behavior.display_grandpy_status_code_to_incomprehension_limit(chat_session)


def management_of_correct_behavior(chat_session):
    if (not chat_session.has_user_indecency_status 
        and
        not chat_session.has_user_incomprehension_status):
        if chat_session.number_of_user_entries == 5:
            display_behavior.display_grandpy_status_code_to_tired(chat_session)
            counting_behavior.user_question_answer_count(chat_session)
        elif chat_session.number_of_user_entries == 10:
            display_behavior.display_grandpy_status_code_to_response_limit(chat_session)
        else:
            display_behavior.display_grandpy_status_code_to_response(chat_session)
            counting_behavior.user_question_answer_count(chat_session)
            chat_session.get_user_request_parser()


def main(user_request, database_redis_number=0):
    """question answer between user and Grandpy"""
    print('Main')
    # ~ import pdb; pdb.set_trace()
    object_connection = \
        conversation_between_user_and_grandpy(user_request, database_redis_number)
    chat_object_connect = connection[0]
    database_object_redis_connect = connection[1]
    # management level 1
    if (
        chat_object_connect.level == 1
        and
        database_object_redis_connect.db_session.ttl('has_fatigue_quotas_of_grandpy') == -1
    ):
        management_of_incivility_behavior(chat_object_connect)
        management_of_indecency_behavior(chat_object_connect)
        # ~ if user_request not in sessions[0].INCIVILITY_SET_DATA:
        management_of_incomprehension_behavior(chat_object_connect)
    # management level 2
    elif (
        chat_object_connect.level == 2
        and
        database_object_redis_connect.db_session.ttl('has_fatigue_quotas_of_grandpy') == -1
    ):
        # ~ import pdb; pdb.set_trace()
        management_of_indecency_behavior(chat_object_connect)
        # ~ if user_request in sessions[0].INCOMPREHENSION_SET_DATA:
        management_of_incomprehension_behavior(chat_object_connect)
        management_of_correct_behavior(chat_object_connect)

    database_object_redis_connect.update_redis_database(chat_object_connect)
    return chat_object_connect


if __name__ == '__main__':
    pass

