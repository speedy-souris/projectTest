#!/usr/bin/env python
import requests
from mock_api import get_mockreturn
from conversation import Conversation


class TestConversation:
    def setup_method(self):
        Conversation('', 1).database_init_ordered()

    def test_lower_and_split_user_entry(self):
        user_request = Conversation('Bonjour', 1)

        expected_result = ['bonjour']

        result = user_request.lower_and_split_user_entry()
        assert expected_result == result

    def test_calculate_the_incivility(self):
        user_request = Conversation('Bonjour', 1)

        user_incivility_status, number_of_user_incivility, fatigue_quotas_of_grandpy =\
            False, 0, False

        expected_result = (
            user_incivility_status, number_of_user_incivility, fatigue_quotas_of_grandpy
        )

        user_request.calculate_the_incivility()

        user_incivility_status_to_false, \
            number_of_user_incivility_to_0, \
            fatigue_quotas_of_grandpy_to_false = \
            user_request.user_behavior[user_request.__class__.get_user_behavior_key(0)], \
            user_request.user_behavior[user_request.__class__.get_user_behavior_key(5)], \
            user_request.user_behavior[user_request.__class__.get_user_behavior_key(3)]

        result = (
            user_incivility_status_to_false,
            number_of_user_incivility_to_0,
            fatigue_quotas_of_grandpy_to_false
        )
        assert expected_result == result

    def test_calculate_the_incivility_to_false(self):
        user_request = Conversation('openClassrooms', 1)

        user_incivility_status, number_of_user_incivility, fatigue_quotas_of_grandpy =\
            True, 1, False

        expected_result = (
            user_incivility_status, number_of_user_incivility, fatigue_quotas_of_grandpy
        )

        user_request.calculate_the_incivility()

        user_incivility_status_to_true, \
            number_of_user_incivility_to_1, \
            fatigue_quotas_of_grandpy_to_false = \
            user_request.user_behavior[user_request.__class__.get_user_behavior_key(0)], \
            user_request.user_behavior[user_request.__class__.get_user_behavior_key(5)], \
            user_request.user_behavior[user_request.__class__.get_user_behavior_key(3)]

        result = (
            user_incivility_status_to_true,
            number_of_user_incivility_to_1,
            fatigue_quotas_of_grandpy_to_false
        )
        assert expected_result == result

    def test_calculate_the_indecency(self):
        user_request = Conversation('vieux', 1)

        user_indecency_status, number_of_user_indecency, fatigue_quotas_of_grandpy = \
            True, 1, False

        expected_result = (
            user_indecency_status, number_of_user_indecency, fatigue_quotas_of_grandpy
        )

        user_request.calculate_the_indecency()

        user_indecency_status_to_true, \
            number_of_user_indecency_to_1, \
            fatigue_quotas_of_grandpy_to_false = \
            user_request.user_behavior[user_request.get_user_behavior_key(1)], \
            user_request.user_behavior[user_request.get_user_behavior_key(6)], \
            user_request.user_behavior[user_request.get_user_behavior_key(3)]

        result = (
            user_indecency_status_to_true,
            number_of_user_indecency_to_1,
            fatigue_quotas_of_grandpy_to_false,
        )
        assert expected_result == result

    def test_calculate_the_indecency_to_false(self):
        user_request = Conversation('bonjour', 1)

        user_indecency_status, number_of_user_indecency, fatigue_quotas_of_grandpy = \
            False, 0, False

        expected_result = (
            user_indecency_status, number_of_user_indecency, fatigue_quotas_of_grandpy
        )

        user_request.calculate_the_indecency()

        user_indecency_status_to_false, \
            number_of_user_indecency_to_0, \
            fatigue_quotas_of_grandpy_to_false = \
            user_request.user_behavior[user_request.get_user_behavior_key(1)], \
            user_request.user_behavior[user_request.get_user_behavior_key(6)], \
            user_request.user_behavior[user_request.get_user_behavior_key(3)]

        result = (
            user_indecency_status_to_false,
            number_of_user_indecency_to_0,
            fatigue_quotas_of_grandpy_to_false,
        )
        assert expected_result == result

    def test_calculate_the_incomprehension(self, monkeypatch):
        incomprehensible_user = Conversation('gjegruiotuygtugyt', 1)
        expected_mock_result = {
            'candidates': [],
            'status': 'ZERO_RESULTS'
        }

        user_incomprehension_status, number_of_user_incomprehension, fatigue_quotas_of_grandpy = \
            True, 1, False

        expected_result = (
            user_incomprehension_status, number_of_user_incomprehension, fatigue_quotas_of_grandpy
        )

        mock_result = expected_mock_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)

        incomprehensible_user.calculate_the_incomprehension()

        user_incomprehension_status_to_true, \
            number_of_user_incomprehension_to_1, \
            fatigue_quotas_of_grandpy_to_false = \
            incomprehensible_user.user_behavior[incomprehensible_user.get_user_behavior_key(2)],\
            incomprehensible_user.user_behavior[incomprehensible_user.get_user_behavior_key(7)],\
            incomprehensible_user.user_behavior[incomprehensible_user.get_user_behavior_key(3)]

        result = (
            user_incomprehension_status_to_true,
            number_of_user_incomprehension_to_1,
            fatigue_quotas_of_grandpy_to_false
        )
        assert expected_result == result

        incomprehensible_user = Conversation('1255871436', 1)
        expected_mock_result = {
            'candidates': [],
            'status': 'ZERO_RESULTS'
        }

        user_incomprehension_status, number_of_user_incomprehension, fatigue_quotas_of_grandpy = \
            True, 1, False

        expected_result = (
            user_incomprehension_status, number_of_user_incomprehension, fatigue_quotas_of_grandpy
        )

        mock_result = expected_mock_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)

        incomprehensible_user.calculate_the_incomprehension()

        user_incomprehension_status_to_true, \
            number_of_user_incomprehension_to_1, \
            fatigue_quotas_of_grandpy_to_false = \
            incomprehensible_user.user_behavior[incomprehensible_user.get_user_behavior_key(2)], \
            incomprehensible_user.user_behavior[incomprehensible_user.get_user_behavior_key(7)], \
            incomprehensible_user.user_behavior[incomprehensible_user.get_user_behavior_key(3)]

        result = (
            user_incomprehension_status_to_true,
            number_of_user_incomprehension_to_1,
            fatigue_quotas_of_grandpy_to_false
        )
        assert expected_result == result

        incomprehensible_user = Conversation('', 1)
        expected_mock_result = {
            'candidates': [],
            'status': 'INVALID_REQUEST'
        }

        user_incomprehension_status, number_of_user_incomprehension, fatigue_quotas_of_grandpy = \
            True, 1, False

        expected_result = (
            user_incomprehension_status, number_of_user_incomprehension, fatigue_quotas_of_grandpy
        )

        mock_result = expected_mock_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)

        incomprehensible_user.calculate_the_incomprehension()

        user_incomprehension_status_to_true, \
            number_of_user_incomprehension_to_1, \
            fatigue_quotas_of_grandpy_to_false = \
            incomprehensible_user.user_behavior[incomprehensible_user.get_user_behavior_key(2)], \
            incomprehensible_user.user_behavior[incomprehensible_user.get_user_behavior_key(7)], \
            incomprehensible_user.user_behavior[incomprehensible_user.get_user_behavior_key(3)]

        result = (
            user_incomprehension_status_to_true,
            number_of_user_incomprehension_to_1,
            fatigue_quotas_of_grandpy_to_false
        )
        assert expected_result == result

    def test_get_request_parser(self):
        user_request = Conversation('ou se trouve openClassrooms', 1)
        expected_result = 'openClassrooms'
        result = user_request.get_request_parser()
        assert expected_result == result
