from . import requests
from . import pytest
from . import erasing_data
from . import BehaviorParams


# @pytest.mark.skip()
class TestBehaviorParams:
    @staticmethod
    def setup_method():
        erasing_data(1)

    @pytest.mark.parametrize(
        "behavior_status_returned, behavior_status ",
        [(BehaviorParams.get_user_behavior_key('has_user_incivility_status'),
          BehaviorParams.USER_BEHAVIOR_DEFAULT_DATA_KEYS[0]),
         (BehaviorParams.get_user_behavior_key('has_user_indecency_status'),
          BehaviorParams.USER_BEHAVIOR_DEFAULT_DATA_KEYS[1]),
         (BehaviorParams.get_user_behavior_key('has_user_indecency_status2'),
          BehaviorParams.USER_BEHAVIOR_DEFAULT_DATA_KEYS[2]),
         (BehaviorParams.get_user_behavior_key('has_user_incomprehension_status'),
          BehaviorParams.USER_BEHAVIOR_DEFAULT_DATA_KEYS[3]),
         (BehaviorParams.get_user_behavior_key('has_user_incomprehension_status2'),
          BehaviorParams.USER_BEHAVIOR_DEFAULT_DATA_KEYS[4]),
         (BehaviorParams.get_user_behavior_key('has_fatigue_quotas_of_grandpy'),
          BehaviorParams.USER_BEHAVIOR_DEFAULT_DATA_KEYS[5]),
         (BehaviorParams.get_user_behavior_key('grandpy_status_code'),
          BehaviorParams.USER_BEHAVIOR_DEFAULT_DATA_KEYS[6]),
         (BehaviorParams.get_user_behavior_key('behavior_level'),
          BehaviorParams.USER_BEHAVIOR_DEFAULT_DATA_KEYS[7]),
         (BehaviorParams.get_user_behavior_key('number_of_user_incivility'),
          BehaviorParams.USER_BEHAVIOR_DEFAULT_DATA_KEYS[8]),
         (BehaviorParams.get_user_behavior_key('number_of_user_indecency'),
          BehaviorParams.USER_BEHAVIOR_DEFAULT_DATA_KEYS[9]),
         (BehaviorParams.get_user_behavior_key('number_of_user_indecency2'),
          BehaviorParams.USER_BEHAVIOR_DEFAULT_DATA_KEYS[10]),
         (BehaviorParams.get_user_behavior_key('number_of_user_incomprehension'),
          BehaviorParams.USER_BEHAVIOR_DEFAULT_DATA_KEYS[11]),
         (BehaviorParams.get_user_behavior_key('number_of_user_incomprehension2'),
          BehaviorParams.USER_BEHAVIOR_DEFAULT_DATA_KEYS[12]),
         (BehaviorParams.get_user_behavior_key('number_of_user_entries'),
          BehaviorParams.USER_BEHAVIOR_DEFAULT_DATA_KEYS[13])])
    def test_get_user_behavior_key(self, behavior_status_returned, behavior_status):
        assert behavior_status_returned == behavior_status

    # @pytest.mark.skip()
    @pytest.mark.parametrize(
        "response_status_returned, grandpy_response_status",
        [(BehaviorParams.get_grandpy_status_key('home'),
          BehaviorParams.GRANDPY_STATUS_DATA_KEYS[0]),
         (BehaviorParams.get_grandpy_status_key('benevolent'),
          BehaviorParams.GRANDPY_STATUS_DATA_KEYS[1]),
         (BehaviorParams.get_grandpy_status_key('response'),
          BehaviorParams.GRANDPY_STATUS_DATA_KEYS[2]),
         (BehaviorParams.get_grandpy_status_key('tired'),
          BehaviorParams.GRANDPY_STATUS_DATA_KEYS[3]),
         (BehaviorParams.get_grandpy_status_key('inconsistency'),
          BehaviorParams.GRANDPY_STATUS_DATA_KEYS[4]),
         (BehaviorParams.get_grandpy_status_key('mannerless'),
          BehaviorParams.GRANDPY_STATUS_DATA_KEYS[5]),
         (BehaviorParams.get_grandpy_status_key('disrespectful'),
          BehaviorParams.GRANDPY_STATUS_DATA_KEYS[6]),
         (BehaviorParams.get_grandpy_status_key('incivility_limit'),
          BehaviorParams.GRANDPY_STATUS_DATA_KEYS[7]),
         (BehaviorParams.get_grandpy_status_key('indecency_limit'),
          BehaviorParams.GRANDPY_STATUS_DATA_KEYS[8]),
         (BehaviorParams.get_grandpy_status_key('incomprehension_limit'),
          BehaviorParams.GRANDPY_STATUS_DATA_KEYS[9]),
         (BehaviorParams.get_grandpy_status_key('response_limit'),
          BehaviorParams.GRANDPY_STATUS_DATA_KEYS[10]),
         (BehaviorParams.get_grandpy_status_key('exhausted'),
          BehaviorParams.GRANDPY_STATUS_DATA_KEYS[11])])
    def test_get_grandpy_status_key(self, response_status_returned, grandpy_response_status):
        assert response_status_returned == grandpy_response_status

    # @pytest.mark.skip()
    @pytest.mark.parametrize(
        "grandpy_response_returned, grandpy_response",
        [(BehaviorParams.read_grandpy_answer('home'),
          BehaviorParams.GRANDPY_STATUS_DATA[BehaviorParams.get_grandpy_status_key('home')]),
         (BehaviorParams.read_grandpy_answer('benevolent'),
          BehaviorParams.GRANDPY_STATUS_DATA[BehaviorParams.get_grandpy_status_key('benevolent')]),
         (BehaviorParams.read_grandpy_answer('response'),
          BehaviorParams.GRANDPY_STATUS_DATA[BehaviorParams.get_grandpy_status_key('response')]),
         (BehaviorParams.read_grandpy_answer('tired'),
          BehaviorParams.GRANDPY_STATUS_DATA[BehaviorParams.get_grandpy_status_key('tired')]),
         (BehaviorParams.read_grandpy_answer('inconsistency'),
          BehaviorParams.GRANDPY_STATUS_DATA[
              BehaviorParams.get_grandpy_status_key('inconsistency')]),
         (BehaviorParams.read_grandpy_answer('mannerless'),
          BehaviorParams.GRANDPY_STATUS_DATA[BehaviorParams.get_grandpy_status_key('mannerless')]),
         (BehaviorParams.read_grandpy_answer('disrespectful'),
          BehaviorParams.GRANDPY_STATUS_DATA[
              BehaviorParams.get_grandpy_status_key('disrespectful')]),
         (BehaviorParams.read_grandpy_answer('incivility_limit'),
          BehaviorParams.GRANDPY_STATUS_DATA[
              BehaviorParams.get_grandpy_status_key('incivility_limit')]),
         (BehaviorParams.read_grandpy_answer('indecency_limit'),
          BehaviorParams.GRANDPY_STATUS_DATA[
              BehaviorParams.get_grandpy_status_key('indecency_limit')]),
         (BehaviorParams.read_grandpy_answer('incomprehension_limit'),
          BehaviorParams.GRANDPY_STATUS_DATA[
               BehaviorParams.get_grandpy_status_key('incomprehension_limit')]),
         (BehaviorParams.read_grandpy_answer('response_limit'),
          BehaviorParams.GRANDPY_STATUS_DATA[
               BehaviorParams.get_grandpy_status_key('response_limit')]),
         (BehaviorParams.read_grandpy_answer('exhausted'),
          BehaviorParams.GRANDPY_STATUS_DATA[BehaviorParams.get_grandpy_status_key('exhausted')])])
    def test_read_grandpy_answer(self, grandpy_response_returned, grandpy_response):
        assert grandpy_response_returned == grandpy_response

    def test_lower_and_split_user_entry(self):
        user_request = BehaviorParams('Bonjour', 1)
        expected_result = ['bonjour']
        result = user_request.lower_and_split_user_entry()
        assert expected_result == result

    def test_get_request_parser(self):
        user_request = BehaviorParams('ou se trouve openClassrooms', 1)
        user_request.get_user_request_parser()
        user_entry = user_request.user_entry
        assert user_entry == 'openClassrooms'
