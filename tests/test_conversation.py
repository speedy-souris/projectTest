import requests
from . import pytest
from . import RedisDataManagement
from . import Conversation
from . import google_api
from . import get_mockreturn
# from . import BehaviorParams


# @pytest.mark.skip()
class TestBehaviorParams:
    def setup_method(self):
        self.db_session = RedisDataManagement(database_redis_number=1)
        self.db_session.erasing_redis_databases()
        self.conversation = Conversation('', database_redis_number=1)

    

    # ~ #@pytest.mark.skip()
    def test_database_init_by_default(self):
        self.conversation.database_init_by_default()
        expected_result = self.db_session.read_access_conversation_data('number_of_user_entries')
        assert expected_result == b'0'

    
    #@pytest.mark.skip()
    def test_update_database(self):
        self.conversation.number_of_user_entries = 7
        self.conversation.update_database()
        expected_result = self.db_session.read_access_conversation_data('number_of_user_entries')
        assert expected_result == b'7'

    #@pytest.mark.skip()
    def test_get_request_parser(self):
        user_request = Conversation('ou se trouve openClassrooms', database_redis_number=1)
        user_request.get_user_request_parser()
        user_entry = user_request.parsed_user_entry
        assert user_entry == 'openClassrooms'
