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

    def test_calculate_the_incomprehension_status(self, monkeypatch):
        expected_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_result))

        assert expected_result == google_api.get_placeid_from_address('hsdfklhdsfklh')
        assert expected_result == google_api.get_placeid_from_address('')
        assert expected_result == google_api.get_placeid_from_address('Bonjour')

    #@pytest.mark.skip()
    def test_get_request_parser(self):
        user_request = Conversation('ou se trouve openClassrooms', database_redis_number=1)
        user_request.get_user_request_parser()
        user_entry = user_request.parsed_user_entry
        assert user_entry == 'openClassrooms'
