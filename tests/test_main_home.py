from . import requests
from . import pytest
from . import erasing_data
from . import get_mockreturn
from . import main


@pytest.mark.skip()
class TestHomeMain:
    @staticmethod
    def setup_method():
        erasing_data(1)

    # 11) DONE incivility query X1
    # @pytest.mark.skip()
    def test_incorrect_presentation_user_to_X1(self):
        # incorrect presentation of the user X1 ==> question without ('bonjour'...)
        presentation_user_incivility = main('ou se trouve openClassrooms', db_number=1)

        # user_behavior['has_user_incivility_status'] = True
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'has_user_incivility_status')]
        # user_behavior['has_user_indecency_status'] = False
        assert not presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'has_user_indecency_status')]
        # user_behavior['has_user_incomprehension_status'] = False
        assert not presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'has_user_incomprehension_status')]
        # user_behavior['has_fatigue_quotas_of_grandpy'] = False
        assert not presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'has_fatigue_quotas_of_grandpy')]
        # user_behavior['grandpy_status_code'] = 'mannerless'
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key('grandpy_status_code')]\
            == 'mannerless'
        # user_behavior['number_of_user_incivility'] = 1
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'number_of_user_incivility')] == 1
        # user_behavior['number_of_user_indecency'] = 0
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'number_of_user_indecency')] == 0
        # user_behavior['number_of_user_incomprehension'] = 0
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'number_of_user_incomprehension')] == 0
        # user_behavior['number_of_user_entries'] = 0
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'number_of_user_entries')] == 0

    # @pytest.mark.skip()
    def test_incorrect_presentation_user_to_X2(self):
        # incorrect presentation of the user X2 ==> question without ('bonjour'...)
        main('ou se trouve openClassrooms', db_number=1)
        presentation_user_incivility = main('ou se trouve openClassrooms', db_number=1)

        # user_behavior['has_user_incivility_status'] = True
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'has_user_incivility_status')]
        # user_behavior['has_user_indecency_status'] = False
        assert not presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'has_user_indecency_status')]
        # user_behavior['has_user_incomprehension_status'] = False
        assert not presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'has_user_incomprehension_status')]
        # user_behavior['has_fatigue_quotas_of_grandpy'] = False
        assert not presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'has_fatigue_quotas_of_grandpy')]
        # user_behavior['grandpy_status_code'] = 'mannerless'
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key('grandpy_status_code')]\
            == 'mannerless'
        # user_behavior['number_of_user_incivility'] = 2
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'number_of_user_incivility')] == 2
        # user_behavior['number_of_user_indecency'] = 0
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'number_of_user_indecency')] == 0
        # user_behavior['number_of_user_incomprehension'] = 0
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'number_of_user_incomprehension')] == 0
        # user_behavior['number_of_user_entries'] = 0
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key('number_of_user_entries')]\
            == 0

    # 13) DONE incivility query X3
    # @pytest.mark.skip()
    def test_incorrect_presentation_user_to_X3(self):
        # incorrect presentation of the user X3 ==> question without ('bonjour'...)
        main('ou se trouve openClassrooms', db_number=1)
        main('ou se trouve openClassrooms', db_number=1)
        main('ou se trouve openClassrooms', db_number=1)
        # incorrect presentation of the user ==> question without ('bonjour'...)
        presentation_user_incivility = main('ou se trouve openClassrooms', db_number=1)

        # user_behavior['has_fatigue_quotas_of_grandpy'] = True
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'has_fatigue_quotas_of_grandpy')]
        # user_behavior['grandpy_status_code'] = 'incivility_limit'
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key('grandpy_status_code')]\
            == 'incivility_limit'
        # user_behavior['number_of_user_incivility'] = 3
        assert presentation_user_incivility.user_behavior[
            presentation_user_incivility.__class__.get_user_behavior_key(
                'number_of_user_incivility')] == 3

    # 15) DONE indecency query (home) 1 to X2
    # @pytest.mark.skip()
    def test_indecency_request_user_to_X1(self):
        # incorrect request of the user X1 ==> indecency presentation without ('bonjour'....)
        presentation_user_indecency = main('dinosaure', db_number=1)

        # user_behavior['has_user_incivility_status'] = True
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'has_user_incivility_status')]
        # user_behavior['has_user_indecency_status'] = True
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'has_user_indecency_status')]
        # user_behavior['has_user_incomprehension_status'] = False
        assert not presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'has_user_incomprehension_status')]
        # user_behavior['has_fatigue_quotas_of_grandpy'] = False
        assert not presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'has_fatigue_quotas_of_grandpy')]
        # user_behavior['grandpy_status_code'] = 'disrespectful'
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key('grandpy_status_code')]\
            == 'disrespectful'
        # user_behavior['number_of_user_incivility'] = 1
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'number_of_user_incivility')] == 1
        # user_behavior['number_of_user_indecency'] = 1
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'number_of_user_indecency')] == 1
        # user_behavior['number_of_user_incomprehension'] = 0
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'number_of_user_incomprehension')] == 0
        # user_behavior['number_of_user_entries'] = 0
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key('number_of_user_entries')]\
            == 0

    # @pytest.mark.skip()
    def test_indecency_request_user_to_X2(self):
        # incorrect request of the user X2 ==> indecency presentation without ('bonjour'....)
        main('vieux', db_number=1)
        presentation_user_indecency = main('vieux', db_number=1)

        # user_behavior['has_user_incivility_status'] = True
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'has_user_incivility_status')]
        # user_behavior['has_user_indecency_status'] = True
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'has_user_indecency_status')]
        # user_behavior['has_user_incomprehension_status'] = False
        assert not presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'has_user_incomprehension_status')]
        # user_behavior['has_fatigue_quotas_of_grandpy'] = False
        assert not presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'has_fatigue_quotas_of_grandpy')]
        # user_behavior['grandpy_status_code'] = 'disrespectful'
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key('grandpy_status_code')]\
            == 'disrespectful'
        # user_behavior['number_of_user_incivility'] = 1
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'number_of_user_incivility')] == 1
        # user_behavior['number_of_user_indecency'] = 2
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'number_of_user_indecency')] == 2
        # user_behavior['number_of_user_incomprehension'] = 0
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'number_of_user_incomprehension')] == 0
        # user_behavior['number_of_user_entries'] = 0
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key('number_of_user_entries')]\
            == 0

    # 17) DONE indecency query (home) X3
    # @pytest.mark.skip()
    def test_indecency_request_user_to_X3(self):
        # incorrect request of the user X3 ==> indecency presentation without ('bonjour'....)
        main('dinosaure', db_number=1)
        main('vieux', db_number=1)
        main('senile', db_number=1)
        # incorrect request of the user X4 ==> indecency presentation without ('bonjour'....)
        presentation_user_indecency = main('fossile', db_number=1)

        # user_behavior['has_fatigue_quotas_of_grandpy'] = True
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'has_fatigue_quotas_of_grandpy')]
        # user_behavior['grandpy_status_code'] = 'indecency_limit'
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key('grandpy_status_code')]\
            == 'indecency_limit'
        # user_behavior['number_of_user_indecency'] = 3
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'number_of_user_indecency')] == 3

    # 19) DONE incomprehension query (home) 1 to X2
    # @pytest.mark.skip()
    def test_incomprehension_request_user_to_X1(self, monkeypatch):
        # incomprehension presentation of the user X1 ==> question without ('bonjour'...)
        expected_mock_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        monkeypatch.setattr(
            requests, 'get',
            get_mockreturn(expected_mock_result))
        presentation_user_incomprehension = main('', db_number=1)

        # user_behavior['has_user_incivility_status'] = True
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'has_user_incivility_status')]
        # user_behavior['has_user_indecency_status'] = False
        assert not presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'has_user_indecency_status')]
        # user_behavior['has_user_incomprehension_status'] = True
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'has_user_incomprehension_status')]
        # user_behavior['has_fatigue_quotas_of_grandpy'] = False
        assert not presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'has_fatigue_quotas_of_grandpy')]
        # user_behavior['grandpy_status_code'] = 'incomprehension'
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'grandpy_status_code')] == 'incomprehension'
        # user_behavior['number_of_user_incivility'] = 1
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'number_of_user_incivility')] == 1
        # user_behavior['number_of_user_indecency'] = 0
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'number_of_user_indecency')] == 0
        # user_behavior['number_of_user_incomprehension'] = 1
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'number_of_user_incomprehension')] == 1
        # user_behavior['number_of_user_entries'] = 0
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'number_of_user_entries')] == 0

    # @pytest.mark.skip()
    def test_incomprehension_request_user_to_X2(self, monkeypatch):
        # incomprehension presentation of the user X2 ==> question without ('bonjour'...)
        expected_mock_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        monkeypatch.setattr(
            requests, 'get',
            get_mockreturn(expected_mock_result))
        main('', db_number=1)
        presentation_user_incomprehension = main('', db_number=1)

        # user_behavior['has_user_incivility_status'] = True
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'has_user_incivility_status')]
        # user_behavior['has_user_indecency_status'] = False
        assert not presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'has_user_indecency_status')]
        # user_behavior['has_user_incomprehension_status'] = True
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'has_user_incomprehension_status')]
        # user_behavior['has_fatigue_quotas_of_grandpy'] = False
        assert not presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'has_fatigue_quotas_of_grandpy')]
        # user_behavior['grandpy_status_code'] = 'incomprehension'
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'grandpy_status_code')] == 'incomprehension'
        # user_behavior['number_of_user_incivility'] = 1
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'number_of_user_incivility')] == 1
        # user_behavior['number_of_user_indecency'] = 0
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'number_of_user_indecency')] == 0
        # user_behavior['number_of_user_incomprehension'] = 2
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'number_of_user_incomprehension')] == 2
        # user_behavior['number_of_user_entries'] = 0
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'number_of_user_entries')] == 0

    # 21) DONE incomprehension query X3
    # @pytest.mark.skip()
    def test_incomprehension_request_user_to_X3(self, monkeypatch):
        # incomprehension presentation of the user ==> question without ('bonjour'...)
        expected_mock_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        monkeypatch.setattr(
            requests, 'get',
            get_mockreturn(expected_mock_result))
        main('', db_number=1)
        main('', db_number=1)
        main('', db_number=1)
        # incomprehension presentation of the user X4 ==> question without ('bonjour'...)
        presentation_user_incomprehension = main('', db_number=1)

        # user_behavior['has_fatigue_quotas_of_grandpy'] = True
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'has_fatigue_quotas_of_grandpy')]
        # user_behavior['grandpy_status_code'] = 'incomprehension_limit'
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'grandpy_status_code')] == 'incomprehension_limit'
        # user_behavior['number_of_user_incomprehension'] = 3
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'number_of_user_incomprehension')] == 3

    # # 7) DONE correct query X1
    # @pytest.mark.skip()
    def test_correct_presentation_user(self):
        # correct presentation of the user ==> ('bonjour'....)
        dialogue_of_presentation = main('bonjour', db_number=1)

        # user_behavior['has_user_incivility_status'] == False
        assert not dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key('has_user_incivility_status')]
        # user_behavior['has_user_indecency_status'] == False
        assert not dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key('has_user_indecency_status')]
        # user_behavior['has_user_incomprehension_status'] == False
        assert not dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(
                'has_user_incomprehension_status')]
        # user_behavior['has_fatigue_quotas_of_grandpy'] == False
        assert not dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(
                'has_fatigue_quotas_of_grandpy')]
        # user_behavior['grandpy_status_code'] == 'benevolent'
        assert dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key('grandpy_status_code')]\
            == 'benevolent'
        # user_behavior['number_of_user_incivility'] == 0
        assert dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key('number_of_user_incivility')]\
            == 0
        # user_behavior['number_of_user_indecency'] == 0
        assert dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key('number_of_user_indecency')]\
            == 0
        # user_behavior['number_of_user_incomprehension'] == 0
        assert dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(
                'number_of_user_incomprehension')] == 0
        # user_behavior['number_of_user_entries'] == 0
        assert dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key('number_of_user_entries')] == 0
