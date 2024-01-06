from . import requests
from . import pytest
from . import RedisDataManagement
from . import get_mockreturn
from . import expected_result_mock
from . import main

#@pytest.mark.skip()
class TestHomeMain:
    def setup_method(self):
        self.database_object_redis_connect = \
            RedisDataManagement(database_redis_number=1)
        self.database_object_redis_connect.erasing_redis_databases()
        self.database_object_redis_connect.redis_database_init_by_default()

    @staticmethod
    def mock_params(monkeypatch, expected_result_function):
        """mock parameter for monkeypatch"""
        get_candidate_places = expected_result_function(get_candidate_places=True)
        about_a_place = expected_result_function(about_a_place=True)
        get_wikipedia_places = expected_result_function(get_wikipedia_places=True)
        monkeypatch.setattr(
            requests, 'get', get_mockreturn(
                candidate_places_result=get_candidate_places,
                about_a_place_result=about_a_place, 
                wikipedia_places_result=get_wikipedia_places)
        )
    # ~ @pytest.mark.skip()
    def test_incomprehension_request_user_to_1_with_empty_input(self, monkeypatch):
        # incomprehension presentation of the user X1 ==> question with ('bonjour'...)
            expected_mock_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
            get_candidate_places = expected_result_mock(get_candidate_places=True)
            monkeypatch.setattr(
                requests, 'get', get_mockreturn(get_candidate_places))
            presentation_user_incomprehension = main.main(' sqdsqsqdqs', database_redis_number=1)
            # user_behavior['has_user_incomprehension_status'] = True
            assert presentation_user_incomprehension.has_user_incomprehension_status
            # user_behavior['has_fatigue_quotas_of_grandpy'] = False
            assert not presentation_user_incomprehension.has_fatigue_quotas_of_grandpy
            # user_behavior['grandpy_status_code'] = 'incomprehension'
            assert presentation_user_incomprehension.grandpy_status_code == 'incomprehension'
            # user_behavior['number_of_user_entries'] = 0
            assert presentation_user_incomprehension.number_of_user_entries == 0 

    # ~ @pytest.mark.skip()
    def test_correct_presentation_userX1(self, monkeypatch):
        # correct presentation of the user
        self.mock_params(monkeypatch, expected_result_mock)
        dialogue_of_presentation = main.main('ou se trouve openClassrooms', database_redis_number=1)
        # has_fatigue_quotas_of_grandpy == False
        assert not dialogue_of_presentation.has_fatigue_quotas_of_grandpy
        # grandpy_status_code == 'response'
        assert dialogue_of_presentation.grandpy_status_code == 'response'
        # number_of_user_entries == 1
        assert dialogue_of_presentation.number_of_user_entries == 2

    # ~ @pytest.mark.skip()
    def test_correct_presentation_userX10(self, monkeypatch):
        # correct presentation of the user 
        self.mock_params(monkeypatch, expected_result_mock)
        main.main('ou se trouve openClassrooms', database_redis_number=1)
        main.main('ou se trouve openClassrooms', database_redis_number=1)
        main.main('ou se trouve openClassrooms', database_redis_number=1)
        main.main('ou se trouve openClassrooms', database_redis_number=1)
        main.main('ou se trouve openClassrooms', database_redis_number=1)
        main.main('ou se trouve openClassrooms', database_redis_number=1)
        main.main('ou se trouve openClassrooms', database_redis_number=1)
        main.main('ou se trouve openClassrooms', database_redis_number=1)
        main.main('ou se trouve openClassrooms', database_redis_number=1)
        main.main('ou se trouve openClassrooms', database_redis_number=1)
        main.main('ou se trouve openClassrooms', database_redis_number=1)
        dialogue_of_presentation = main.main('ou se trouve openClassrooms', database_redis_number=1)
        print(f"number_entries[test] = {dialogue_of_presentation.number_of_user_entries}")
        # has_fatigue_quotas_of_grandpy == True
        assert dialogue_of_presentation.has_fatigue_quotas_of_grandpy
        # grandpy_status_code == 'exhausted'
        assert dialogue_of_presentation.grandpy_status_code == 'exhausted'
        # number_of_user_entries == 10
        assert dialogue_of_presentation.number_of_user_entries == 10
        # TTL has_fatigue_quotas_of_grandpy > 0
        assert self.database_object_redis_connect.database_connect.ttl('has_fatigue_quotas_of_grandpy') > 0

   
