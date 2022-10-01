#!/usr/bin/env python
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

    def erasing_data(self) -> None:
        """data erasure redis"""
        self.db_session.flushall()

    def data_expiration(self, has_fatigue_quotas_of_grandpy) -> None:
        """expiration of the fatigue_quotas_of_grandpy data for a theoretical duration of 24h00
        which simulates the well-deserved rest of grandpy
        ==> real duration for the tests 120 seconds"""
        self.db_session.expire(has_fatigue_quotas_of_grandpy, 120)

    def scan_database_redis(self) -> list:
        """scan all values of the redis database"""
        data_redis = self.db_session.keys('*')
        return data_redis

    def write_database_encoding(self, key_value, data_value) -> None:
        """Write data encoded in the database """
        self.db_session.set(key_value, data_value)

    def read_access_conversation_data(self, name_user_behavior) -> dict:
        """reading data from the database"""
        value_user_behavior = self.db_session.get(name_user_behavior)
        return value_user_behavior


if __name__ == '__main__':
    pass
