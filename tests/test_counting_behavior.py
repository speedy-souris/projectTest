from . import pytest
from . import RedisDataManagement
from . import Conversation
from . import counting_behavior


# @pytest.mark.skip()
class TestCounting:
    def setup_method(self):
        self.db_session = RedisDataManagement(database_redis_number=1)
        self.db_session.erasing_redis_databases()
        self.chat_session = Conversation('', self.db_session)

    
    # @pytest.mark.skip()
    def test_user_question_answer_count_1_to_10(self):
        counting_behavior.user_question_answer_count(self.chat_session)
        expected_result = self.chat_session.number_of_user_entries
        assert expected_result == 1

        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        expected_result = self.chat_session.number_of_user_entries
        assert expected_result == 10
