#!/usr/bin/env python3
"""main module"""
from src.session.behavior_parameters import BehaviorParams
from src.display.display_behavior import display_grandpy_status_code_to_home
from src.display.display_behavior import display_grandpy_status_code_to_benevolent
from src.display.display_behavior import display_grandpy_status_code_to_mannerless
from src.display.display_behavior import display_grandpy_status_code_to_disrespectful
from src.display.display_behavior import display_grandpy_status_code_to_inconsistency
from src.display.display_behavior import display_grandpy_status_code_to_response
from src.display.counting_behavior import user_incivility_count
from src.display.counting_behavior import user_indecency_count
from src.display.counting_behavior import user_incomprehension_count
from src.display import display_behavior
# from . import user_question_answer_count
# from . import display_grandpy_status_code_to_response


def conversation_between_user_and_grandpy(user_request, db_number):
    # DONE conversation object
    """creation of the chat_session conversation object according to the user's request"""
    chat_session = BehaviorParams(user_request, db_number)
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


def define_indecency_chosen(chat_session):
    """choose the parameter of indecency status since level --> 1 / 2
    ==> ' Presentation ' / ' Chat_session '"""
    has_user_indecency_status = None
    # if user_behavior['behavior_level'] = 'presentation'
    if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('behavior_level')]\
            == chat_session.level_parameters(1):
        has_user_indecency_status\
            = chat_session.level_name_user(
                chat_session.user_behavior[
                    chat_session.__class__.get_user_behavior_key('behavior_level')]
                , chat_session.level_name_user(
                    chat_session.level_parameters(1), 'has_user_indecency_status'))
    # if user_behavior['behavior_level'] = 'chat_session'
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('behavior_level')]\
            == chat_session.level_parameters(2):
        has_user_indecency_status\
            = chat_session.level_name_user(
                chat_session.user_behavior[
                    chat_session.__class__.get_user_behavior_key('behavior_level')]
                , chat_session.level_name_user(
                    chat_session.level_parameters(2), 'has_user_indecency_status2'))
    return has_user_indecency_status


def define_number_indecency_chosen(chat_session):
    """choose the parameter of indecency number since level --> 1 / 2
    ==> ' Presentation ' / ' Chat_session '"""
    number_of_user_indecency = None
    # if user_behavior['behavior_level'] = 'presentation'
    if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('behavior_level')]\
            == chat_session.level_parameters(1):
        number_of_user_indecency\
            = chat_session.level_name_user(
                chat_session.user_behavior[
                    chat_session.__class__.get_user_behavior_key('behavior_level')]
                , chat_session.level_name_user(
                    chat_session.level_parameters(1), 'number_of_user_indecency'))
    # if user_behavior['behavior_level'] = 'chat_session'
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('behavior_level')]\
            == chat_session.level_parameters(2):
        number_of_user_indecency\
            = chat_session.level_name_user(
                chat_session.user_behavior[
                    chat_session.__class__.get_user_behavior_key('behavior_level')]
                , chat_session.level_name_user(
                    chat_session.level_parameters(2), 'number_of_user_indecency2'))
    return number_of_user_indecency


def define_incomprehension_chosen(chat_session):
    """choose the parameter of incomprehension status since level --> 1 / 2
    ==> ' Presentation ' / ' Chat_session '"""
    has_user_incomprehension_status = None
    # if user_behavior['behavior_level'] = 'presentation'
    if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('behavior_level')]\
            == chat_session.level_parameters(1):
        has_user_incomprehension_status\
            = chat_session.level_name_user(
                chat_session.user_behavior[
                    chat_session.__class__.get_user_behavior_key('behavior_level')]
                , chat_session.level_name_user(
                    chat_session.level_parameters(1), 'has_user_incomprehension_status'))
    # if user_behavior['behavior_level'] = 'chat_session'
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('behavior_level')]\
            == chat_session.level_parameters(2):
        has_user_incomprehension_status\
            = chat_session.level_name_user(
                chat_session.user_behavior[
                    chat_session.__class__.get_user_behavior_key('behavior_level')]
                , chat_session.level_name_user(
                    chat_session.level_parameters(2), 'has_user_incomprehension_status2'))
    return has_user_incomprehension_status


def define_number_incomprehension_chosen(chat_session):
    """choose the parameter of incomprehension number since level --> 1 / 2
    ==> ' Presentation ' / ' Chat_session '"""
    number_of_user_incomprehension = None
    # if user_behavior['behavior_level'] = 'presentation'
    if chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('behavior_level')]\
            == chat_session.level_parameters(1):
        number_of_user_incomprehension\
            = chat_session.level_name_user(
                chat_session.user_behavior[
                    chat_session.__class__.get_user_behavior_key('behavior_level')]
                , chat_session.level_name_user(
                    chat_session.level_parameters(1), 'number_of_user_incomprehension'))
    # if user_behavior['behavior_level'] = 'chat_session'
    elif chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('behavior_level')]\
            == chat_session.level_parameters(2):
        number_of_user_incomprehension\
            = chat_session.level_name_user(
                chat_session.user_behavior[
                    chat_session.__class__.get_user_behavior_key('behavior_level')]
                , chat_session.level_name_user(
                    chat_session.level_parameters(2), 'number_of_user_incomprehension2'))
    return number_of_user_incomprehension


def set_user_incivility_status(chat_session):
    """incivility status activation and counting"""
    chat_session.calculate_the_incivility_status()
    # if user_behavior['has_user_incivility_status'] = True
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('has_user_incivility_status')]:
        display_grandpy_status_code_to_mannerless(chat_session)
        user_incivility_count(chat_session)


def set_user_indecency_status(chat_session):
    """indecency status activation and counting --> level 1 / 2"""
    has_user_indecency_status = define_indecency_chosen(chat_session)
    number_of_user_indecency = define_number_indecency_chosen(chat_session)
    chat_session.calculate_the_indecency_status(has_user_indecency_status)
    # if user_behavior['has_user_indecency_status'] = True
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key(has_user_indecency_status)]:
        display_grandpy_status_code_to_disrespectful(chat_session)
        user_indecency_count(chat_session, number_of_user_indecency)


def set_user_incomprehension_status(chat_session):
    """incomprehension status activation and counting --> level 1 / 2"""
    has_user_incomprehension_status = define_incomprehension_chosen(chat_session)
    number_of_user_incomprehension = define_number_incomprehension_chosen(chat_session)
    chat_session.calculate_the_incomprehension_status(has_user_incomprehension_status)
    # if user_behavior['has_user_incomprehension_status'] = True
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key(has_user_incomprehension_status)]:
        display_grandpy_status_code_to_inconsistency(chat_session)
        user_incomprehension_count(chat_session, number_of_user_incomprehension)


def create_incivility_status(chat_session):
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('home'):
        chat_session.calculate_the_incivility_status()
        if chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('has_user_incivility_status')]:
            display_behavior.display_grandpy_status_code_to_mannerless(chat_session)
    # if user_behavior['grandpy_status_code'] = 'mannerless'
    if chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('mannerless'):
        if chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('number_of_user_incivility')] < 3:
            chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('number_of_user_incivility')] += 1
        elif chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('number_of_user_incivility')] >= 3:
            chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('number_of_user_incivility')] = 3
            display_behavior.display_grandpy_status_code_to_incivility_limit(chat_session)


def create_indecency_status(chat_session, level):
    # session level data initialization
    has_user_indecency_status = None
    number_of_user_indecency = None
    # leve 1 --> user_behavior|'behavior_level'] = 'presentation'
    if level == 'presentation':
        has_user_indecency_status\
            = chat_session.level_name_user('presentation', 'has_user_indecency_status')
        number_of_user_indecency\
            = chat_session.level_name_user('presentation', 'number_of_user_indecency')
    # level 2 --> user_behavior['behavior_level'] = 'chat_session'
    elif level == 'chat_session':
        has_user_indecency_status \
            = chat_session.level_name_user('chat_session', 'has_user_indecency_status2')
        number_of_user_indecency\
            = chat_session.level_name_user('chat_session', 'number_of_user_indecency')
    # user_behavior['grandpy_status_code'] = 'mannerless'
    if chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('grandpy_status_code')] \
            == chat_session.__class__.get_grandpy_status_key('mannerless'):
        chat_session.calculate_the_indecency_status(has_user_indecency_status)
        if chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key(has_user_indecency_status)]:
            display_behavior.display_grandpy_status_code_to_disrespectful(chat_session)
    # if user_behavior['grandpy_status_code'] = 'indecency'
    if chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('grandpy_status_code')] \
            == chat_session.__class__.get_grandpy_status_key('indecency'):
        if chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key(number_of_user_indecency)] < 3:
            chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key(number_of_user_indecency)] += 1
        elif chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key(number_of_user_indecency)] >= 3:
            chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key(number_of_user_indecency)] = 3
            display_behavior.display_grandpy_status_code_to_indecency_limit(chat_session)


def create_incomprehension_status(chat_session, level):
    # session level data initialization
    has_user_incomprehension_status = None
    number_of_user_incomprehension = None
    # leve 1 --> user_behavior|'behavior_level'] = 'presentation'
    if level == 'presentation':
        has_user_incomprehension_status\
            = chat_session.level_name_user('presentation', 'has_user_incomprehension_status')
        number_of_user_incomprehension\
            = chat_session.level_name_user('presentation', 'number_of_user_incomprehension')
    # level 2 --> user_behavior['behavior_level'] = 'chat_session'
    elif level == 'chat_session':
        has_user_incomprehension_status\
            = chat_session.level_name_user('chat_session', 'has_user_incomprehension_status2')
        number_of_user_incomprehension\
            = chat_session.level_name_user('chat_session', 'number_of_user_incomprehension')
    if chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('disrespectful'):
        chat_session.calculate_the_incomprehension_status(has_user_incomprehension_status)
        if chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key(has_user_incomprehension_status)]:
            display_behavior.display_grandpy_status_code_to_inconsistency(chat_session)
    # if user_behavior['grandpy_status_code'] = 'incomprehension'
    if chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('incomprehension'):
        if chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key(number_of_user_incomprehension)] < 3:
            chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key(number_of_user_incomprehension)] += 1
        elif chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key(number_of_user_incomprehension)] >= 3:
            chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key(number_of_user_incomprehension)] = 3
            display_behavior.display_grandpy_status_code_to_incomprehension_limit(chat_session)


# --------------------------
# -- PRESENTATION OF USER --
# --------------------------
def get_behavior_status_management(chat_session):
    """management of user behavior during presentation / chat_session"""
    # if user_behavior['grandpy_status_code'] = 'home'
    if chat_session.user_behavior[
        chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == chat_session.__class__.get_grandpy_status_key('home'):
        display_grandpy_status_code_to_home(chat_session)
        # initialization at level 1 ==> presentation
        chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('behavior_level')]\
            = chat_session.level_parameters(1)
        set_user_incivility_status(chat_session)
        # if user_behavior['grandpy_status_code'] = 'mannerless'
        if chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
                == chat_session.__class__.get_grandpy_status_key('mannerless'):
            get_behavior_status_management(chat_session)
        set_user_indecency_status(chat_session)
        # if user_behavior['grandpy_status_code'] = 'disrespectful'
        if chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
                == chat_session.__class__.get_grandpy_status_key('disrespectful'):
            get_behavior_status_management(chat_session)
        set_user_incomprehension_status(chat_session)
        # if user_behavior['grandpy_status_code'] = 'incomprehension'
        if chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
                == chat_session.__class__.get_grandpy_status_key('incomprehension'):
            get_behavior_status_management(chat_session)

    # if user_behavior['grandpy_status_code'] = 'mannerless'
    # elif chat_session.user_behavior[
    #     chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
    #         == chat_session.__class__.get_grandpy_status_key('mannerless'):
    #     user_incivility_count(chat_session)
    # # if user_behavior['grandpy_status_code'] = 'incomprehension'
    # elif chat_session.user_behavior[
    #     chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
    #         == chat_session.__class__.get_grandpy_status_key('incomprehension'):
    #     get_behavior_status_management(chat_session)
    # else:
    #     print(f"status_code = "
    #           f"{chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('grandpy_status_code')]}")
    #     chat_session.user_behavior[
    #         chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
    #         = chat_session.__class__.get_grandpy_status_key('benevolent')
    #     display_grandpy_status_code_to_benevolent(chat_session)
    #     # initialization at level 2 ==> chat_session
    #     chat_session.user_behavior[
    #         chat_session.__class__.get_user_behavior_key('behavior_level')]\
    #         = chat_session.level_parameters(2)
# --------------------------
# --         END          --
# -- PRESENTATION OF USER --
# --------------------------


def main(user_request, db_number=0):
    """question answer between user and Grandpy"""
    # 6) DONE Create test_main.py module
    # 8) DONE correct query creation X1
    chat_session = conversation_between_user_and_grandpy(user_request, db_number=db_number)
    # initialization session level
    chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('behavior_level')]\
        = chat_session.level_parameters(1)
    level_presentation\
        = chat_session.user_behavior[chat_session.__class__.get_user_behavior_key('behavior_level')]
    # get_behavior_status_management(chat_session)
    create_incivility_status(chat_session)
    # create_indecency_status(chat_session, level_presentation)
    # create_incomprehension_status(chat_session, level_presentation)
    # if chat_session.user_behavior[
    #         chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
    #         == chat_session.__class__.get_grandpy_status_key('benevolent'):
    #     get_behavior_status_management(
    #         chat_session, chat_session.level_parameters(2), 'has_user_indecency_status2')
    # if user_behavior['grandpy_status_code'] = 'mannerless'
    # if chat_session.user_behavior[
    #         chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
    #         == chat_session.__class__.get_grandpy_status_key('mannerless'):
    #     user_incivility_count(chat_session)
    # # if user_behavior['grandpy_status_code'] = 'disrespectful'
    # elif chat_session.user_behavior[
    #         chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
    #         == chat_session.__class__.get_grandpy_status_key('disrespectful'):
    #     if chat_session.user_behavior[
    #         chat_session.__class__.get_user_behavior_key('behavior_level')]\
    #             == chat_session.level_parameters(1):
    #         get_behavior_status_management(
    #             chat_session, chat_session.level_parameters(1), 'has_user_indecency_status')
    #     elif chat_session.user_behavior[
    #         chat_session.__class__.get_user_behavior_key('behavior_level')]\
    #             == chat_session.level_parameters(2):
    #         get_behavior_status_management(
    #             chat_session, chat_session.level_parameters(1), 'has_user_indecency_status2')
    # # if user_behavior['grandpy_status_code'] = 'incomprehension'
    # elif chat_session.user_behavior[
    #     chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
    #         == chat_session.__class__.get_grandpy_status_key('incomprehension'):
    #     if chat_session.user_behavior[
    #         chat_session.__class__.get_user_behavior_key('behavior_level')]\
    #             == chat_session.level_parameters(1):
    #         get_behavior_status_management(
    #             chat_session, chat_session.level_parameters(1), 'has_user_incomprehension_status')
    #     elif chat_session.user_behavior[
    #         chat_session.__class__.get_user_behavior_key('behavior_level')]\
    #             == chat_session.level_parameters(2):
    #         get_behavior_status_management(
    #             chat_session, chat_session.level_parameters(1), 'has_user_incomprehension_status2')
    # elif chat_session.user_behavior[
    #     chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
    #         == chat_session.__class__.get_grandpy_status_key('response'):
    #     display_grandpy_status_code_to_response(chat_session)
    chat_session.update_database()
    return chat_session


if __name__ == '__main__':
    pass
