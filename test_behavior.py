#!/usr/bin/env python
import requests
from mock_api import get_mockreturn
from main import search_address_to_wiki


def teardown_method():
    Conversation.database_init(1)


class TestBehavior:

    def test_number_incivility_max(self):
        expected_result = (True, 3, True)
        search_address_to_wiki('openClassrooms')
        search_address_to_wiki('openClassrooms')
        search_address_to_wiki('openClassrooms')
        user_request = search_address_to_wiki('openClassrooms')
        result = (
            user_request.user_behavior['user_incivility'],
            user_request.user_behavior['number_of_incivility'],
            user_request.user_behavior['fatigue_quotas']
        )
        assert expected_result == result

    def test_number_indecency_max(self):
        expected_result = (True, 3, True)
        search_address_to_wiki('vieux')
        search_address_to_wiki('vieux')
        search_address_to_wiki('vieux')
        user_request = search_address_to_wiki('vieux')
        result = (
            user_request.user_behavior['user_indecency'],
            user_request.user_behavior['number_of_indecency'],
            user_request.user_behavior['fatigue_quotas']
        )
        assert expected_result == result

    def test_number_incomprehension_max(self, monkeypatch):
        expected_mock_result = {
            'candidates': [],
            'status': 'ZERO_RESULTS'
        }
        expected_result = (True, 3, True)
        mock_result = expected_mock_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        search_address_to_wiki('gjegruiotuygtugyt')
        search_address_to_wiki('gjegruiotuygtugyt')
        search_address_to_wiki('gjegruiotuygtugyt')
        incomprehensible_user = search_address_to_wiki('gjegruiotuygtugyt')
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
