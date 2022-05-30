from . import requests
from . import pytest
from . import erasing_data
from . import Conversation
from . import google_api
from . import get_mockreturn
from . import get_place_id_googleMap_api_mockreturn
from . import get_address_googleMap_api_mockreturn


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
        user_request.calculate_the_indecency_status('presentation', 'indecency')
        has_user_indecency_status\
            = user_request.user_behavior[
                user_request.get_user_behavior_key('has_user_indecency_status')]

        assert not has_user_indecency_status

        user_request.calculate_the_indecency_status('chat_session', 'indecency')
        has_user_indecency_status2\
            = user_request.user_behavior[
                user_request.get_user_behavior_key('has_user_indecency_status2')]

        assert not has_user_indecency_status2

    # @pytest.mark.skip()
    def test_calculate_the_indecency_status_to_True(self):
        user_request = Conversation('vieux', 1)
        user_request.calculate_the_indecency_status('presentation', 'indecency')
        has_user_indecency_status\
            = user_request.user_behavior[
                user_request.get_user_behavior_key('has_user_indecency_status')]

        assert has_user_indecency_status

        user_request.calculate_the_indecency_status('chat_session', 'indecency')
        has_user_indecency_status2\
            = user_request.user_behavior[
                user_request.get_user_behavior_key('has_user_indecency_status2')]

        assert has_user_indecency_status2

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

        incomprehensible_user = Conversation('openClassrooms', 1)
        incomprehensible_user.calculate_the_incomprehension_status(
            'presentation', 'incomprehension')
        user_incomprehension_status\
            = incomprehensible_user.user_behavior[
                incomprehensible_user.__class__.get_user_behavior_key(
                    'has_user_incomprehension_status')]

        assert not user_incomprehension_status

        incomprehensible_user.calculate_the_incomprehension_status(
            'chat_session', 'incomprehension')
        user_incomprehension_status2\
            = incomprehensible_user.user_behavior[
                incomprehensible_user.__class__.get_user_behavior_key(
                    'has_user_incomprehension_status2')]

        assert not user_incomprehension_status2

    # @pytest.mark.skip()
    def test_calculate_the_incomprehension_status_to_True(self, monkeypatch):
        expected_mock_result = {'candidates': [], 'status': 'ZERO_RESULTS'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_mock_result))
        incomprehension_user = Conversation('gjegruiotuygtugyt', 1)
        incomprehension_user.calculate_the_incomprehension_status('presentation', 'incomprehension')
        user_incomprehension_status\
            = incomprehension_user.user_behavior[
                incomprehension_user.__class__.get_user_behavior_key(
                    'has_user_incomprehension_status')]
        assert user_incomprehension_status

        incomprehension_user.calculate_the_incomprehension_status('chat_session', 'incomprehension')
        user_incomprehension_status2\
            = incomprehension_user.user_behavior[
                incomprehension_user.__class__.get_user_behavior_key(
                    'has_user_incomprehension_status2')]
        assert user_incomprehension_status2

        incomprehension_user = Conversation('1255871436', 1)
        incomprehension_user.calculate_the_incomprehension_status('presentation', 'incomprehension')
        user_incomprehension_status\
            = incomprehension_user.user_behavior[
                incomprehension_user.__class__.get_user_behavior_key(
                    'has_user_incomprehension_status')]

        assert user_incomprehension_status

        incomprehension_user.calculate_the_incomprehension_status('chat_session', 'incomprehension')
        user_incomprehension_status2\
            = incomprehension_user.user_behavior[
                incomprehension_user.__class__.get_user_behavior_key(
                    'has_user_incomprehension_status2')]

        assert user_incomprehension_status2

        expected_mock_result2 = {'candidates': [], 'status': 'INVALID_REQUEST'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_mock_result2))
        incomprehension_user = Conversation('', 1)
        incomprehension_user.calculate_the_incomprehension_status('presentation', 'incomprehension')
        user_incomprehension_status\
            = incomprehension_user.user_behavior[
                incomprehension_user.__class__.get_user_behavior_key(
                    'has_user_incomprehension_status')]
        assert user_incomprehension_status

        incomprehension_user.calculate_the_incomprehension_status('chat_session', 'incomprehension')
        user_incomprehension_status2\
            = incomprehension_user.user_behavior[
                incomprehension_user.__class__.get_user_behavior_key(
                    'has_user_incomprehension_status2')]
        assert user_incomprehension_status2

    def test_level_user_name(self):
        user_name_level = Conversation('', 1)
        indecency1 = user_name_level.level_user_name('presentation', 'indecency')
        indecency2 = user_name_level.level_user_name('chat_session', 'indecency')
        incomprehension1 = user_name_level.level_user_name('presentation', 'incomprehension')
        incomprehension2 = user_name_level.level_user_name('chat_session', 'incomprehension')

        assert indecency1\
            == user_name_level.__class__.get_user_behavior_key('has_user_indecency_status')
        assert indecency2\
               == user_name_level.__class__.get_user_behavior_key('has_user_indecency_status2')
        assert incomprehension1\
            == user_name_level.__class__.get_user_behavior_key('has_user_incomprehension_status')
        assert incomprehension2\
            == user_name_level.__class__.get_user_behavior_key('has_user_incomprehension_status2')

    def test_level_status(self):
        user_level_status = Conversation('', 1)
        user_level_status.level_status('presentation', 'indecency', False)
        assert not user_level_status.user_behavior[
            user_level_status.__class__.get_user_behavior_key('has_user_indecency_status')]

        user_level_status.level_status('presentation', 'indecency', True)
        assert user_level_status.user_behavior[
            user_level_status.__class__.get_user_behavior_key('has_user_indecency_status')]

        user_level_status.level_status('chat_session', 'indecency', False)
        assert not user_level_status.user_behavior[
            user_level_status.__class__.get_user_behavior_key('has_user_indecency_status2')]

        user_level_status.level_status('chat_session', 'indecency', True)
        assert user_level_status.user_behavior[
            user_level_status.__class__.get_user_behavior_key('has_user_indecency_status2')]

        user_level_status.level_status('presentation', 'incomprehension', False)
        assert not user_level_status.user_behavior[
            user_level_status.__class__.get_user_behavior_key('has_user_incomprehension_status')]

        user_level_status.level_status('presentation', 'incomprehension', True)
        assert user_level_status.user_behavior[
            user_level_status.__class__.get_user_behavior_key('has_user_incomprehension_status')]

        user_level_status.level_status('chat_session', 'incomprehension', False)
        assert not user_level_status.user_behavior[
            user_level_status.__class__.get_user_behavior_key('has_user_incomprehension_status2')]

        user_level_status.level_status('chat_session', 'incomprehension', True)
        assert user_level_status.user_behavior[
            user_level_status.__class__.get_user_behavior_key('has_user_incomprehension_status2')]

    def test_get_request_parser(self):
        user_request = Conversation('ou se trouve openClassrooms', 1)
        user_request.get_user_request_parser()
        user_entry = user_request.user_entry

        assert user_entry == 'openClassrooms'
