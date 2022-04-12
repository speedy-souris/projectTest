#!/usr/bin/env python

from redis_utilities import read_access_conversation_data
from conversation import Conversation


def test_redis_writing():
    Conversation('', 1).database_init_ordered()
    chat_session = Conversation('bonjour', 1)
    chat_session.calculate_the_incivility()
    assert chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] ==\
        'user_question'
    chat_session.update_database()
    assert read_access_conversation_data('grandpy_status_code', 1) == 'user_question'


def test_redis_writing_incivility():
    Conversation('', 1).database_init_ordered()
    chat_session = Conversation('openClassroom', 1)
    chat_session.calculate_the_incivility()
    assert chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(5)] == 1

    chat_session.update_database()
    assert read_access_conversation_data('number_of_user_incivility', 1) == 1

