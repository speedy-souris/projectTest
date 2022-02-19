#!/usr/bin/env python
import requests
from mock_api import get_mockreturn
from conversation import Conversation
from main import search_address_to_wiki

def setup_method():
    Conversation.database_init(1)

class TestBehavior:

    def test_number_incivility_max(self, monkeypatch):
        expected_result = {
            'html_attributions': [],
            'result': {
                'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                'geometry': {
                    'location': {'lat': 48.8975156, 'lng': 2.3833993},
                    'viewport': {
                        'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                        'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}
                    }
                }
            },
            'status': 'OK'
        }
        mock_result = expected_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
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
        expected_message = 'home'
        user_request = search_address_to_wiki('bonjour')
        result = user_request.user_behavior['grandpy_code']
        assert expected_message == result

    def test_grandpy_code(self):
        expected_message = "Bonjour Mon petit, en quoi puis-je t'aider ?"
        user_request = search_address_to_wiki('bonjour')
        grandpy_code = user_request.user_behavior['grandpy_code']
        result = user_request.GRANDPY_CODE[grandpy_code]
        assert expected_message == result

    def test_number_request_max(self, monkeypatch):
        expected_mock_result = {
            'candidates': [],
            'status': 'ZERO_RESULTS'
        }
        expected_result = (False, False, 10, True)
        mock_result = expected_mock_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        search_address_to_wiki('bonjour')
        search_address_to_wiki('openClassrooms')
        search_address_to_wiki('openClassrooms')
        search_address_to_wiki('openClassrooms')
        search_address_to_wiki('openClassrooms')
        search_address_to_wiki('openClassrooms')
        search_address_to_wiki('openClassrooms')
        search_address_to_wiki('openClassrooms')
        search_address_to_wiki('openClassrooms')
        search_address_to_wiki('openClassrooms')
        user_request = search_address_to_wiki('openClassrooms')
        result = (
            user_request.user_behavior['user_indecency'],
            user_request.user_behavior['user_incomprehension'],
            user_request.user_behavior['number_of_user_entries'],
            user_request.user_behavior['fatigue_quotas']
        )
        assert expected_result == result
