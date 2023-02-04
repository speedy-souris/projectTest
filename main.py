"""main module"""
from src.redis_utilities import RedisDataManagement
from src.session.conversation import Conversation
from src.display import counting_behavior
from src.display import display_behavior
from src.APIs import google_api
from src.APIs import wikipedia_api


def conversation_between_user_and_grandpy(user_request, db_number):
    # DONE conversation object
    """creation of the chat_session conversation object according to the user's request"""
    chat_session = Conversation(user_request, db_number=db_number)
    db_session = RedisDataManagement(db_number=db_number)
    if not db_session.scan_database_redis():
        # ~ chat_session = Conversation(user_request, db_number=db_number)
        chat_session.database_init_by_default()
        # ~ print(f'grandpy_home [main] = {chat_session.grandpy_status_code}')
    else:
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
        chat_session = Conversation(user_request, db_number, **args)
    return chat_session


# ---------------------------
# 4) DONE management of the call to the GoogleMap API
def search_address_to_gMap(user_request):
    # DONE GoogleMap API calling
    """call of the GoogleMap APIs according to the user's request"""
    gmap_api_placeid_value = google_api.get_placeid_from_address(user_request)
    place_id = gmap_api_placeid_value['candidates'][0]['place_id']
    googleMap_data = google_api.get_address_api_from_placeid(place_id)
    return googleMap_data


# 5) TODO management of the call to the WikiPedia API
def search_address_to_wiki(user_request_parsed):
    # DONE WIKIPEDIA API calling
    """call of the WikiPedia APIs according to the user's request"""
    googleMap_data = search_address_to_gMap(user_request_parsed)
    latitude = \
        googleMap_data['result']['geometry']['location']['lat']
    longitude = \
        googleMap_data['result']['geometry']['location']['lng']
    wiki_pages= wikipedia_api.get_address_url(latitude, longitude)
    for title in wiki_pages['query']['geosearch'][0]['title']:
        if title in googleMap_data['result']['formatted_address']:
            wiki_result = wikipedia_api.get_page_url(user_request_parsed)
    return wiki_result


def management_of_incivility_behavior(chat_session):
    chat_session.calculate_the_incivility_status()
    if chat_session.has_user_incivility_status:
        if chat_session.number_of_user_incivility < 3:
            display_behavior.display_grandpy_status_code_to_mannerless(chat_session)
            counting_behavior.user_incivility_count(chat_session)
        else:
            print('je suis arrivez la')
            display_behavior.display_grandpy_status_code_to_incivility_limit(chat_session)
    else:
        chat_session.level = 2


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
    if not (
        chat_session.has_user_indecency_status and\
        chat_session.has_user_incomprehension_status):
        print(f'number user_entries [main-correct_behavior] = {chat_session.number_of_user_entries}')
        if chat_session.number_of_user_entries == 5:
            display_behavior.display_grandpy_status_code_to_tired(chat_session)
            counting_behavior.user_question_answer_count(chat_session)
        elif chat_session.number_of_user_entries == 10:
            display_behavior.display_grandpy_status_code_to_response_limit(chat_session)
        else:
            display_behavior.display_grandpy_status_code_to_response(chat_session)
            counting_behavior.user_question_answer_count(chat_session)
            chat_session.get_user_request_parser()


def main(user_request, db_number=0):
    """question answer between user and Grandpy"""
    chat_session = conversation_between_user_and_grandpy(user_request, db_number)
    # management level 1
    if chat_session.level == 1:
        management_of_incivility_behavior(chat_session)
        management_of_indecency_behavior(chat_session)
        management_of_incomprehension_behavior(chat_session)
    # management level 2
    elif chat_session.level == 2:
        management_of_indecency_behavior(chat_session)
        management_of_incomprehension_behavior(chat_session)
        management_of_correct_behavior(chat_session)
    chat_session.update_database()
    return chat_session

def main_old(user_request, db_number=0):
    """question answer between user and Grandpy"""
    # 6) DONE Create test_main.py module
    # 8) DONE correct query creation X1
    print('[main]...')
    chat_session = conversation_between_user_and_grandpy(user_request, db_number)
    display_behavior.display_grandpy_status_code_to_home(chat_session)
    # ~ chat_session.set_attributes_from_database()
    if chat_session.level == 1:
        chat_session.calculate_the_incivility_status()
        chat_session.calculate_the_indecency_status()
        chat_session.calculate_the_incomprehension_status()
        if chat_session.has_user_incivility_status:
            if chat_session.number_of_user_incivility < 3:
                display_behavior.display_grandpy_status_code_to_mannerless(chat_session)
                counting_behavior.user_incivility_count(chat_session)
            else:
                display_behavior.display_grandpy_status_code_to_incivility_limit(chat_session)
        if chat_session.has_user_indecency_status:
            if chat_session.number_of_user_indecency < 3:
                display_behavior.display_grandpy_status_code_to_disrespectful(chat_session)
                counting_behavior.user_indecency_count(chat_session)
            else:
                display_behavior.display_grandpy_status_code_to_indecency_limit(chat_session)
        if chat_session.has_user_incomprehension_status:
            if chat_session.number_of_user_incomprehension < 3:
                display_behavior.display_grandpy_status_code_to_incomprehension(chat_session)
                counting_behavior.user_incomprehension_count(chat_session)
            else:
                display_behavior.display_grandpy_status_code_to_incomprehension_limit(chat_session)
        if not chat_session.has_user_incivility_status:
            chat_session.level = 2

    elif chat_session.level == 2:
        display_behavior.display_grandpy_status_code_to_benevolent(chat_session)
        chat_session.calculate_the_indecency_status()
        chat_session.calculate_the_incomprehension_status()
        if chat_session.has_user_indecency_status:
            if chat_session.number_of_user_indecency < 3:
                display_behavior.display_grandpy_status_code_to_disrespectful(chat_session)
                counting_behavior.user_indecency_count(chat_session)
            else:
                display_behavior.display_grandpy_status_code_to_indecency_limit(chat_session)
        if chat_session.has_user_incomprehension_status:
            if chat_session.number_of_user_incomprehension < 3:
                display_behavior.display_grandpy_status_code_to_incomprehension(chat_session)
                counting_behavior.user_incomprehension_count(chat_session)
            else:
                display_behavior.display_grandpy_status_code_to_incomprehension_limit(chat_session)
        if not (
            chat_session.has_user_indecency_status and\
            chat_session.has_user_incomprehension_status):
            if chat_session.number_of_user_entries == 5:
                display_behavior.display_grandpy_status_code_to_tired(chat_session)
            elif chat_session.number_of_user_entries == 9:
                display_behavior.display_grandpy_status_code_to_response_limit(chat_session)
            else:
                display_behavior.display_grandpy_status_code_to_response(chat_session)
            counting_behavior.user_question_answer_count(chat_session)
            chat_session.get_user_request_parser()
    chat_session.update_database()
    # ~ googlemap_address = search_address_to_gMap(user_request)
    # ~ wikipedia = search_address_to_wiki(user_request)
    return chat_session


if __name__ == '__main__':
    pass

