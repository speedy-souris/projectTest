#!/usr/bin/env python
"""module for managing the Redis database"""
import redis


def get_database_access(db_number=0):
    """method for data_connection to the database
       db_number arg = 0 ==> Redis connect 'dev'
       db_number arg = 1 ==> Redis connect 'test'"""
    redis_connect = redis.Redis(host='localhost', port=6379, db=db_number)
    return redis_connect


def erasing_data(db_session):
    """data erasure redis"""
    db_session.flushall()


def data_expiration(has_fatigue_quotas_of_grandpy, db_session):
    """expiration of the fatigue_quotas_of_grandpy data for a theoretical duration of 24h00
    which simulates the well-deserved rest of grandpy ==> real duration for the tests 120 seconds"""
    db_session.expire(has_fatigue_quotas_of_grandpy, 120)


def scan_database_redis(db_session):
    """scan all values of the redis database"""
    return db_session.keys('*')


def value_to_string_conversion(script_value):
    """conversion from value to string"""
    return str(script_value)


def byte_to_int_conversion(script_value):
    """conversion from byte value to integer"""
    return int.from_bytes(script_value, 'little')


def byte_to_boolean_conversion(script_value):
    """conversion from byte value to boolean"""
    string_value = ''
    if script_value == value_to_string_conversion(b'False'):
        string_value = False
    elif script_value == value_to_string_conversion(b'True'):
        string_value = True
    return string_value


def decode_value_to_byte(chat_session):
    """recovery of attribute values and conversion to byte"""
    byte_value = {}
    bool_reference = {
        'has_user_incivility_status': chat_session.has_user_incivility_status,
        'has_user_indecency_status': chat_session.has_user_indecency_status,
        'has_user_incomprehension_status': chat_session.has_user_incomprehension_status,
        'has_fatigue_quotas_of_grandpy': chat_session.has_fatigue_quotas_of_grandpy}
    int_reference = {
        'level': chat_session.level,
        'number_of_user_incivility': chat_session.number_of_user_incivility,
        'number_of_user_indecency': chat_session.number_of_user_indecency,
        'number_of_user_incomprehension': chat_session.number_of_user_incomprehension,
        'number_of_user_entries': chat_session.number_of_user_entries}
    string_reference = {'grandpy_status_code': chat_session.grandpy_status_code}
    print(f'int_reference [tobyte_redis] = {int_reference}')
    for name, value in bool_reference.items():
        byte_value[name] = bytes(value_to_string_conversion(value), 'utf-8')
    for name, value in int_reference.items():
        byte_value[name] = value_to_string_conversion(value).encode()
    for name, value in string_reference.items():
        byte_value[name] = bytes(value, 'utf-8')
    print(f'dict_bayte [redis]= {byte_value}')
    return byte_value


def decode_byte_to_value(db_session):
    """retrieving byte values from the database and converting them
    into a character string, boolean or numeric value"""
    value = {}
    string_reference = {
        'grandpy_status_code': db_session.get('grandpy_status_code')}
    boolean_reference = {
        'has_user_incivility_status': db_session.get('has_user_incivility_status'),
        'has_user_indecency_status': db_session.get('has_user_indecency_status'),
        'has_user_incomprehension_status': db_session.get('has_user_incomprehension_status'),
        'has_fatigue_quotas_of_grandpy': db_session.get('has_fatigue_quotas_of_grandpy')}
    int_reference = {
        'level': db_session.get('level'),
        'number_of_user_incivility': db_session.get('number_of_user_incivility'),
        'number_of_user_indecency': db_session.get('number_of_user_indecency'),
        'number_of_user_incomprehension': db_session.get('number_of_user_incomprehension'),
        'number_of_user_entries': db_session.get('number_of_user_entries')}
    for name, byte in string_reference.items():
        value[name] = value_to_string_conversion(byte)
    for name, byte in boolean_reference.items():
        value[name] = byte_to_boolean_conversion(byte)
    for name, byte in int_reference.items():
        value[name] = byte_to_int_conversion(byte)
    return value


def write_access_conversation_data(name_user_behavior, chat_session, db_session):
    """writing data to the database"""
    value = decode_value_to_byte(chat_session)
    print(f'\nvalue["names_user_behavior"] = {value[name_user_behavior]}')
    db_session.set(name_user_behavior, value[name_user_behavior])


def read_access_conversation_data(name_user_behavior, db_session):
    """reading data from the database"""
    value_user_behavior = decode_byte_to_value(db_session)
    return value_user_behavior[name_user_behavior]


if __name__ == '__main__':
    pass
