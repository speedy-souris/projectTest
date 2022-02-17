#!/usr/bin/env python
"""main module"""
from conversation import Conversation
from redis_utilities import erasing_data


def search_address_to_wiki(user_request, db_number=0):
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
    print("Grandpy response[Accueil] :  Bonjour mon petit en quoi puis je t'aider")
    chat = search_address_to_wiki('bonjour')
    print(f"user_request {chat.user_entry}")
    print(f'\nuser_behavior = {chat.user_behavior}')
    # request_parsed = chat.get_request_parser()
    # print(f'user_request parsed : {chat.user_entry}')
    for i in range(11):
        print(f" request number  {i+1}")
        print(f"Grandpy_response {chat.__class__.GRANDPY_CODE[chat.user_behavior['grandpy_code']]}")
        chat1 = search_address_to_wiki('ou se trouve openClassrooms')
        chat = chat1
        print(f"user_request {chat.user_entry}")
        print(f'\nuser_behavior = {chat.user_behavior}')
