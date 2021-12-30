#!/usr/bin/env python
"""main module"""
from conversation import Conversation
from redis_utilities import erasing_data


def search_address_to_wiki(user_request, db_number=0):
    """Searched for a googleMaps address with a Wikipedia history"""
    chat_session = Conversation(user_request, db_number=db_number)
    print(
        'Grandpy response[ligne10] :'
        f"{chat_session.get_grandpy_status(chat_session.user_behavior['grandpy_code'])}"
    )
    if chat_session.user_behavior['grandpy_code'] == 'home':
        chat_session.calculate_the_incivility()
    #     if not chat_session.user_behavior['user_incivility']:
    #         chat_session.calculate_the_indecency()
    #         if not chat_session.user_behavior['user_indecency']:
    #             chat_session.calculate_the_incomprehension()
    #             if not chat_session.user_behavior['user_incomprehension']:
    #                 chat_session.calculate_the_user_entries()
    #         else:
    #             chat_session.user_behavior['grandpy_code'] = \
    #                 chat_session.__class__.NAME_GRANDPY_CODE[0]
    #             print(
    #                 'Grandpy_response[user_indecency] : '
    #                 f"{chat.get_grandpy_status(chat.user_behavior['grandpy_code'])}"
    #             )
    #     else:
    #         chat_session.user_behavior['grandpy_code'] =\
    #             chat_session.__class__.NAME_GRANDPY_CODE[0]
    #         print(
    #             'Grandpy_response[user_incivility] : '
    #             f"{chat.get_grandpy_status(chat.user_behavior['grandpy_code'])}"
    #         )
    # #  chat_session.calculate_the_user_entries()
    chat_session.update_database(db_number=db_number)
    return chat_session


if __name__ == '__main__':
    erasing_data(0)
    chat = search_address_to_wiki('openClassrooms')
    while not chat.user_behavior['fatigue_quotas']:
        chat1 = search_address_to_wiki('openClassrooms')
        chat = chat1
        print(f'\nuser_behavior[main_fin] = {chat1.user_behavior}')
