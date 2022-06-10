from . import pytest
from ..src.redis_utilities import read_access_conversation_data
from ..src.redis_utilities import write_access_conversation_data
from . import erasing_data


# @pytest.mark.skip()
class TestWritingRedis:
    @staticmethod
    def setup_method():
        erasing_data(1)

    @staticmethod
    def teardown_method():
        erasing_data(1)

    @pytest.mark.parametrize(
        "data, value", [('has_user_incivility', False), ('has_user_indecency', True),
                        ('has_user_incomprehension', False), ('number_of_user_incivility', 2),
                        ('behavior_level', 'chat_session'), ('number_of_user_entries', 7)])
    def test_data_exchange_in_redis(self, data, value):
        write_access_conversation_data(data, value, 1)

        assert read_access_conversation_data(data, 1) == value
