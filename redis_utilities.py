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

def boolean_to_string_conversion(boolean_value):
    """conversion from boolean to string"""
    if boolean_value:
        boolean_value = 'True'
    else:
        boolean_value = 'False'
    return boolean_value

def string_to_boolean_conversion(string_value):
    """conversion from string to boolean"""
    if string_value == b'False':
        string_value = False
    elif string_value == b'True':
        string_value = True
    else:
        string_value = False
    return string_value

def string_to_int_conversion(string_value):
    """conversion from string to integer"""
    return int(string_value)


def write_access_conversation_data(name_user_behavior, value_user_behavior, db_number):
    """writing data to the database"""
    chat_access = get_database_access(db_number=db_number)
    if type(value_user_behavior) == bool:
        value = boolean_to_string_conversion(value_user_behavior)
    else:
        value = value_user_behavior
    chat_access.set(name_user_behavior, value)


def read_access_conversation_data(name_user_behavior, db_number):
    """reading data from the database"""
    chat_access = get_database_access(db_number=db_number)
    if 'number' in name_user_behavior:
        data_value = string_to_int_conversion(chat_access.get(name_user_behavior))
    else:
        data_value = string_to_boolean_conversion(chat_access.get(name_user_behavior))
    return data_value
