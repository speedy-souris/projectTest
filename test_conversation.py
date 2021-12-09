#!/usr/bin/env python
import requests
from conversation import Conversation
from mock_api import get_mockreturn


class TestConversation:
    def setup_method(self):
        Conversation.database_init(1)
        self.entry_bonjour = Conversation('Bonjour', db_number=1)
        self.incorrect_entry = Conversation('vieux', db_number=1)

    def test_lower_and_split_user_entry(self):
        user_request = self.entry_bonjour
        expected_result = ['bonjour']
        result = user_request.lower_and_split_user_entry()
        assert expected_result == result

    def test_calculate_the_incivility(self):
        user_request = self.entry_bonjour
        expected_result = (False, 0)
        result = user_request.calculate_the_incivility()
        assert expected_result == result

    def test_calculate_the_indecency(self):
        user_request = self.incorrect_entry
        expected_result = (True, 1)
        result = user_request.calculate_the_indecency()
        assert expected_result == result

    def test_calculate_the_incomprehension(self, monkeypatch):
        expected_result = {
            'candidates': [],
            'status': 'ZERO_RESULTS'
        }
        mock_result = expected_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        result1 = Conversation.get_placeid_from_address('gjegruiotuygtugyt')
        result2 = Conversation.get_placeid_from_address('1255871436')
        assert expected_result == result1
        assert exception_result ==  result2

        expected_result = {
            'candidates': [],
            'status': 'INVALID_REQUEST'
        }
        mock_result = expected_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        result = Conversation.get_placeid_from_address('')
        assert expected_result == result