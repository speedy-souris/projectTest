#!/usr/bin/env python
"""module for managing the Redis database"""
import redis


def get_database_access(db_number=0):
    """method for data_connection to the database
       db_number arg = 0 ==> Redis connect 'dev'
       db_number arg = 1 ==> Redis connect 'test'"""
    redis_connect = redis.Redis(
        host='localhost',
        port=6379,
        db=db_number
    )
    return redis_connect


def value_to_string_conversion(script_value):
    """conversion from script_value to string"""
    return str(script_value)


def byte_to_value_conversion(string_value):
    """conversion from string to boolean"""
    string_value = string_value.decode()  # byte to string
    try:
        string_value = int(string_value)
    except ValueError:
        pass
    if string_value == 'False':
        string_value = False
    elif string_value == 'True':
        string_value = True
    return string_value


def write_access_conversation_data(name_user_behavior, value_user_behavior, db_number):
    """writing data to the database"""
    chat_access = get_database_access(db_number=db_number)
    chat_access.set(name_user_behavior, value_to_string_conversion(value_user_behavior))


def read_access_conversation_data(name_user_behavior, db_number):
    """reading data from the database"""
    chat_access = get_database_access(db_number=db_number)
    data_conversion = byte_to_value_conversion(chat_access.get(name_user_behavior))
    return data_conversion


def erasing_data(db_number):
    """data erasure redis"""
    db_redis = get_database_access(db_number)
    for key in db_redis.keys('*'):
        db_redis.delete(key)


def data_expiration(db_number):
    """expiration of the fatigue_quotas data for a theoretical duration of 24h00
    which simulates the well-deserved rest of grandpy ==> real duration for the tests 60 seconds"""
    db_redis = get_database_access(db_number)
    db_redis.expire('fatigue_quotas', 60)


if __name__ == '__main__':
    pass
