#!/usr/bin/env python
import requests
from mock_api import get_mockreturn
from conversation import Conversation


def teardown_method():
    Conversation.database_init(1)


class TestBehavior:

    def test_number_incivility_max(self):
        user_request = Conversation('openClassroom', db_number=1)
        expected_result = (True, 3, True)
        user_request.calculate_the_incivility()
        user_request.calculate_the_incivility()
        user_request.calculate_the_incivility()
        user_request.calculate_the_incivility()
        result = (
            user_request.user_behavior['user_incivility'],
            user_request.user_behavior['number_of_incivility'],
            user_request.user_behavior['fatigue_quotas']
        )
        assert expected_result == result

    def test_number_indecency_max(self):
        user_request = Conversation('vieux', db_number=1)
        expected_result = (True, 3, True)
        user_request.calculate_the_indecency()
        user_request.calculate_the_indecency()
        user_request.calculate_the_indecency()
        user_request.calculate_the_indecency()
        result = (
            user_request.user_behavior['user_indecency'],
            user_request.user_behavior['number_of_indecency'],
            user_request.user_behavior['fatigue_quotas']
        )
        assert expected_result == result

    def test_number_incomprehension_max(self, monkeypatch):
        incomprehensible_user = Conversation('gjegruiotuygtugyt', db_number=1)
        expected_mock_result = {
            'candidates': [],
            'status': 'ZERO_RESULTS'
        }
        expected_result = (True, 3, True)
        mock_result = expected_mock_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        incomprehensible_user.calculate_the_incomprehension()
        incomprehensible_user.calculate_the_incomprehension()
        incomprehensible_user.calculate_the_incomprehension()
        incomprehensible_user.calculate_the_incomprehension()
        result = (
            incomprehensible_user.user_behavior['user_incomprehension'],
            incomprehensible_user.user_behavior['number_of_incomprehension'],
            incomprehensible_user.user_behavior['fatigue_quotas']
        )
        assert expected_result == result

    def test_get_grandpy_status(self):
        user_request = Conversation('bonjour', db_number=1)
        expected_message = 'home'
        user_request.get_grandpy_status()
        result = user_request.user_behavior['grandpy_code']
        assert expected_message == result

    def test_grandpy_code(self):
        user_request = Conversation('bonjour', db_number=1)
        expected_message = "Bonjour Mon petit, en quoi puis-je t'aider ?"
        user_request.get_grandpy_status()
        grandpy_code = user_request.user_behavior['grandpy_code']
        result = user_request.GRANDPY_CODE[grandpy_code]
        assert expected_message == result

    def test_number_request_max(self, monkeypatch):
        user_request = Conversation('openClassroom', db_number=1)
        user_request.calculate_the_incivility()
        expected_mock_result = {
            'candidates': [],
            'status': 'ZERO_RESULTS'
        }
        expected_result = (False, False, 10, True)
        mock_result = expected_mock_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        user_request.calculate_the_user_entries()
        user_request.calculate_the_user_entries()
        user_request.calculate_the_user_entries()
        user_request.calculate_the_user_entries()
        user_request.calculate_the_user_entries()
        user_request.calculate_the_user_entries()
        user_request.calculate_the_user_entries()
        user_request.calculate_the_user_entries()
        user_request.calculate_the_user_entries()
        user_request.calculate_the_user_entries()
        user_request.calculate_the_user_entries()
        result = (
            user_request.user_behavior['user_indecency'],
            user_request.user_behavior['user_incomprehension'],
            user_request.user_behavior['number_of_user_entries'],
            user_request.user_behavior['fatigue_quotas']
        )
        assert expected_result == result
