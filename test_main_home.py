#!/usr/bin/env python
import requests
from mock_api import get_mockreturn
import main
from redis_utilities import erasing_data
import pytest


class TestHomeMain:
    @staticmethod
    def setup_method():
        erasing_data(1)

    # 11) DONE incivility query X1
    # @pytest.mark.skip()
    def test_incorrect_presentation_user_to_X1(self):
        # incorrect presentation of the user X1 ==> question without ('bonjour'...)
        presentation_user_incivility = main.main('ou se trouve openClassrooms', db_number=1)

        # user_behavior['has_user_incivility_status'] = True
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(0)]
        # user_behavior['has_user_indecency_status'] = False
        assert not presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(1)]
        # user_behavior['has_user_incomprehension_status'] = False
        assert not presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(2)]
        # user_behavior['has_fatigue_quotas_of_grandpy'] = False
        assert not presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(3)]
        # user_behavior['grandpy_status_code'] = 'mannerless'
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(4)] == 'mannerless'
        # user_behavior['number_of_user_incivility'] = 1
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(5)] == 1
        # user_behavior['number_of_user_indecency'] = 0
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(6)] == 0
        # user_behavior['number_of_user_incomprehension'] = 0
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(7)] == 0
        # user_behavior['number_of_user_entries'] = 0
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(8)] == 0

    # @pytest.mark.skip()
    def test_incorrect_presentation_user_to_X2(self):
        # incorrect presentation of the user X2 ==> question without ('bonjour'...)
        main.main('ou se trouve openClassrooms', db_number=1)
        presentation_user_incivility = main.main('ou se trouve openClassrooms', db_number=1)

        # user_behavior['has_user_incivility_status'] = True
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(0)]
        # user_behavior['has_user_indecency_status'] = False
        assert not presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(1)]
        # user_behavior['has_user_incomprehension_status'] = False
        assert not presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(2)]
        # user_behavior['has_fatigue_quotas_of_grandpy'] = False
        assert not presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(3)]
        # user_behavior['grandpy_status_code'] = 'mannerless'
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(4)] == 'mannerless'
        # user_behavior['number_of_user_incivility'] = 2
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(5)] == 2
        # user_behavior['number_of_user_indecency'] = 0
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(6)] == 0
        # user_behavior['number_of_user_incomprehension'] = 0
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(7)] == 0
        # user_behavior['number_of_user_entries'] = 0
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(8)] == 0

    # 13) DONE incivility query X3
    # @pytest.mark.skip()
    def test_incorrect_presentation_user_to_X3(self):
        # incorrect presentation of the user X3 ==> question without ('bonjour'...)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        # incorrect presentation of the user ==> question without ('bonjour'...)
        presentation_user_incivility = main.main('ou se trouve openClassrooms', db_number=1)

        # user_behavior['has_fatigue_quotas_of_grandpy'] = True
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(3)]
        # user_behavior['grandpy_status_code'] = 'incivility_limit'
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(4)] == 'incivility_limit'
        # user_behavior['number_of_user_incivility'] = 3
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(5)] == 3

    # 15) DONE indecency query (home) 1 to X2
    # @pytest.mark.skip()
    def test_indecency_request_user_to_X1(self):
        # incorrect request of the user X1 ==> indecency presentation without ('bonjour'....)
        presentation_user_indecency = main.main('dinosaure', db_number=1)

        # user_behavior['has_user_incivility_status'] = True
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(0)]
        # user_behavior['has_user_indecency_status'] = True
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(1)]
        # user_behavior['has_user_incomprehension_status'] = False
        assert not presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(2)]
        # user_behavior['has_fatigue_quotas_of_grandpy'] = False
        assert not presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(3)]
        # user_behavior['grandpy_status_code'] = 'disrespectful'
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(4)] == 'disrespectful'
        # user_behavior['number_of_user_incivility'] = 1
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(5)] == 1
        # user_behavior['number_of_user_indecency'] = 1
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(6)] == 1
        # user_behavior['number_of_user_incomprehension'] = 0
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(7)] == 0
        # user_behavior['number_of_user_entries'] = 0
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(8)] == 0

    # @pytest.mark.skip()
    def test_indecency_request_user_to_X2(self):
        # incorrect request of the user X2 ==> indecency presentation without ('bonjour'....)
        main.main('vieux', db_number=1)
        presentation_user_indecency = main.main('vieux', db_number=1)

        # user_behavior['has_user_incivility_status'] = True
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(0)]
        # user_behavior['has_user_indecency_status'] = True
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(1)]
        # user_behavior['has_user_incomprehension_status'] = False
        assert not presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(2)]
        # user_behavior['has_fatigue_quotas_of_grandpy'] = False
        assert not presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(3)]
        # user_behavior['grandpy_status_code'] = 'disrespectful'
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(4)] == 'disrespectful'
        # user_behavior['number_of_user_incivility'] = 1
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(5)] == 1
        # user_behavior['number_of_user_indecency'] = 2
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(6)] == 2
        # user_behavior['number_of_user_incomprehension'] = 0
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(7)] == 0
        # user_behavior['number_of_user_entries'] = 0
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(8)] == 0

    # 17) DONE indecency query (home) X3
    # @pytest.mark.skip()
    def test_indecency_request_user_to_X3(self):
        # incorrect request of the user X3 ==> indecency presentation without ('bonjour'....)
        main.main('dinosaure', db_number=1)
        main.main('vieux', db_number=1)
        main.main('senile', db_number=1)
        # incorrect request of the user X4 ==> indecency presentation without ('bonjour'....)
        presentation_user_indecency = main.main('fossile', db_number=1)

        # user_behavior['has_fatigue_quotas_of_grandpy'] = True
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(3)]
        # user_behavior['grandpy_status_code'] = 'indecency_limit'
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(4)] == 'indecency_limit'
        # user_behavior['number_of_user_indecency'] = 3
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(6)] == 3

    # 19) DONE incomprehension query (home) 1 to X2
    # @pytest.mark.skip()
    def test_incomprehension_request_user_to_X1(self, monkeypatch):
        # incomprehension presentation of the user X1 ==> question without ('bonjour'...)
        presentation_user_incomprehension = main.main('', db_number=1)
        expected_mock_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        mock_result = expected_mock_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        presentation_user_incomprehension.calculate_the_incomprehension()

        # user_behavior['has_user_incivility_status'] = True
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(0)]
        # user_behavior['has_user_indecency_status'] = False
        assert not presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(1)]
        # user_behavior['has_user_incomprehension_status'] = True
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(2)]
        # user_behavior['has_fatigue_quotas_of_grandpy'] = False
        assert not presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(3)]
        # user_behavior['grandpy_status_code'] = 'incomprehension'
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(4)] ==\
            'incomprehension'
        # user_behavior['number_of_user_incivility'] = 1
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(5)] == 1
        # user_behavior['number_of_user_indecency'] = 0
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(6)] == 0
        # user_behavior['number_of_user_incomprehension'] = 1
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(7)] == 1
        # user_behavior['number_of_user_entries'] = 0
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(8)] == 0

    # @pytest.mark.skip()
    def test_incomprehension_request_user_to_X2(self, monkeypatch):
        # incomprehension presentation of the user X2 ==> question without ('bonjour'...)
        presentation_user_incomprehension = main.main('', db_number=1)
        expected_mock_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        mock_result = expected_mock_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        presentation_user_incomprehension.calculate_the_incomprehension()
        presentation_user_incomprehension.calculate_the_incomprehension()

        # user_behavior['has_user_incivility_status'] = True
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(0)]
        # user_behavior['has_user_indecency_status'] = False
        assert not presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(1)]
        # user_behavior['has_user_incomprehension_status'] = True
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(2)]
        # user_behavior['has_fatigue_quotas_of_grandpy'] = False
        assert not presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(3)]
        # user_behavior['grandpy_status_code'] = 'incomprehension'
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(4)] == \
            'incomprehension'
        # user_behavior['number_of_user_incivility'] = 1
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(5)] == 1
        # user_behavior['number_of_user_indecency'] = 0
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(6)] == 0
        # user_behavior['number_of_user_incomprehension'] = 2
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(7)] == 2
        # user_behavior['number_of_user_entries'] = 0
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(8)] == 0

    # 21) DONE incomprehension query X3
    # @pytest.mark.skip()
    def test_incomprehension_request_user_to_X3(self, monkeypatch):
        # incomprehension presentation of the user ==> question without ('bonjour'...)
        presentation_user_incomprehension = main.main('', db_number=1)
        expected_mock_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        mock_result = expected_mock_result
        mockreturn = get_mockreturn(mock_result)
        monkeypatch.setattr(requests, 'get', mockreturn)
        presentation_user_incomprehension.calculate_the_incomprehension()
        presentation_user_incomprehension.calculate_the_incomprehension()
        presentation_user_incomprehension.calculate_the_incomprehension()
        # incomprehension presentation of the user X4 ==> question without ('bonjour'...)
        presentation_user_incomprehension.calculate_the_incomprehension()

        # user_behavior['has_fatigue_quotas_of_grandpy'] = True
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(3)]
        # user_behavior['grandpy_status_code'] = 'incomprehension_limit'
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(4)] ==\
            'incomprehension_limit'
        # user_behavior['number_of_user_incomprehension'] = 3
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(7)] == 3

    # # 7) DONE correct query X1
    # @pytest.mark.skip()
    def test_correct_presentation_user(self):
        # correct presentation of the user ==> ('bonjour'....)
        dialogue_of_presentation = main.main('bonjour', db_number=1)

        # has_user_incivility_status == False
        assert not dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(0)]
        # has_user_indecency_status == False
        assert not dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(1)]
        # has_user_incomprehension_status == False
        assert not dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(2)]
        # has_fatigue_quotas_of_grandpy == False
        assert not dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(3)]
        # grandpy_status_code == 'benevolent'
        assert dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(4)] == 'benevolent'
        # number_of_user_incivility == 0
        assert dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(5)] == 0
        # number_of_user_indecency == 0
        assert dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(6)] == 0
        # number_of_user_incomprehension == 0
        assert dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(7)] == 0
        # number_of_user_entries == 0
        assert dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(8)] == 0
