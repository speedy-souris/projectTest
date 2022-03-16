#!/usr/bin/env python
"""main module"""
from conversation import Conversation
from redis_utilities import erasing_data


# 3) DONE create max_number_of_incivility
def max_number_of_incivility(chat_session):
    # DONE max_incivlity counter
    """restoration of grandpy's status since a number of user incivility equal to 3"""
    incivility_limit_finded = chat_session.__class__.get_grandpy_status_key(7)  #  incivility_limit
    #  user_incivility_status
    chat_session.user_behavior[chat_session.__class__.USER_BEHAVIOR_DEFAULT_DATA_KEY[0]] = True
    #  fatigue_quotas_of_grandpy
    chat_session.user_behavior[chat_session.__class__.USER_BEHAVIOR_DEFAULT_DATA_KEY[3]] = True
    print(
        'Réponse de Grandpy : '
        f'{chat_session.__class__.read_grandpy_answer(incivility_limit_finded)}'
    )
    log_off_for_24_hours = chat_session.__class__.get_grandpy_status_key(10)  # exhausted
    print(
        f'Réponse de Grandpy : {chat_session.__class__.read_grandpy_answer(log_off_for_24_hours)}'
    )


def max_number_of_indecency(chat_session):
    # DONE max_indecency counter
    """restoration of grandpy's status since a number of user indecency equal to 3"""
    indecency_limit_reached = chat_session.get_grandpy_status(
        chat_session.__class__.grandpy_status_search_key(
            chat_session.__class__.GRANDPY_STATUS_DATA['disrespectful']
        )
    )
    chat_session.user_behavior[indecency_limit_reached] = True
    chat_session.user_behavior['fatigue_quotas'] = True
    print(f'Réponse de Grandpy : {chat_session.user_behavior[indecency_limit_reached]}')
    log_off_for_24_hours = chat_session.get_grandpy_status(
        chat_session.__class__.grandpy_status_search_key(
            chat_session.__class__.grandpy_status_search_key(
                chat_session.__class__.read_grandpy_answer('exhausted')
            )
        )
    )
    print(f'Réponse de Grandpy : {chat_session.user_behavior[log_off_for_24_hours]}')


def max_number_of_incomprehension(chat_session):
    # DONE max incomprehension counter
    """restoration of grandpy's status since a number of user incomprehension equal to 3"""
    incomprehension_limit_reached = chat_session.get_grandpy_status(
        chat_session.__class__.grandpy_status_search_key(
            chat_session.__class__.GRANDPY_STATUS_DATA['incomprehension_limit']
        )
    )
    chat_session.user_behavior[incomprehension_limit_reached] = True
    chat_session.user_behavior['fatigue_quotas'] = True
    print(f'Réponse de Grandpy : {chat_session.user_behavior[incomprehension_limit_reached]}')
    log_off_for_24_hours = chat_session.get_grandpy_status(
        chat_session.__class__.grandpy_status_search_key(
            chat_session.__class__.grandpy_status_search_key(
                chat_session.__class__.read_grandpy_answer('exhausted')
            )
        )
    )
    print(f'Réponse de Grandpy : {chat_session.user_behavior[log_off_for_24_hours]}')


def number_of_user_entries_to_X5(chat_session):
    # DONE user_entries X5
    """restore grandpy status from correct user request count of 5"""
    level_tired = chat_session.get_grandpy_status(
        chat_session.__class__.grandpy_status_search_key(
             chat_session.__class__.GRANDPY_STATUS_DATA['tired']
        )
    )
    chat_session.user_behavior['grandpy_code'] = level_tired
    print(f'Réponse de Grandpy : {chat_session.user_behavior[level_tired]}')
    log_off_for_24_hours = chat_session.get_grandpy_status(
        chat_session.__class__.grandpy_status_search_key(
            chat_session.__class__.read_grandpy_answer('exhausted')
        )
    )
    print(f'Réponse de Grandpy : {chat_session.user_behavior[log_off_for_24_hours]}')


def max_number_of_user_entries(chat_session):
    # DONE max_user_entries counter
    """restoration of grandpy's status
    since a maximum number of correct requests from the user equal to 10"""
    chat_session.user_behavior['fatigue_quotas'] = True
    log_off_for_24_hours = chat_session.get_grandpy_status(
        chat_session.__class__.grandpy_status_search_key(
            chat_session.__class__.read_grandpy_answer('exhausted')
        )
    )
    print(f'Réponse de Grandpy : {chat_session.user_behavior[log_off_for_24_hours]}')


def conversation_between_user_and_grandpy(user_request, db_number=0):
    # DONE conversation object
    """creation of the chat_session conversation object according to the user's request"""
    chat_session = Conversation(user_request, db_number=db_number)
    return chat_session


# ---------------------------
# 4) DONE management of the call to the GoogleMap API
def search_address_to_gMap(chat_session, user_request_parsed):
    # DONE GoogleMap API calling
    """call of the GoogleMap APIs according to the user's request"""
    gmap_api_placeId_value = chat_session.get_placeid_from_address(user_request_parsed)
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
    chat_session.calculate_the_incivility()
    # incivility_limit
    if chat_session.__class__.read_grandpy_answer(
        chat_session.__class__.get_grandpy_status_key(7)) == 'incivility_limit':
        max_number_of_incivility(chat_session)
    else:
        chat_session.user_behavior[chat_session.__class__.USER_BEHAVIOR_DEFAULT_DATA_KEY[4]] =\
            chat_session.__class__.get_grandpy_status_key(1)

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
    chat_session.update_database(db_number)
    return chat_session


def OLD_search_address_to_wiki(user_request, db_number=0):
    """Searched for a googleMaps address with a Wikipedia history"""
    chat_session = Conversation(user_request, db_number=db_number)
    if chat_session.user_behavior['grandpy_code'] == 'home':
        if user_request in chat_session.__class__.INCIVILITY_SET_DATA:
            # print(f'user_question : {user_request}, Grandpy !')
            pass
        else:
            # print(f'user_question : {user_request} ?')
            chat_session.calculate_the_incivility()
        if not chat_session.user_behavior['user_incivility']:
            chat_session.calculate_the_indecency()
            if not chat_session.user_behavior['user_indecency']:
                chat_session.calculate_the_incomprehension()
                if not chat_session.user_behavior['user_incomprehension']:
                    chat_session.calculate_the_user_entries()
            else:
                chat_session.user_behavior['grandpy_code'] = \
                    chat_session.__class__.grandpy_status_search_key(
                        "Bonjour Mon petit, en quoi puis-je t'aider ?"
                    )
                # print(
                #     'Grandpy_response[user_indecency] : '
                #     f"{chat.get_grandpy_status(chat.user_behavior['grandpy_code'])}"
                # )
        else:
            chat_session.user_behavior['grandpy_code'] =\
                chat_session.__class__.grandpy_status_search_key(
                        "Bonjour Mon petit, en quoi puis-je t'aider ?"
                )
            # print(
            #     'Grandpy_response[user_incivility] : '
            #     f"{chat_session.get_grandpy_status(chat_session.user_behavior['grandpy_code'])}"
            # )
    elif not chat_session.user_behavior['fatigue_quotas'] and\
            chat_session.user_behavior['number_of_user_entries'] == 0:
        chat_session.calculate_the_incivility()
        if not chat_session.user_behavior['user_incivility']:
            chat_session.calculate_the_indecency()
            if not chat_session.user_behavior['user_indecency']:
                chat_session.calculate_the_incomprehension()
                if not chat_session.user_behavior['user_incomprehension']:
                    chat_session.calculate_the_user_entries()
            else:
                chat_session.user_behavior['grandpy_code'] = \
                    chat_session.__class__.grandpy_status_search_key(
                        "Bonjour Mon petit, en quoi puis-je t'aider ?"
                    )
                # print(
                #     'Grandpy_response[user_indecency] : '
                #     f"{chat.get_grandpy_status(chat.user_behavior['grandpy_code'])}"
                # )
    else:
        chat_session.user_entry = chat_session.get_request_parser()
        # print(f'search keyword : {user_request} ?')
        chat_session.calculate_the_user_entries()
    print(f"Fatique_quotas = {chat_session.user_behavior['fatigue_quotas']}")
    print(f"nombre de conversation utilisateur {chat_session.user_behavior['number_of_user_entries']}")
    chat_session.update_database(db_number=db_number)
    return chat_session


if __name__ == '__main__':
    erasing_data(0)
    main('bonjour', db_number=0)
    print(f"présentation de l'utilisateur : {user_request}")
    print(chat_session.read_grandpy_answer())
    print(f"requete utilisateur = {'ou se trouve openClassrooms'}")



