#!/usr/bin/env python
import pytest
from redis_utilities import read_access_conversation_data, erasing_data
from conversation import Conversation


# @pytest.mark.skip()
class TestWritingRedis:
    @staticmethod
    def setup_method():
        erasing_data(1)

    def test_redis_writing(self):
        chat_session = Conversation('bonjour', 1)
        chat_session.calculate_the_incivility()

        assert chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(4)] ==\
            'benevolent'
        # ------------------------------------------------------------------------------------------
        chat_session.update_database()

        assert read_access_conversation_data('grandpy_status_code', 1) == 'benevolent'

    def test_redis_writing_incivility(self):
        chat_session = Conversation('openClassroom', 1)
        chat_session.calculate_the_incivility()

        assert chat_session.user_behavior[chat_session.__class__.get_user_behavior_key(5)] == 1
        # ------------------------------------------------------------------------------------------
        chat_session.update_database()

        assert read_access_conversation_data('number_of_user_incivility', 1) == 1
