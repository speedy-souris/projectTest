#!/usr/bin/env python

from redis_utilities import read_access_conversation_data
from conversation import Conversation


def test_redis_writing():
    Conversation.database_init_ordered(1)
    chat_session = Conversation('bonjour', db_number=1)
    chat_session.calculate_the_incivility(1)
    assert chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] ==\
        'user_question'
    chat_session.update_database(1)
    assert read_access_conversation_data('grandpy_status_code', 1) == 'user_question'


