import pytest
from ..src.redis_utilities import read_access_conversation_data
from . import erasing_data
from . import Conversation
from ..src.counting_behaviour import user_incivility_count
from . import get_user_presentation_management


# @pytest.mark.skip()
class TestWritingRedis:
    @staticmethod
    def setup_method():
        erasing_data(1)

    def test_redis_writing(self):
        chat_session = Conversation('bonjour', 1)
        get_user_presentation_management(chat_session, 'presentation', 'indecency')

        assert chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == 'benevolent'

        chat_session.update_database()
        assert read_access_conversation_data('grandpy_status_code', 1) == 'benevolent'

    def test_redis_writing_incivility(self):
        chat_session = Conversation('openClassroom', 1)
        chat_session.calculate_the_incivility_status()
        user_incivility_count(chat_session)

        assert chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('number_of_user_incivility')] == 1

        chat_session.update_database()
        assert read_access_conversation_data('number_of_user_incivility', 1) == 1
