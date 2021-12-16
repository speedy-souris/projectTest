#!/usr/bin/env python
import requests
from mock_api import get_mockreturn
from conversation import Conversation


def initialisation():
    return Conversation.database_and_class_init(1)


def test_lower_and_split_user_entry():
    initialisation()
    user_request = Conversation('Bonjour', db_number=1)
    expected_result = ['bonjour']
    result = user_request.lower_and_split_user_entry()
    assert expected_result == result


def test_calculate_the_incivility():
    initialisation()
    user_request = Conversation('Bonjour', db_number=1)
    expected_result = (False, 0, False)
    user_request.calculate_the_incivility()
    result = (
        user_request.is_user_incivility,
        user_request.number_of_incivility,
        user_request.IS_FATIGUE_QUOTAS_IN_CONVERSATION
    )
    assert expected_result == result


def test_calculate_the_indecency():
    initialisation()
    user_request = Conversation('vieux', db_number=1)
    expected_result = (True, 1, False)
    user_request.calculate_the_indecency()
    result = (
        user_request.is_user_indecency,
        user_request.number_of_indecency,
        user_request.IS_FATIGUE_QUOTAS_IN_CONVERSATION
    )
    assert expected_result == result


def test_calculate_the_incomprehension(monkeypatch):
    incomprehensible_user = Conversation('gjegruiotuygtugyt', db_number=1)
    expected_mock_result = {
        'candidates': [],
        'status': 'ZERO_RESULTS'
    }
    expected_result = (True, 1, False)
    mock_result = expected_mock_result
    mockreturn = get_mockreturn(mock_result)
    monkeypatch.setattr(requests, 'get', mockreturn)
    incomprehensible_user.calculate_the_incomprehension()
    result = (
        incomprehensible_user.is_user_incomprehension,
        incomprehensible_user.number_of_incomprehension,
        incomprehensible_user.IS_FATIGUE_QUOTAS_IN_CONVERSATION
    )
    assert expected_result == result
    incomprehensible_user = Conversation('1255871436', db_number=1)
    expected_mock_result = {
        'candidates': [],
        'status': 'ZERO_RESULTS'
    }
    expected_result = (True, 1, False)
    mock_result = expected_mock_result
    mockreturn = get_mockreturn(mock_result)
    monkeypatch.setattr(requests, 'get', mockreturn)
    incomprehensible_user.calculate_the_incomprehension()
    result = (
        incomprehensible_user.is_user_incomprehension,
        incomprehensible_user.number_of_incomprehension,
        incomprehensible_user.IS_FATIGUE_QUOTAS_IN_CONVERSATION
    )
    assert expected_result == result
    incomprehensible_user = Conversation('', db_number=1)
    expected_mock_result = {
        'candidates': [],
        'status': 'INVALID_REQUEST'
    }
    expected_result = (True, 1, False)
    mock_result = expected_mock_result
    mockreturn = get_mockreturn(mock_result)
    monkeypatch.setattr(requests, 'get', mockreturn)
    incomprehensible_user.calculate_the_incomprehension()
    result = (
        incomprehensible_user.is_user_incomprehension,
        incomprehensible_user.number_of_incomprehension,
        incomprehensible_user.IS_FATIGUE_QUOTAS_IN_CONVERSATION
    )
    assert expected_result == result


def test_get_request_parser():
    user_request = Conversation('ou se trouve openClassrooms', db_number=1)
    expected_result = 'openClassrooms'
    result = user_request.get_request_parser()
    assert expected_result == result
