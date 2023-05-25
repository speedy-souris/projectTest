from . import pytest
from . import RedisDataManagement
from . import Conversation


# @pytest.mark.skip()
class TestWritingRedis:
    def setup_method(self):
        self.db_session = RedisDataManagement(database_redis_number=1)
        self.db_session.erasing_redis_databases()
        self.db_session.redis_database_init_by_default()
        self.conversation = Conversation('')
        # self.chat_session = main('', database_redis_number=1)

    def test_byte_to_int_conversion(self):
        expected_result = self.db_session.byte_to_int_conversion(b'5')
        assert expected_result == 5

    # @pytest.mark.skip()
    def test_byte_to_boolean_conversion(self):
        expected_result = self.db_session.byte_to_boolean_conversion(b'False')
        assert not expected_result

    # @pytest.mark.skip()
    def test_byte_to_string_conversion(self):
        expected_result = self.db_session.byte_to_string_conversion(b'response_limit')
        assert expected_result == 'response_limit'

    def test_string_to_byte(self):
        expected_result = self.db_session.decode_string_to_byte('home')
        expected_result_bool = self.db_session.decode_string_to_byte(True)
        assert expected_result == b'home'
        assert expected_result_bool == b'True'

    def test_decode_int_to_byte(self):
        expected_result = self.db_session.decode_int_to_byte(2)
        assert expected_result == b'2'

    #@pytest.mark.skip()
    def test_database_init_by_default(self):
        expected_result = self.db_session.read_redis_database_decoding('number_of_user_entries')
        assert expected_result == b'0'

    #@pytest.mark.skip()
    def test_update_database(self):
        self.conversation.number_of_user_entries = 7
        self.db_session.update_redis_database(self.conversation)
        expected_result = self.db_session.read_redis_database_decoding('number_of_user_entries')
        assert expected_result == b'7'

    # @pytest.mark.skip()
    def test_write_redis_database_encoding(self):
        self.db_session.write_redis_database_encoding('has_user_incivility_status', b'True')
        expected_result = \
            self.db_session.byte_to_boolean_conversion(
                self.db_session.read_redis_database_decoding('has_user_incivility_status'))
        assert expected_result
