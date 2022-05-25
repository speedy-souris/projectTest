from . import pytest
from . import erasing_data
from . import Conversation
from . import google_api
from . import get_place_id_googleMap_api_mockreturn


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

    def test_calculate_the_incivility_status_to_False(self):
        user_request = Conversation('Bonjour', 1)
        user_request.calculate_the_incivility_status()

        has_user_incivility_status\
            = user_request.user_behavior[
                user_request.get_user_behavior_key('has_user_incivility_status')]

        assert not has_user_incivility_status

    # @pytest.mark.skip()
    def test_calculate_the_incivility_status_to_True(self):
        user_request = Conversation('openClassrooms', 1)
        user_request.calculate_the_incivility_status()

        has_user_incivility_status\
            = user_request.user_behavior[
                user_request.get_user_behavior_key('has_user_incivility_status')]

        assert has_user_incivility_status

    # @pytest.mark.skip()
    def test_calculate_the_indecency_status_to_False(self):
        user_request = Conversation('bonjour', 1)
        user_request.calculate_the_indecency_status()

        has_user_indecency_status\
            = user_request.user_behavior[
                user_request.get_user_behavior_key('has_user_indecency_status')]

        assert not has_user_indecency_status

    # @pytest.mark.skip()
    def test_calculate_the_indecency_status_to_True(self):
        user_request = Conversation('vieux', 1)
        user_request.calculate_the_indecency_status()

        has_user_indecency_status\
            = user_request.user_behavior[
                user_request.get_user_behavior_key('has_user_indecency_status')]

        assert has_user_indecency_status

    # @pytest.mark.skip()
    def test_calculate_the_incomprehension_status_to_True(self, monkeypatch):
        expected_mock_result1 = {'candidates': [], 'status': 'ZERO_RESULTS'}
        monkeypatch.setattr(
            google_api, 'get_placeid_from_address',
            get_place_id_googleMap_api_mockreturn(expected_mock_result1))
        incomprehensible_user = Conversation('gjegruiotuygtugyt', 1)
        incomprehensible_user.calculate_the_incomprehension_status()
        user_incomprehension_status\
            = incomprehensible_user.user_behavior[
                incomprehensible_user.__class__.get_user_behavior_key(
                    'has_user_incomprehension_status')]

        assert user_incomprehension_status

        expected_mock_result1 = {'candidates': [], 'status': 'ZERO_RESULTS'}
        monkeypatch.setattr(
            google_api, 'get_placeid_from_address',
            get_place_id_googleMap_api_mockreturn(expected_mock_result1))
        incomprehensible_user = Conversation('1255871436', 1)
        incomprehensible_user.calculate_the_incomprehension_status()
        user_incomprehension_status\
            = incomprehensible_user.user_behavior[
                incomprehensible_user.__class__.get_user_behavior_key(
                    'has_user_incomprehension_status')]

        assert user_incomprehension_status

        expected_mock_result2 = {'candidates': [], 'status': 'INVALID_REQUEST'}
        monkeypatch.setattr(
            google_api, 'get_placeid_from_address',
            get_place_id_googleMap_api_mockreturn(expected_mock_result2))
        incomprehensible_user = Conversation('', 1)
        incomprehensible_user.calculate_the_incomprehension_status()
        user_incomprehension_status \
            = incomprehensible_user.user_behavior[
                incomprehensible_user.__class__.get_user_behavior_key(
                    'has_user_incomprehension_status')]

        assert user_incomprehension_status

    def test_get_request_parser(self):
        user_request = Conversation('ou se trouve openClassrooms', 1)
        user_request.get_user_request_parser()
        user_entry = user_request.user_entry

        assert user_entry == 'openClassrooms'
