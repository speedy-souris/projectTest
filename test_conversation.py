#!/usr/bin/env python
import requests
from mock_api import get_mockreturn
from conversation import Conversation


def test_lower_and_split_user_entry():
    Conversation.database_init(1)
    user_request = Conversation('Bonjour', db_number=1)
    expected_result = ['bonjour']
    result = user_request.lower_and_split_user_entry()
    assert expected_result == result


def test_calculate_the_incivility():
    Conversation.database_init(1)
    user_request = Conversation('Bonjour', db_number=1)
    expected_result = (False, 0, False)
    result = user_request.calculate_the_incivility()
    assert expected_result == result


def test_calculate_the_indecency():
    Conversation.database_init(1)
    user_request = Conversation('vieux', db_number=1)
    expected_result = (True, 1, False)
    result = user_request.calculate_the_indecency()
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
    result = incomprehensible_user.calculate_the_incomprehension()
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
    result = incomprehensible_user.calculate_the_incomprehension()
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
    result = incomprehensible_user.calculate_the_incomprehension()
    assert expected_result == result
