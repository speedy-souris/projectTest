#!/usr/bin/env python
import requests
from mock_api import get_mockreturn
from conversation import Conversation
from redis_utilities import erasing_data
import pytest


# @pytest.mark.skip()
class TestConversation:
    @staticmethod
    def setup_method():
        erasing_data(1)

    def test_lower_and_split_user_entry(self):
        user_request = Conversation('Bonjour', 1)
        expected_result = ['bonjour']
        result = user_request.lower_and_split_user_entry()
        assert expected_result == result

    def test_calculate_the_incivility_to_False(self):
        user_request = Conversation('Bonjour', 1)
        user_request.calculate_the_incivility()

        has_user_incivility_status =\
            user_request.user_behavior[user_request.get_user_behavior_key(0)]
        number_of_user_incivility =\
            user_request.user_behavior[user_request.get_user_behavior_key(5)]
        assert (has_user_incivility_status, number_of_user_incivility) == (False, 0)

    def test_calculate_the_incivility_to_True(self):
        user_request = Conversation('openClassrooms', 1)
        user_request.calculate_the_incivility()

        has_user_incivility_status =\
            user_request.user_behavior[user_request.get_user_behavior_key(0)]
        number_of_user_incivility =\
            user_request.user_behavior[user_request.get_user_behavior_key(5)]
        assert (has_user_incivility_status, number_of_user_incivility) == (True, 1)

    def test_calculate_the_indecency_to_False(self):
        user_request = Conversation('bonjour', 1)
        user_request.calculate_the_indecency()

        has_user_indecency_status =\
            user_request.user_behavior[user_request.get_user_behavior_key(1)]
        number_of_user_indecency =\
            user_request.user_behavior[user_request.get_user_behavior_key(6)]
        assert (has_user_indecency_status, number_of_user_indecency) == (False, 0)

    def test_calculate_the_indecency_to_True(self):
        user_request = Conversation('vieux', 1)
        user_request.calculate_the_indecency()

        has_user_indecency_status =\
            user_request.user_behavior[user_request.get_user_behavior_key(1)]
        number_of_user_indecency =\
            user_request.user_behavior[user_request.get_user_behavior_key(6)]
        assert (has_user_indecency_status, number_of_user_indecency) == (True, 1)

    def test_calculate_the_incomprehension(self, monkeypatch):
        incomprehensible_user = Conversation('gjegruiotuygtugyt', 1)
        expected_mock_result = {'candidates': [], 'status': 'ZERO_RESULTS'}
        mock_result = expected_mock_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        incomprehensible_user.calculate_the_incomprehension()

        user_incomprehension_status = \
            incomprehensible_user.user_behavior[incomprehensible_user.get_user_behavior_key(2)]
        number_of_user_incomprehension = \
            incomprehensible_user.user_behavior[incomprehensible_user.get_user_behavior_key(7)]
        assert (user_incomprehension_status, number_of_user_incomprehension) == (True, 1)
        # ------------------------------------------------------------------------------------------
        incomprehensible_user = Conversation('1255871436', 1)
        expected_mock_result = {'candidates': [], 'status': 'ZERO_RESULTS'}
        mock_result = expected_mock_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        incomprehensible_user.calculate_the_incomprehension()

        user_incomprehension_status = \
            incomprehensible_user.user_behavior[incomprehensible_user.get_user_behavior_key(2)]
        number_of_user_incomprehension = \
            incomprehensible_user.user_behavior[incomprehensible_user.get_user_behavior_key(7)]
        assert (user_incomprehension_status, number_of_user_incomprehension) == (True, 1)
        # ------------------------------------------------------------------------------------------
        incomprehensible_user = Conversation('', 1)
        expected_mock_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        mock_result = expected_mock_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        incomprehensible_user.calculate_the_incomprehension()

        user_incomprehension_status = \
            incomprehensible_user.user_behavior[incomprehensible_user.get_user_behavior_key(2)]
        number_of_user_incomprehension = \
            incomprehensible_user.user_behavior[incomprehensible_user.get_user_behavior_key(7)]
        assert (user_incomprehension_status, number_of_user_incomprehension) == (True, 1)

    def test_get_request_parser(self):
        user_request = Conversation('ou se trouve openClassrooms', 1)
        expected_result = user_request.get_request_parser()

        assert expected_result == 'openClassrooms'
