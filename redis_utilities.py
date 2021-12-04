#!/usr/bin/env python
"""conversation data management menu"""
import redis


def get_access_database(db_number: int = 0) -> object:
    """method for data_connection to the database
    db_number arg = 0 ==> Redis connect 'dev'
    db_number arg = 1 ==> Redis connect 'test'"""
    redis_connect = redis.Redis(
        host='localhost',
        port=6379,
        db=db_number
    )
    return redis_connect


def boolean_to_string_conversion(boolean_value: bool) -> str:
    """conversion from boolean to string"""
    if boolean_value:
        value = 'True'
    else:
        value = 'False'
    return value


def string_to_boolean_conversion(string_value: str) -> bool:
    """conversion from string to boolean"""
    if string_value == b'False':
        value = False
    elif string_value == b'True':
        value = True
    else:
        value = False
    return value


def string_to_int_conversion(string_value: str) -> int:
    """conversion from string to integer"""
    return int(string_value)


def read_access_conversation_data(db_data: str, db_number: int = 0) -> str:
    """reading the value of conversation in db_data"""
    chat_dbaccess = get_access_database(db_number=db_number)
    return chat_dbaccess.get(db_data)


def write_access_conversation_data(db_data: str, db_data_value: str, db_number: int = 0):
    """writing the value of conversation in db_data"""
    chat_dbaccess = get_access_database(db_number=db_number)
    chat_dbaccess.set(db_data, db_data_value)
