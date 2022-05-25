import pytest
from . import get_place_id_googleMap_api_mockreturn
from . import get_address_googleMap_api_mockreturn
from . import google_api
from . import main
from . import erasing_data


# @pytest.mark.skip()
class TestQuestionMain:
    @staticmethod
    def setup_method():
        erasing_data(1)

    # @pytest.mark.skip()
    def test_correct_user_request_to_X1(self, monkeypatch):
        # correct presentation of the user ==> ('bonjour'....)
        user_presentation = main('bonjour', db_number=1)

        # has_user_incivility_status == False
        assert not user_presentation.user_behavior[
            user_presentation.__class__.get_user_behavior_key('has_user_incivility_status')]
        # has_user_indecency_status == False
        assert not user_presentation.user_behavior[
            user_presentation.__class__.get_user_behavior_key('has_user_indecency_status')]
        # has_user_incomprehension_status == False
        assert not user_presentation.user_behavior[
            user_presentation.__class__.get_user_behavior_key('has_user_incomprehension_status')]
        # has_fatigue_quotas_of_grandpy == False
        assert not user_presentation.user_behavior[
            user_presentation.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]
        # grandpy_status_code == 'benevolent'
        assert user_presentation.user_behavior[
            user_presentation.__class__.get_user_behavior_key('grandpy_status_code')]\
            == 'benevolent'
        # number_of_user_incivility == 0
        assert user_presentation.user_behavior[
            user_presentation.__class__.get_user_behavior_key('number_of_user_incivility')]\
            == 0
        # number_of_user_indecency == 0
        assert user_presentation.user_behavior[
            user_presentation.__class__.get_user_behavior_key('number_of_user_indecency')]\
            == 0
        # number_of_user_incomprehension == 0
        assert user_presentation.user_behavior[
            user_presentation.__class__.get_user_behavior_key('number_of_user_incomprehension')]\
            == 0
        # number_of_user_entries == 0
        assert user_presentation.user_behavior[
            user_presentation.__class__.get_user_behavior_key('number_of_user_entries')] == 0

        # correct presentation of the user ==> question with ('bonjour'...)
        # level1 GoogleMap api
        expected_result1 = {
            'candidates': [{'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}], 'status': 'OK'}
        # level2 GoogleMap api
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
        # Mock level1 GoogleMap api
        monkeypatch.setattr(
            google_api, 'get_placeid_from_address',
            get_place_id_googleMap_api_mockreturn(expected_result1))
        # Mock level2 GoogleMap api
        monkeypatch.setattr(
            google_api, 'get_address_api_from_placeid',
            get_address_googleMap_api_mockreturn(expected_result2))
        first_request = main('ou se trouve openClassrooms', db_number=1)
        first_request.calculate_the_indecency_status()
        first_request.calculate_the_incomprehension_status()

        # has_user_incivility_status == False
        assert not first_request.user_behavior[
            first_request.__class__.get_user_behavior_key('has_user_incivility_status')]
        # has_user_indecency_status == False
        assert not first_request.user_behavior[
            first_request.__class__.get_user_behavior_key('has_user_indecency_status')]
        # has_user_incomprehension_status == False
        assert not first_request.user_behavior[
            first_request.__class__.get_user_behavior_key('has_user_incomprehension_status')]
        # has_fatigue_quotas_of_grandpy == False
        assert not first_request.user_behavior[
            first_request.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]
        # grandpy_status_code == 'response'
        assert first_request.user_behavior[
            first_request.__class__.get_user_behavior_key('grandpy_status_code')] == 'response'
        # number_of_user_incivility == 0
        assert first_request.user_behavior[
            first_request.__class__.get_user_behavior_key('number_of_user_incivility')] == 0
        # number_of_user_indecency == 0
        assert first_request.user_behavior[
            first_request.__class__.get_user_behavior_key('number_of_user_indecency')] == 0
        # number_of_user_incomprehension == 0
        assert first_request.user_behavior[
            first_request.__class__.get_user_behavior_key('number_of_user_incomprehension')] == 0
        # number_of_user_entries == 1
        assert first_request.user_behavior[
            first_request.__class__.get_user_behavior_key('number_of_user_entries')] == 1

    @pytest.mark.skip()
    def test_correct_user_request_X5(self, monkeypatch):
        # correct presentation of the user ==> ('bonjour'....)
        main('bonjour', db_number=1)
        expected_result1 = {
            'candidates': [{'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}], 'status': 'OK'}
        # level2 GoogleMap api
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
        # Mock level1 GoogleMap api
        monkeypatch.setattr(
            google_api, 'get_placeid_from_address',
            get_place_id_googleMap_api_mockreturn(expected_result1))
        # Mock level2 GoogleMap api
        monkeypatch.setattr(
            google_api, 'get_address_api_from_placeid',
            get_address_googleMap_api_mockreturn(expected_result2))
        main('ou se trouve openClassrooms', db_number=1)
        main('ou se trouve openClassrooms', db_number=1)
        main('ou se trouve openClassrooms', db_number=1)
        main('ou se trouve openClassrooms', db_number=1)
        main('ou se trouve openClassrooms', db_number=1)
        request_to_X5 = main('ou se trouve openClassrooms', db_number=1)
        request_to_X5.calculate_the_indecency_status()
        request_to_X5.calculate_the_incomprehension_status()

        # has_user_incivility_status == False
        assert not request_to_X5.user_behavior[
            request_to_X5.__class__.get_user_behavior_key('has_user_incivility_status')]
        # has_user_indecency_status == False
        assert not request_to_X5.user_behavior[
            request_to_X5.__class__.get_user_behavior_key('has_user_indecency_status')]
        # has_user_incomprehension_status == False
        assert not request_to_X5.user_behavior[
            request_to_X5.__class__.get_user_behavior_key('has_user_incomprehension_status')]
        # has_fatigue_quotas_of_grandpy == False
        assert not request_to_X5.user_behavior[
            request_to_X5.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]
        # grandpy_status_code == 'tired'
        assert request_to_X5.user_behavior[
            request_to_X5.__class__.get_user_behavior_key('grandpy_status_code')] == 'tired'
        # number_of_user_incivility == 0
        assert request_to_X5.user_behavior[
            request_to_X5.__class__.get_user_behavior_key('number_of_user_incivility')] == 0
        # number_of_user_indecency == 0
        assert request_to_X5.user_behavior[
            request_to_X5.__class__.get_user_behavior_key('number_of_user_indecency')] == 0
        # number_of_user_incomprehension == 0
        assert request_to_X5.user_behavior[
            request_to_X5.__class__.get_user_behavior_key('number_of_user_incomprehension')] == 0
        # number_of_user_entries == 5
        assert request_to_X5.user_behavior[
            request_to_X5.__class__.get_user_behavior_key('number_of_user_entries')] == 5

    @pytest.mark.skip()
    def test_correct_user_request_X9(self, monkeypatch):
        # correct presentation of the user ==> ('bonjour'....)
        main('bonjour', db_number=1)
        expected_result1 = {
            'candidates': [{'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}], 'status': 'OK'}
        # level2 GoogleMap api
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
        # Mock level1 GoogleMap api
        monkeypatch.setattr(
            google_api, 'get_placeid_from_address',
            get_place_id_googleMap_api_mockreturn(expected_result1))
        # Mock level2 GoogleMap api
        monkeypatch.setattr(
            google_api, 'get_address_api_from_placeid',
            get_address_googleMap_api_mockreturn(expected_result2))
        main('ou se trouve openClassrooms', db_number=1)
        main('ou se trouve openClassrooms', db_number=1)
        main('ou se trouve openClassrooms', db_number=1)
        main('ou se trouve openClassrooms', db_number=1)
        main('ou se trouve openClassrooms', db_number=1)
        main('ou se trouve openClassrooms', db_number=1)
        main('ou se trouve openClassrooms', db_number=1)
        main('ou se trouve openClassrooms', db_number=1)
        main('ou se trouve openClassrooms', db_number=1)
        request_to_X9 = main('ou se trouve openClassrooms', db_number=1)
        request_to_X9.calculate_the_indecency_status()
        request_to_X9.calculate_the_incomprehension_status()

        # has_user_incivility_status == False
        assert not request_to_X9.user_behavior[
            request_to_X9.__class__.get_user_behavior_key('has_user_incivility_status')]
        # has_user_indecency_status == False
        assert not request_to_X9.user_behavior[
            request_to_X9.__class__.get_user_behavior_key('has_user_indecency_status')]
        # has_user_incomprehension_status == False
        assert not request_to_X9.user_behavior[
            request_to_X9.__class__.get_user_behavior_key('has_user_incomprehension_status')]
        # has_fatigue_quotas_of_grandpy == False
        assert not request_to_X9.user_behavior[
            request_to_X9.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]
        # grandpy_status_code == 'response'
        assert request_to_X9.user_behavior[
            request_to_X9.__class__.get_user_behavior_key('grandpy_status_code')] == 'response'
        # number_of_user_incivility == 0
        assert request_to_X9.user_behavior[
            request_to_X9.__class__.get_user_behavior_key('number_of_user_incivility')] == 0
        # number_of_user_indecency == 0
        assert request_to_X9.user_behavior[
            request_to_X9.__class__.get_user_behavior_key('number_of_user_indecency')] == 0
        # number_of_user_incomprehension == 0
        assert request_to_X9.user_behavior[
            request_to_X9.__class__.get_user_behavior_key('number_of_user_incomprehension')] == 0
        # number_of_user_entries == 9
        assert request_to_X9.user_behavior[
            request_to_X9.__class__.get_user_behavior_key('number_of_user_entries')] == 9

    # 23) TODO incivility conditional
    # 25) TODO indecency conditional
    # 27) TODO incomprehension conditional
