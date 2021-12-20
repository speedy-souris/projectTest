#!/usr/bin/env python
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


def byte_to_value_conversion(string_value, name_grandpy_code):
    """conversion from string to boolean"""
    if string_value == b'False':
        string_value = False
    elif string_value == b'True':
        string_value = True
    elif string_value in b'01235789':
        string_value = int(string_value)
    else:
        for value in name_grandpy_code:
            if string_value in value:
                string_value = value
    return string_value


def write_access_conversation_data(name_user_behavior, value_user_behavior, db_number):
    """writing data to the database"""
    chat_access = get_database_access(db_number=db_number)
    chat_access.set(name_user_behavior, value_to_string_conversion(value_user_behavior))


def read_access_conversation_data(name_user_behavior, name_grandpy_code, db_number):
    """reading data from the database"""
    chat_access = get_database_access(db_number=db_number)
    name_user_behavior =\
        byte_to_value_conversion(chat_access.get(name_user_behavior), name_grandpy_code)
    return name_user_behavior
