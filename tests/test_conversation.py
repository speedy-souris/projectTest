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

    def test_calculate_the_incivility_status(self):
        user_behavior_data_incivility = Conversation('Ou se trouve OpenClassrooms', database_redis_number=1)
        user_behavior_data_incivility.calculate_the_incivility_status()
        expected_result_data_incivility = user_behavior_data_incivility.has_user_incivility_status
        assert expected_result_data_incivility

        user_behavior_data = Conversation('Bonjour', database_redis_number=1)
        user_behavior_data.calculate_the_incivility_status()
        expected_result_data = user_behavior_data.has_user_incivility_status
        assert not expected_result_data

    def test_calculate_the_indecency_status(self):
        user_behavior_data_indecency = Conversation("hello le vieux", database_redis_number=1)
        user_behavior_data_indecency.calculate_the_indecency_status()
        expected_result_data_indecency = user_behavior_data_indecency.has_user_indecency_status

        assert expected_result_data_indecency

        user_behavior_data = Conversation('Bonjour', database_redis_number=1)
        user_behavior_data.calculate_the_indecency_status()
        expected_result_data = user_behavior_data.has_user_indecency_status
        assert not expected_result_data

    def test_calculate_the_incomprehension_status(self, monkeypatch):
        expected_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_result))

        assert expected_result == google_api.get_placeid_from_address('hsdfklhdsfklh')
        assert expected_result == google_api.get_placeid_from_address('')
        assert expected_result == google_api.get_placeid_from_address('Bonjour')

    #@pytest.mark.skip()
    # ~ def test_database_init_by_default(self):
        # ~ self.conversation.database_init_by_default()
        # ~ expected_result = self.db_session.read_access_conversation_data('number_of_user_entries')
        # ~ assert expected_result == b'0'

    #@pytest.mark.skip()
    def test_lower_and_split_user_entry(self):
        user_request = Conversation('BONJOUR', database_redis_number=1)
        expected_result = user_request.lower_and_split_user_entry()
        assert expected_result == ['bonjour']

    #@pytest.mark.skip()
    # ~ def test_update_database(self):
        # ~ self.conversation.number_of_user_entries = 7
        # ~ self.conversation.update_database()
        # ~ expected_result = self.db_session.read_access_conversation_data('number_of_user_entries')
        # ~ assert expected_result == b'7'

    #@pytest.mark.skip()
    def test_get_request_parser(self):
        user_request = Conversation('ou se trouve openClassrooms', database_redis_number=1)
        user_request.get_user_request_parser()
        user_entry = user_request.user_entry
        assert user_entry == 'openClassrooms'
