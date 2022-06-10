#!/usr/bin/env python
"""test user behaviour module """
from . import requests
from . import pytest
from . import BehaviorParams
from . import erasing_data
from . import google_api
from . import get_place_id_googleMap_api_mockreturn, get_address_googleMap_api_mockreturn
from . import get_mockreturn


# @pytest.mark.skip()
class TestBehavior:
    @staticmethod
    def setup_method():
        erasing_data(1)

    # @pytest.mark.skip()
    def test_set_has_user_incivility_status(self):
        chat_session = BehaviorParams('', 1)

        chat_session.set_has_user_incivility_status(True)
        assert chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('has_user_incivility_status')]

        chat_session.set_has_user_incivility_status(False)
        assert not chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('has_user_incivility_status')]

    # @pytest.mark.skip()
    def test_set_has_user_status(self):
        chat_session = BehaviorParams('', 1)

        chat_session.set_has_user_status('has_user_indecency_status', True)
        assert chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('has_user_indecency_status')]

        chat_session.set_has_user_status('has_user_indecency_status', False)
        assert not chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('has_user_indecency_status')]

        chat_session.set_has_user_status('has_user_indecency_status2', True)
        assert chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('has_user_indecency_status2')]

        chat_session.set_has_user_status('has_user_indecency_status2', False)
        assert not chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('has_user_indecency_status2')]

        chat_session.set_has_user_status('has_user_incomprehension_status', True)
        assert chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('has_user_incomprehension_status')]

        chat_session.set_has_user_status('has_user_incomprehension_status', False)
        assert not chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('has_user_incomprehension_status')]

        chat_session.set_has_user_status('has_user_incomprehension_status2', True)
        assert chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('has_user_incomprehension_status2')]

        chat_session.set_has_user_status('has_user_incomprehension_status2', False)
        assert not chat_session.user_behavior[
            chat_session.__class__.get_user_behavior_key('has_user_incomprehension_status2')]

    # @pytest.mark.skip()
    def test_set_has_fatigue_quotas_of_grandpy(self):
        chat_session = BehaviorParams('', 1)

        chat_session.set_has_fatigue_quotas_of_grandpy(True)
        assert chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

        chat_session.set_has_fatigue_quotas_of_grandpy(False)
        assert not chat_session.user_behavior[
                chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

    def test_calculate_the_incivility_status_to_False(self):
        user_request = BehaviorParams('Bonjour', 1)

        user_request.calculate_the_incivility_status()
        assert not user_request.user_behavior[
            user_request.get_user_behavior_key('has_user_incivility_status')]

    # @pytest.mark.skip()
    def test_calculate_the_incivility_status_to_True(self):
        user_request = BehaviorParams('openClassrooms', 1)

        user_request.calculate_the_incivility_status()
        assert user_request.user_behavior[
            user_request.get_user_behavior_key('has_user_incivility_status')]

    # @pytest.mark.skip()
    def test_calculate_the_indecency_status_to_False(self):
        user_request = BehaviorParams('bonjour', 1)

        user_request.calculate_the_indecency_status('has_user_indecency_status')
        assert not user_request.user_behavior[
            user_request.get_user_behavior_key('has_user_indecency_status')]

        user_request.calculate_the_indecency_status('has_user_indecency_status2')
        assert not user_request.user_behavior[
            user_request.get_user_behavior_key('has_user_indecency_status2')]

    # @pytest.mark.skip()
    def test_calculate_the_indecency_status_to_True(self):
        user_request = BehaviorParams('vieux', 1)

        user_request.calculate_the_indecency_status('has_user_indecency_status')
        assert user_request.user_behavior[
            user_request.get_user_behavior_key('has_user_indecency_status')]

        user_request.calculate_the_indecency_status('has_user_indecency_status2')
        assert user_request.user_behavior[
            user_request.get_user_behavior_key('has_user_indecency_status2')]

    # @pytest.mark.skip()
    def test_calculate_the_incomprehension_status_to_False(self, monkeypatch):
        # level 1
        expected_result1 = {
            'candidates': [{
                'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}],
            'status': 'OK'}
        # leval 2
        expected_result2 = {
            'html_attributions': [],
            'result': {
                'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                'geometry': {
                    'location': {'lat': 48.8975156, 'lng': 2.3833993},
                    'viewport': {
                        'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                        'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}}}},
            'status': 'OK'}
        # mock level 1
        monkeypatch.setattr(
            google_api, 'get_placeid_from_address',
            get_place_id_googleMap_api_mockreturn(expected_result1))
        # mock level 2
        monkeypatch.setattr(
            google_api, 'get_address_api_from_placeid',
            get_address_googleMap_api_mockreturn(expected_result2))

        incomprehensible_user = BehaviorParams('openClassrooms', 1)

        incomprehensible_user.calculate_the_incomprehension_status(
            'has_user_incomprehension_status')
        assert not incomprehensible_user.user_behavior[
            incomprehensible_user.__class__.get_user_behavior_key(
                'has_user_incomprehension_status')]

        incomprehensible_user.calculate_the_incomprehension_status(
            'has_user_incomprehension_status2')
        assert not incomprehensible_user.user_behavior[
            incomprehensible_user.__class__.get_user_behavior_key(
                'has_user_incomprehension_status2')]

    # @pytest.mark.skip()
    def test_calculate_the_incomprehension_status_to_True(self, monkeypatch):
        expected_mock_result = {'candidates': [], 'status': 'ZERO_RESULTS'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_mock_result))
        incomprehension_user = BehaviorParams('gjegruiotuygtugyt', 1)

        incomprehension_user.calculate_the_incomprehension_status('has_user_incomprehension_status')
        assert incomprehension_user.user_behavior[
            incomprehension_user.__class__.get_user_behavior_key(
                'has_user_incomprehension_status')]

        incomprehension_user.calculate_the_incomprehension_status(
            'has_user_incomprehension_status2')
        assert incomprehension_user.user_behavior[
            incomprehension_user.__class__.get_user_behavior_key(
                'has_user_incomprehension_status2')]

        incomprehension_user = BehaviorParams('1255871436', 1)
        incomprehension_user.calculate_the_incomprehension_status('has_user_incomprehension_status')
        assert incomprehension_user.user_behavior[
            incomprehension_user.__class__.get_user_behavior_key(
                'has_user_incomprehension_status')]

        incomprehension_user.calculate_the_incomprehension_status(
            'has_user_incomprehension_status2')
        assert incomprehension_user.user_behavior[
            incomprehension_user.__class__.get_user_behavior_key(
                'has_user_incomprehension_status2')]

        expected_mock_result2 = {'candidates': [], 'status': 'INVALID_REQUEST'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_mock_result2))
        incomprehension_user = BehaviorParams('', 1)
        incomprehension_user.calculate_the_incomprehension_status('has_user_incomprehension_status')
        assert incomprehension_user.user_behavior[
            incomprehension_user.__class__.get_user_behavior_key(
                'has_user_incomprehension_status')]

        incomprehension_user.calculate_the_incomprehension_status(
            'has_user_incomprehension_status2')
        assert incomprehension_user.user_behavior[
            incomprehension_user.__class__.get_user_behavior_key(
                'has_user_incomprehension_status2')]

    def test_level_parameters(self):
        level_parameter = BehaviorParams('', 1)
        assert level_parameter.level_parameters(1) == 'presentation'
        assert level_parameter.level_parameters(2) == 'chat_session'

    def test_level_name_user(self):
        user_name_level = BehaviorParams('', 1)

        assert user_name_level.level_name_user(
            user_name_level.level_parameters(1), 'has_user_indecency_status')\
            == user_name_level.__class__.get_user_behavior_key('has_user_indecency_status')
        assert user_name_level.level_name_user(
            user_name_level.level_parameters(1), 'number_of_user_indecency')\
            == user_name_level.__class__.get_user_behavior_key('number_of_user_indecency')
        assert user_name_level.level_name_user(
            user_name_level.level_parameters(2), 'has_user_indecency_status2')\
            == user_name_level.__class__.get_user_behavior_key('has_user_indecency_status2')
        assert user_name_level.level_name_user(
            user_name_level.level_parameters(2), 'number_of_user_indecency2')\
            == user_name_level.__class__.get_user_behavior_key('number_of_user_indecency2')
        assert user_name_level.level_name_user(
            user_name_level.level_parameters(1), 'has_user_incomprehension_status')\
            == user_name_level.__class__.get_user_behavior_key('has_user_incomprehension_status')
        assert user_name_level.level_name_user(
            user_name_level.level_parameters(1), 'number_of_user_incomprehension')\
            == user_name_level.__class__.get_user_behavior_key('number_of_user_incomprehension')
        assert user_name_level.level_name_user(
            user_name_level.level_parameters(2), 'has_user_incomprehension_status2')\
            == user_name_level.__class__.get_user_behavior_key('has_user_incomprehension_status2')
        assert user_name_level.level_name_user(
            user_name_level.level_parameters(2), 'number_of_user_incomprehension2')\
            == user_name_level.__class__.get_user_behavior_key('number_of_user_incomprehension2')
