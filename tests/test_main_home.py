from . import requests
from . import pytest
from . import RedisDataManagement
from . import get_mockreturn
from .. import main
# from . import BehaviorParams


# @pytest.mark.skip()
class TestHomeMain:
    @staticmethod
    def setup_method():
        db_session = RedisDataManagement(db_number=1)
        db_session.get_database_access(1)
        db_session.erasing_data()

    # 11) DONE incivility query X1
    # @pytest.mark.skip()
    def test_incorrect_presentation_user_to_1(self):
        # incorrect presentation of the user X1 ==> question without ('bonjour'...)
        presentation_user = main.main('ou se trouve openClassrooms', db_number=1)
        # has_user_incivility_status = True
        assert presentation_user.has_user_incivility_status
        # has_user_indecency_status = False
        assert not presentation_user.has_user_indecency_status
        # has_user_incomprehension_status = False
        assert not presentation_user.has_user_incomprehension_status
        # has_fatigue_quotas_of_grandpy = False
        assert not presentation_user.has_fatigue_quotas_of_grandpy
        # grandpy_status_code = 'mannerless'
        assert presentation_user.grandpy_status_code == 'mannerless'
        # number_of_user_incivility = 1
        assert presentation_user.number_of_user_incivility == 1
        # number_of_user_indecency = 0
        assert presentation_user.number_of_user_indecency == 0
        # number_of_user_incomprehension = 0
        assert presentation_user.number_of_user_incomprehension == 0
        # number_of_user_entries = 0
        assert presentation_user.number_of_user_entries == 0

    @pytest.mark.skip()
    def test_incorrect_presentation_user_to_2(self):
        # incorrect presentation of the user X2 ==> question without ('bonjour'...)
        main.main('ou se trouve openClassrooms', db_number=1)
        presentation_user_incivility = main.main('ou se trouve openClassrooms', db_number=1)
        # has_user_incivility_status = True
        assert presentation_user_incivility.has_user_incivility_status
        # has_user_indecency_status = False
        assert not presentation_user_incivility.has_user_indecency_status
        # has_user_incomprehension_status = False
        assert not presentation_user_incivility.has_user_incomprehension_status
        # has_fatigue_quotas_of_grandpy = False
        assert not presentation_user_incivility.has_fatigue_quotas_of_grandpy
        # grandpy_status_code = 'mannerless'
        assert presentation_user_incivility.grandpy_status_code == 'mannerless'
        # number_of_user_incivility = 2
        assert presentation_user_incivility.number_of_user_incivility == 2
        # number_of_user_indecency = 0
        assert presentation_user_incivility.number_of_user_indecency == 0
        # number_of_user_incomprehension = 0
        assert presentation_user_incivility.number_of_user_incomprehension == 0
        # number_of_user_entries = 0
        assert presentation_user_incivility.number_of_user_entries == 0

    # 13) DONE incivility query X3
    @pytest.mark.skip()
    def test_incorrect_presentation_user_to_3(self):
        # incorrect presentation of the user X3 ==> question without ('bonjour'...)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        # incorrect presentation of the user ==> question without ('bonjour'...)
        presentation_user_incivility = main.main('ou se trouve openClassrooms', db_number=1)

        # grandpy_status_code = 'mannerless'
        assert presentation_user_incivility.grandpy_status_code == 'incivility_limit'
        # number_of_user_incivility = 3
        assert presentation_user_incivility.number_of_user_incivility == 3
        # has_fatigue_quotas_of_grandpy = True
        assert presentation_user_incivility.has_fatigue_quotas_of_grandpy

        presentation_user_incivility = main.main('ou se trouve openClassrooms', db_number=1)
        # has_fatigue_quotas_of_grandpy = True
        assert not presentation_user_incivility.has_fatigue_quotas_of_grandpy
        # grandpy_status_code = 'incivility_limit'
        assert presentation_user_incivility.grandpy_status_code == 'incivility_limit'
        # number_of_user_incivility = 3
        assert presentation_user_incivility.number_of_user_incivility == 3
        presentation_user_incivility = main.main('ou se trouve openClassrooms', db_number=1)
        # grandpy_status_code = 'incivility_limit'
        assert presentation_user_incivility.grandpy_status_code == 'incivility_limit'
        # number_of_user_incivility = 3
        assert presentation_user_incivility.number_of_user_incivility == 3

    # 15) DONE indecency query (home) 1 to X2
    @pytest.mark.skip()
    def test_indecency_request_user_to_1(self):
        # incorrect request of the user X1 ==> indecency presentation without ('bonjour'....)
        presentation_user_indecency = main.main('dinosaure', db_number=1)

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

    @pytest.mark.skip()
    def test_indecency_request_user_to_2(self):
        # incorrect request of the user X2 ==> indecency presentation without ('bonjour'....)
        main.main('vieux', db_number=1)
        presentation_user_indecency = main.main('vieux', db_number=1)

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
    @pytest.mark.skip()
    def test_indecency_request_user_to_3(self):
        # incorrect request of the user X3 ==> indecency presentation without ('bonjour'....)
        main.main('dinosaure', db_number=1)
        main.main('vieux', db_number=1)
        # incorrect request of the user X4 ==> indecency presentation without ('bonjour'....)
        presentation_user_indecency = main.main('fossile', db_number=1)

        # user_behavior['has_fatigue_quotas_of_grandpy'] = False
        assert not presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
                'has_fatigue_quotas_of_grandpy')]
        # user_behavior['grandpy_status_code'] = 'disrespectful'
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key('grandpy_status_code')]\
            == 'disrespectful'
        # user_behavior['number_of_user_indecency'] = 3
        assert presentation_user_indecency.user_behavior[
            presentation_user_indecency.__class__.get_user_behavior_key(
               'number_of_user_indecency')] == 3

        presentation_user_indecency = main.main('senile', db_number=1)
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
    @pytest.mark.skip()
    def test_incomprehension_request_user_to_1(self, monkeypatch):
        # incomprehension presentation of the user X1 ==> question without ('bonjour'...)
        expected_mock_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_mock_result))
        presentation_user_incomprehension = main.main('', db_number=1)

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

    @pytest.mark.skip()
    def test_incomprehension_request_user_to_2(self, monkeypatch):
        # incomprehension presentation of the user X2 ==> question without ('bonjour'...)
        expected_mock_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_mock_result))
        main.main('', db_number=1)
        presentation_user_incomprehension = main.main('', db_number=1)

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
        # user_behavior['number_of_user_incivility'] = 2
        assert presentation_user_incomprehension.user_behavior[
            presentation_user_incomprehension.__class__.get_user_behavior_key(
                'number_of_user_incivility')] == 2
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
    @pytest.mark.skip()
    def test_incomprehension_request_user_to_3(self, monkeypatch):
        # incomprehension presentation of the user ==> question without ('bonjour'...)
        expected_mock_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_mock_result))
        main.main('', db_number=1)
        main.main('', db_number=1)
        main.main('', db_number=1)
        # incomprehension presentation of the user X4 ==> question without ('bonjour'...)
        presentation_user_incomprehension = main.main('', db_number=1)

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
    @pytest.mark.skip()
    def test_correct_presentation_user(self):
        # correct presentation of the user ==> ('bonjour'....)
        dialogue_of_presentation = main.main('bonjour', db_number=1)

        # user_behavior['has_user_incivility_status'] == False
        assert not dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key('has_user_incivility_status')]
        # user_behavior['has_user_indecency_status'] == False
        assert not dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(
                'has_user_indecency_status')]
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

    # @pytest.mark.skip()
    # @pytest.mark.parametrize(
    #     "behavior_status_returned, behavior_status",
    #     [(main.main('ou se trouve openClassrooms', db_number=1).user_behavior['has_user_incivility_status'], True),
    #      (BehaviorParams('', 1).user_behavior['has_user_indecency_status'], False),
    #      (BehaviorParams('', 1).user_behavior['has_user_indecency_status2'], False),
    #      (BehaviorParams('', 1).user_behavior['has_user_incomprehension_status'], False),
    #      (BehaviorParams('', 1).user_behavior['has_user_incomprehension_status2'], False),
    #      (BehaviorParams('', 1).user_behavior['has_fatigue_quotas_of_grandpy'], False),
    #      (BehaviorParams('', 1).user_behavior['grandpy_status_code'], 'mannerless'),
    #      (BehaviorParams('', 1).user_behavior['behavior_level'], 'presentation'),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_incivility'], 1),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_indecency'], 0),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_indecency2'], 0),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_incomprehension'], 0),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_incomprehension2'], 0),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_entries'], 0)])
    # def test_main_incivility(self, behavior_status_returned, behavior_status):
    #
    #     assert behavior_status_returned == behavior_status

    # @pytest.mark.skip()
    # @pytest.mark.parametrize(
    #     "behavior_status_returned, behavior_status",
    #     [(BehaviorParams('', 1).user_behavior['has_user_incivility_status'], True),
    #      (BehaviorParams('', 1).user_behavior['has_user_indecency_status'], False),
    #      (BehaviorParams('', 1).user_behavior['has_user_indecency_status2'], False),
    #      (BehaviorParams('', 1).user_behavior['has_user_incomprehension_status'], False),
    #      (BehaviorParams('', 1).user_behavior['has_user_incomprehension_status2'], False),
    #      (BehaviorParams('', 1).user_behavior['has_fatigue_quotas_of_grandpy'], False),
    #      (BehaviorParams('', 1).user_behavior['grandpy_status_code'], 'mannerless'),
    #      (BehaviorParams('', 1).user_behavior['behavior_level'], 'presentation'),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_incivility'], 2),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_indecency'], 0),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_indecency2'], 0),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_incomprehension'], 0),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_incomprehension2'], 0),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_entries'], 0)])
    # def test_main_incivility_to_2(self, behavior_status_returned, behavior_status):
    #     main.main('ou se trouve openClassrooms', db_number=1)
    #     main.main('ou se trouve openClassrooms', db_number=1)
    #     assert behavior_status_returned == behavior_status
    #
    # @pytest.mark.skip()
    # @pytest.mark.parametrize(
    #     "behavior_status_returned, behavior_status",
    #     [(BehaviorParams('', 1).user_behavior['has_user_incivility_status'], True),
    #      (BehaviorParams('', 1).user_behavior['has_user_indecency_status'], False),
    #      (BehaviorParams('', 1).user_behavior['has_user_indecency_status2'], False),
    #      (BehaviorParams('', 1).user_behavior['has_user_incomprehension_status'], False),
    #      (BehaviorParams('', 1).user_behavior['has_user_incomprehension_status2'], False),
    #      (BehaviorParams('', 1).user_behavior['has_fatigue_quotas_of_grandpy'], True),
    #      (BehaviorParams('', 1).user_behavior['grandpy_status_code'], 'incivility_limit'),
    #      (BehaviorParams('', 1).user_behavior['behavior_level'], 'presentation'),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_incivility'], 3),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_indecency'], 0),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_indecency2'], 0),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_incomprehension'], 0),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_incomprehension2'], 0),
    #      (BehaviorParams('', 1).user_behavior['number_of_user_entries'], 0)])
    # def test_main_incivility_to_3(self, behavior_status_returned, behavior_status):
    #     main.main('ou se trouve openClassrooms', db_number=1)
    #     main.main('ou se trouve openClassrooms', db_number=1)
    #     main.main('ou se trouve openClassrooms', db_number=1)
    #     main.main('ou se trouve openClassrooms', db_number=1)
    #     main.main('ou se trouve openClassrooms', db_number=1)
    #     assert behavior_status_returned == behavior_status

    @pytest.mark.skip()
    def test_main_indecency(self):
        presentation_user = main.main('dinosaure', db_number=1)
        assert presentation_user.user_behavior['has_user_incivility_status']
        assert presentation_user.user_behavior['number_of_user_indecency'] == 1

    @pytest.mark.skip()
    def test_main_indecency_to_2(self):
        main.main('vieux', db_number=1)
        presentation_user = main.main('dinosaure', db_number=1)
        assert presentation_user.user_behavior['has_user_indecency_status']
        assert presentation_user.user_behavior['number_of_user_indecency'] == 2

    @pytest.mark.skip()
    def test_main_indecency_to_3(self):
        main.main('vieux', db_number=1)
        main.main('gateux', db_number=1)
        presentation_user = main.main('senile', db_number=1)
        assert presentation_user.user_behavior['has_user_indecency_status']
        assert not presentation_user.user_behavior['has_fatigue_quotas_of_grandpy']
        assert presentation_user.user_behavior['number_of_user_indecency'] == 3

        presentation_user = main.main('ancetre', db_number=1)
        assert presentation_user.user_behavior['has_user_indecency_status']
        assert presentation_user.user_behavior['has_fatigue_quotas_of_grandpy']
        assert presentation_user.user_behavior['number_of_user_indecency'] == 3

    @pytest.mark.skip()
    def test_main_incomprehension(self, monkeypatch):
        expected_mock_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_mock_result))
        presentation_user_incomprehension = main.main('', db_number=1)
        assert presentation_user_incomprehension.user_behavior['has_user_incivility_status']
        assert presentation_user_incomprehension.user_behavior['number_of_user_indecency'] == 1

    @pytest.mark.skip()
    def test_main_incomprehension_to_2(self, monkeypatch):
        expected_mock_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_mock_result))
        main.main('', db_number=1)
        presentation_user_incomprehension = main.main('', db_number=1)
        assert presentation_user_incomprehension.user_behavior['has_user_incivility_status']
        assert presentation_user_incomprehension.user_behavior['number_of_user_indecency'] == 2
