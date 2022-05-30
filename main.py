#!/usr/bin/env python3
"""main module"""
from . import Conversation
from . import display_grandpy_status_code_to_home
from . import display_grandpy_status_code_to_benevolent
from . import display_grandpy_status_code_to_mannerless
from . import display_grandpy_status_code_to_disrespectful
from . import display_grandpy_status_code_to_incomprehension
from . import display_grandpy_status_code_to_response
from . import user_incivility_count
from . import user_indecency_count
from . import user_incomprehension_count
# from . import user_question_answer_count
# from . import display_grandpy_status_code_to_response


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


# --------------------------
# -- PRESENTATION OF USER --
# --------------------------
def get_presentation_management(chat_session, level, behavior_level):
    """management of user behavior during presentation"""
    # if user_behavior['grandpy_status_code'] = 'home'
    if chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('home'):
        get_user_presentation_management(chat_session, level, behavior_level)
    # if user_behavior['has_user_incivility_status'] = 'mannerless'
    elif chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('has_user_incivility_status')]\
            == chat_session.__class__.get_grandpy_status_key('mannerless'):
        get_user_presentation_management(chat_session, level, behavior_level)
    # if user_behavior['has_user_indecency_status'] = 'disrespectful'
    elif chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('has_user_indecency_status')]\
            == chat_session.__class__.get_grandpy_status_key('disrespectful'):
        get_user_presentation_management(chat_session, level, behavior_level)
    # if user_behavior['has_user_incomprehension_status'] = 'incomprehension'
    elif chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('has_user_incomprehension_status')]\
            == chat_session.__class__.get_grandpy_status_key('incomprehension'):
        get_user_presentation_management(chat_session, level, behavior_level)
    elif chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('benevolent'):
        display_grandpy_status_code_to_benevolent(chat_session)


# ---------------------------
def get_user_presentation_management(chat_session, level, behavior_level):
    """management of the presentation of the user"""
    display_grandpy_status_code_to_home(chat_session)
    chat_session.calculate_the_incivility_status()
    # if user_behavior['has_user_incivility_status'] = True
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('has_user_incivility_status')]:
        display_grandpy_status_code_to_mannerless(chat_session)
        get_behavior_presentation_management(chat_session, level, behavior_level)
    chat_session.calculate_the_indecency_status(level, behavior_level)
    # if user_behavior['has_user_indecency_status'] = True
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('has_user_indecency_status')]:
        display_grandpy_status_code_to_disrespectful(chat_session)
        get_behavior_presentation_management(chat_session, level, behavior_level)
    behavior_level = 'incomprehension'
    chat_session.calculate_the_incomprehension_status(level, behavior_level)
    # if user_behavior['has_user_incomprehension_status'] = True
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('has_user_incomprehension_status')]:
        display_grandpy_status_code_to_incomprehension(chat_session)
        get_behavior_presentation_management(chat_session, level, behavior_level)
    # if user_behavior['grandpy_status_code'] = 'home'
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('home'):
        chat_session.user_behavior['grandpy_status_code']\
            = chat_session.__class__.get_grandpy_status_key('benevolent')
# ------------------------------------


def get_behavior_presentation_management(chat_session, level, behavior_level):
    """management of the behavioral user in presentation"""
    # if user_behavior['grandpy_status_code'] = 'mannerless'
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('mannerless'):
        user_incivility_count(chat_session)
    # if user_behavior['grandpy_status_code'] = 'disrespectful'
    elif chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('disrespectful'):
        user_indecency_count(chat_session, level, behavior_level)
    # if user_behavior['grandpy_status_code'] = 'incomprehension'
    elif chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('incomprehension'):
        user_incomprehension_count(chat_session, level, behavior_level)
# --------------------------
# --         END          --
# -- PRESENTATION OF USER --
# --------------------------


# ------------------
# -- CHAT SESSION --
# ------------------

# -----------------------------------
def get_user_chat_session_management(chat_session):
    """session_chat management between user and grandpy"""
    display_grandpy_status_code_to_benevolent(chat_session)
    chat_session.calculate_the_indecency_status()
    # if user_behavior['has_user_indecency_status'] = True
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('has_user_indecency_status')]:
        display_grandpy_status_code_to_disrespectful(chat_session)
        get_behavior_chat_session_management(chat_session)
    chat_session.calculate_the_incomprehension_status()
    # if user_behavior['has_user_incomprehension_status'] = True
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('has_user_incomprehension_status')]:
        display_grandpy_status_code_to_incomprehension(chat_session)
        get_behavior_chat_session_management(chat_session)
    # if user_behavior['grandpy_status_code'] = 'benevolent'
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('benevolent'):
        chat_session.user_behavior['grandpy_status_code']\
            = chat_session.__class__.get_grandpy_status_key('response')
# -----------------------------------


def get_behavior_chat_session_management(chat_session):
    """management of the behavioral user in chat_session"""
    # if user_behavior['grandpy_status_code'] = 'disrespectful'
    if chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('disrespectful'):
        user_indecency_count(chat_session)
    # if user_behavior['grandpy_status_code'] = 'incomprehension'
    elif chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('incomprehension'):
        user_incomprehension_count(chat_session)
# ------------------
# --    END       --
# -- CHAT SESSION --
# ------------------


def main(user_request, db_number=0):
    """question answer between user and Grandpy"""
    # 6) DONE Create test_main.py module
    # 8) DONE correct query creation X1
    chat_session = conversation_between_user_and_grandpy(user_request, db_number=db_number)
    get_presentation_management(chat_session, 'presentation', 'indecency')
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('benevolent'):
        get_user_chat_session_management(chat_session)
    # # if user_behavior['grandpy_status_code'] = 'disrespectful'
    # elif chat_session.user_behavior[
    #         chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
    #         == chat_session.__class__.get_grandpy_status_key('disrespectful'):
    #     get_user_chat_session_management(chat_session)
    # # if user_behavior['grandpy_status_code'] = 'incomprehension'
    # elif chat_session.user_behavior[
    #     chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
    #         == chat_session.__class__.get_grandpy_status_key('incomprehension'):
    #     get_user_chat_session_management(chat_session)
    # elif chat_session.user_behavior[
    #     chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
    #         == chat_session.__class__.get_grandpy_status_key('response'):
    #     display_grandpy_status_code_to_response(chat_session)
    chat_session.update_database()
    return chat_session


if __name__ == '__main__':
    pass
