"""module for managing the Redis database"""
import redis


class RedisDataManagement:
    """behavioral management of redis"""
    def __init__(self, db_number=0):
        self.db_session = self.get_database_access(db_number=db_number)

    @staticmethod
    def get_database_access(db_number) -> object:
        """method for data_connection to the database
            db_number arg = 0 ==> Redis connect 'dev'
            db_number arg = 1 ==> Redis connect 'test'"""
        redis_connect = redis.Redis(host='localhost', port=6379, db=db_number)
        return redis_connect

    @staticmethod
    def byte_to_string_conversion(script_value) -> str:
        """conversion from byte to string"""
        string_value = ''
        if script_value is not None:
            string_value = script_value.decode()
        return string_value

    def byte_to_int_conversion(self, script_value) -> int:
        """conversion from byte value to integer"""
        int_value = 0
        if script_value is not None:
            int_value = int(self.byte_to_string_conversion(script_value))
        return int_value

    @staticmethod
    def byte_to_boolean_conversion(script_value) -> bool:
        """conversion from byte value to boolean"""
        bool_value = ''
        if script_value == b'False':
            bool_value = False
        elif script_value == b'True':
            bool_value = True
        return bool_value

    @staticmethod
    def decode_string_to_byte(data_value) -> bytes:
        """recovery of attribute string and conversion to byte"""
        byte_value = bytes(str(data_value), 'utf-8')
        return byte_value

    @staticmethod
    def decode_int_to_byte(data_value) -> bytes:
        """recovery of attribute integer and conversion to byte"""
        byte_value = str(data_value).encode()
        return byte_value

    def database_init_by_default(self) -> None:
        """initialization of redis database
        with a key, its value and the ID of the redis database
        example :
        redis_utilities.write_access_conversation_data ('grandpy_status_code', 'home', 0)"""
        print("Initialisation REDIS")
        init_data_redis = {
            'has_user_incivility_status': self.decode_string_to_byte(False),
            'has_user_indecency_status': self.decode_string_to_byte(False),
            'has_user_incomprehension_status': self.decode_string_to_byte(False),
            'has_fatigue_quotas_of_grandpy': self.decode_string_to_byte(False),
            'level': self.decode_int_to_byte(1),
            'number_of_user_incivility': self.decode_int_to_byte(0),
            'number_of_user_indecency': self.decode_int_to_byte(0),
            'number_of_user_incomprehension': self.decode_int_to_byte(0),
            'number_of_user_entries': self.decode_int_to_byte(0),
            'grandpy_status_code': self.decode_string_to_byte('home')}
        for name_init, data_init in init_data_redis.items():
            self.write_database_encoding(name_init, data_init)

    def update_database(self, chat_session) -> None:
        """after all data processing update redis database with local attributes"""
        has_user_incivility_status = \
            self.decode_string_to_byte(chat_session.has_user_incivility_status)
        has_user_indecency_status = \
            self.decode_string_to_byte(chat_session.has_user_indecency_status)
        has_user_incomprehension_status = \
            self.decode_string_to_byte(chat_session.has_user_incomprehension_status)
        has_fatigue_quotas_of_grandpy = \
            self.decode_string_to_byte(chat_session.has_fatigue_quotas_of_grandpy)
        grandpy_status_code = self.decode_string_to_byte(chat_session.grandpy_status_code)
        level = self.decode_int_to_byte(chat_session.level)
        number_of_user_incivility = \
            self.decode_int_to_byte(chat_session.number_of_user_incivility)
        number_of_user_indecency = \
            self.decode_int_to_byte(chat_session.number_of_user_indecency)
        number_of_user_incomprehension = \
            self.decode_int_to_byte(chat_session.number_of_user_incomprehension)
        number_of_user_entries = \
            self.decode_int_to_byte(chat_session.number_of_user_entries)

        attribut_value = {
            'has_user_incivility_status': has_user_incivility_status,
            'has_user_indecency_status': has_user_indecency_status,
            'has_user_incomprehension_status': has_user_incomprehension_status,
            'grandpy_status_code': grandpy_status_code,
            'level': level,
            'number_of_user_incivility': number_of_user_incivility,
            'number_of_user_indecency': number_of_user_indecency,
            'number_of_user_incomprehension': number_of_user_incomprehension,
            'number_of_user_entries': number_of_user_entries}
        for name_update, data_update in attribut_value.items():
            self.write_database_encoding(name_update, data_update)
        if chat_session.previous_has_fatigue_quotas_of_grandpy != \
            chat_session.has_fatigue_quotas_of_grandpy:
            self.write_database_encoding(
                'has_fatigue_quotas_of_grandpy', self.decode_string_to_byte(
                    chat_session.has_fatigue_quotas_of_grandpy))
            self.data_expiration()

    def erasing_data(self) -> None:
        """data erasure redis"""
        self.db_session.flushall()

    def data_expiration(self) -> None:
        """expiration of the fatigue_quotas_of_grandpy data for a theoretical duration of 24h00
        which simulates the well-deserved rest of grandpy
        ==> real duration for the tests 120 seconds"""
        # ~ if self.db_session.ttl('has_fatigue_quotas_of_grandpy') == -1:
        self.db_session.expire('has_fatigue_quotas_of_grandpy', 120)

    def scan_database_redis(self) -> list:
        """scan all values of the redis database"""
        data_redis = self.db_session.keys('*')
        return data_redis

    def write_database_encoding(self, key_value, data_value) -> None:
        """Write data encoded in the database """
        self.db_session.set(key_value, data_value)

    def read_access_conversation_data(
        self, name_user_behavior, default_value=None) -> dict:
        """reading data from the database"""
        try:
            value_user_behavior = self.db_session.get(name_user_behavior)
        except :
            value_user_behavior = default_value
        return value_user_behavior


if __name__ == '__main__':
    pass
