#!/usr/bin/env python
"""main module"""
from conversation import Conversation


def search_address_to_wiki(user_request, db_number=0):
    """Searched for a googleMaps address with a Wikipedia history"""
    chat_session = Conversation(user_request, db_number=db_number)
    if chat_session.user_behavior['grandpy_code'] == 'home':
        chat_session.calculate_the_incivility()
        if not chat_session.user_behavior['user_incivility']:
            chat_session.calculate_the_incivility()
            if not chat_session.user_behavior['user_indecency']:
                chat_session.calculate_the_incomprehension()
                if not chat_session.user_behavior['user_incomprehension']:
                    chat_session.calculate_the_user_entries()
            else:
                chat_session.user_behavior['grandpy_code'] = \
                    chat_session.__class__.NAME_GRANDPY_CODE[0]
        else:
            chat_session.user_behavior['grandpy_code'] =\
                chat_session.__class__.NAME_GRANDPY_CODE[0]
    chat_session.update_database(db_number=db_number)


if __name__ == '__main__':
    start = Conversation('vieux')
    search_address_to_wiki('vieux')
    print(f'\nuser_behavior[main_fin] = {start.user_behavior}')
