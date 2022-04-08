#!/usr/bin/env python
import requests
from mock_api import get_mockreturn
import google_api
import main


class TestMain:

    @staticmethod
    def setup_method():
        main.Conversation('', 1).database_init_ordered()

    # 7) DONE correct query X1
    def test_incorrect_presentation_user(self):
        # incorrect presentation of the user ==> question without ('bonjour'...)
        poor_presentation = main.main('ou se trouve openClassrooms', db_number=1)
        # has_user_incivility_status == True
        assert poor_presentation.user_behavior[
            poor_presentation.__class__.get_user_behavior_key(0)
        ]
        # has_user_indecency_status == False
        assert not poor_presentation.user_behavior[
            poor_presentation.__class__.get_user_behavior_key(1)
        ]
        # has_user_incomprehension_status == False
        assert not poor_presentation.user_behavior[
            poor_presentation.__class__.get_user_behavior_key(2)
        ]
        # has_fatigue_quotas_of_grandpy == False
        assert not poor_presentation.user_behavior[
            poor_presentation.__class__.get_user_behavior_key(3)
        ]
        # grandpy_status_code == 'mannerless'
        assert poor_presentation.user_behavior[
                   poor_presentation.__class__.get_user_behavior_key(4)
               ] == 'mannerless'
        # number_of_user_incivility == 1
        assert poor_presentation.user_behavior[
                   poor_presentation.__class__.get_user_behavior_key(5)
               ] == 1
        # number_of_user_indecency == 0
        assert poor_presentation.user_behavior[
                   poor_presentation.__class__.get_user_behavior_key(6)
               ] == 0
        # number_of_user_incomprehension == 0
        assert poor_presentation.user_behavior[
                   poor_presentation.__class__.get_user_behavior_key(7)
               ] == 0
        # number_of_user_entries == 0
        assert poor_presentation.user_behavior[
                   poor_presentation.__class__.get_user_behavior_key(8)
               ] == 0

    def test_correct_presentation_user(self):
        # correct presentation of the user ==> ('bonjour'....)
        dialogue_of_presentation = main.main('bonjour', db_number=1)
        # has_user_incivility_status == False
        assert not dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(0)
        ]
        # has_user_indecency_status == False
        assert not dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(1)
        ]
        # has_user_incomprehension_status == False
        assert not dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(2)
        ]
        # has_fatigue_quotas_of_grandpy == False
        assert not dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(3)
        ]
        # grandpy_status_code == 'user_question'
        assert dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(4)
        ] == 'user_question'
        # number_of_user_incivility == 0
        assert dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(5)
        ] == 0
        # number_of_user_indecency == 0
        assert dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(6)
        ] == 0
        # number_of_user_incomprehension == 0
        assert dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(7)
        ] == 0
        # number_of_user_entries == 0
        assert dialogue_of_presentation.user_behavior[
            dialogue_of_presentation.__class__.get_user_behavior_key(8)
        ] == 0

    def test_correct_user_request_X1(self, monkeypatch):
        # correct presentation of the user ==> ('bonjour'....)
        first_request = main.main('bonjour', db_number=1)
        # correct presentation of the user ==> question with ('bonjour'...)
        first_request = main.main('ou se trouve openClassrooms', db_number=1)
        # has_user_incivility_status == False
        assert not first_request.user_behavior[
            first_request.__class__.get_user_behavior_key(0)
        ]
        # has_user_indecency_status == False
        assert not first_request.user_behavior[
            first_request.__class__.get_user_behavior_key(1)
        ]
        # has_user_incomprehension_status == False
        assert not first_request.user_behavior[
            first_request.__class__.get_user_behavior_key(2)
        ]
        # has_fatigue_quotas_of_grandpy == False
        assert not first_request.user_behavior[
            first_request.__class__.get_user_behavior_key(3)
        ]
        # grandpy_status_code == 'user_question'
        assert first_request.user_behavior[
                   first_request.__class__.get_user_behavior_key(4)
               ] == 'user_question'
        # number_of_user_incivility == 0
        assert first_request.user_behavior[
                   first_request.__class__.get_user_behavior_key(5)
               ] == 0
        # number_of_user_indecency == 0
        assert first_request.user_behavior[
                   first_request.__class__.get_user_behavior_key(6)
               ] == 0
        # number_of_user_incomprehension == 0
        assert first_request.user_behavior[
                   first_request.__class__.get_user_behavior_key(7)
               ] == 0
        # number_of_user_entries == 1
        assert first_request.user_behavior[
                   first_request.__class__.get_user_behavior_key(8)
               ] == 1
        expected_result1 = {
            'candidates': [{'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}],
            'status': 'OK'
        }
        expected_result2 = {
            'html_attributions': [],
            'result': {
                'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                'geometry': {
                    'location': {'lat': 48.8975156, 'lng': 2.3833993},
                    'viewport': {
                            'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                            'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}
                     }
                }
            },
            'status': 'OK'
        }

        mock_result1 = expected_result1
        mockreturn1 = get_mockreturn(mock_result1)
        monkeypatch.setattr(requests, 'get', mockreturn1)
        place_id = google_api.get_placeid_from_address('openClassrooms')

        mock_result2 = expected_result2
        mockreturn2 = get_mockreturn(mock_result2)
        monkeypatch.setattr(requests, 'get', mockreturn2)
        address_placeid = google_api.get_address_api_from_placeid('ChIJIZX8lhRu5kcRGwYk8Ce3Vc8')

        assert expected_result1 == place_id
        assert expected_result2 == address_placeid

    def test_correct_user_request_X5(self, monkeypatch):
        # correct presentation of the user ==> ('bonjour'....)
        request = main.main('bonjour', db_number=1)
        # has_user_incivility_status == False
        assert not request.user_behavior[request.__class__.get_user_behavior_key(0)]
        # has_user_indecency_status == False
        assert not request.user_behavior[request.__class__.get_user_behavior_key(1)]
        # has_user_incomprehension_status == False
        assert not request.user_behavior[request.__class__.get_user_behavior_key(2)]
        # has_fatigue_quotas_of_grandpy == False
        assert not request.user_behavior[request.__class__.get_user_behavior_key(3)]
        # grandpy_status_code == 'user_question'
        assert request.user_behavior[request.__class__.get_user_behavior_key(4)] == 'user_question'
        # number_of_user_incivility == 0
        assert request.user_behavior[request.__class__.get_user_behavior_key(5)] == 0
        # number_of_user_indecency == 0
        assert request.user_behavior[request.__class__.get_user_behavior_key(6)] == 0
        # number_of_user_incomprehension == 0
        assert request.user_behavior[request.__class__.get_user_behavior_key(7)] == 0
        # correct presentation of the user ==> question with ('bonjour'...)
        request = main.main('ou se trouve openClassrooms', db_number=1)
        print(f'1 = {request.user_behavior[request.__class__.get_user_behavior_key(8)]}')
        # number_of_user_entries == 1
        assert request.user_behavior[request.__class__.get_user_behavior_key(8)] == 1
        request = main.main('ou se trouve openClassrooms', db_number=1)
        print(f'2 = {request.user_behavior[request.__class__.get_user_behavior_key(8)]}')
        # number_of_user_entries == 2
        assert request.user_behavior[request.__class__.get_user_behavior_key(8)] == 2
        request = main.main('ou se trouve openClassrooms', db_number=1)
        print(f'3 = {request.user_behavior[request.__class__.get_user_behavior_key(8)]}')
        # number_of_user_entries == 3
        assert request.user_behavior[request.__class__.get_user_behavior_key(8)] == 3
        request = main.main('ou se trouve openClassrooms', db_number=1)
        print(f'4 = {request.user_behavior[request.__class__.get_user_behavior_key(8)]}')
        # number_of_user_entries == 4
        assert request.user_behavior[request.__class__.get_user_behavior_key(8)] == 4
        request = main.main('ou se trouve openClassrooms', db_number=1)
        print(f'5 = {request.user_behavior[request.__class__.get_user_behavior_key(8)]}')
        # number_of_user_entries == 5
        assert request.user_behavior[request.__class__.get_user_behavior_key(8)] == 5
        expected_result1 = {
            'candidates': [{'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}],
            'status': 'OK'
        }
        expected_result2 = {
            'html_attributions': [],
            'result': {
                'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                'geometry': {
                    'location': {'lat': 48.8975156, 'lng': 2.3833993},
                    'viewport': {
                            'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                            'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}
                     }
                }
            },
            'status': 'OK'
        }

        mock_result1 = expected_result1
        mockreturn1 = get_mockreturn(mock_result1)
        monkeypatch.setattr(requests, 'get', mockreturn1)
        place_id = google_api.get_placeid_from_address('openClassrooms')

        mock_result2 = expected_result2
        mockreturn2 = get_mockreturn(mock_result2)
        monkeypatch.setattr(requests, 'get', mockreturn2)
        address_placeid = google_api.get_address_api_from_placeid('ChIJIZX8lhRu5kcRGwYk8Ce3Vc8')

        assert expected_result1 == place_id
        assert expected_result2 == address_placeid

    # 9) TODO correct query X10
    # def test_correct_user_request_X10(self, monkeypatch):
    #     # correct presentation of the user ==> ('bonjour'....)
    #     request = main.main('bonjour', db_number=1)
    #     # has_user_incivility_status == False
    #     assert not request.user_behavior[request.__class__.get_user_behavior_key(0)]
    #     # has_user_indecency_status == False
    #     assert not request.user_behavior[request.__class__.get_user_behavior_key(1)]
    #     # has_user_incomprehension_status == False
    #     assert not request.user_behavior[request.__class__.get_user_behavior_key(2)]
    #     # has_fatigue_quotas_of_grandpy == False
    #     assert not request.user_behavior[request.__class__.get_user_behavior_key(3)]
    #     # grandpy_status_code == 'user_question'
    #     assert request.user_behavior[request.__class__.get_user_behavior_key(4)] == 'user_question'
    #     # number_of_user_incivility == 0
    #     assert request.user_behavior[request.__class__.get_user_behavior_key(5)] == 0
    #     # number_of_user_indecency == 0
    #     assert request.user_behavior[request.__class__.get_user_behavior_key(6)] == 0
    #     # number_of_user_incomprehension == 0
    #     assert request.user_behavior[request.__class__.get_user_behavior_key(7)] == 0
    #     # correct presentation of the user ==> question with ('bonjour'...)
    #     request = main.main('ou se trouve openClassrooms', db_number=1)
    #     print(f'1 = {request.user_behavior[request.__class__.get_user_behavior_key(8)]}')
    #     # number_of_user_entries == 1
    #     assert request.user_behavior[request.__class__.get_user_behavior_key(8)] == 1
    #     request = main.main('ou se trouve openClassrooms', db_number=1)
    #     print(f'2 = {request.user_behavior[request.__class__.get_user_behavior_key(8)]}')
    #     # number_of_user_entries == 2
    #     assert request.user_behavior[request.__class__.get_user_behavior_key(8)] == 2
    #     request = main.main('ou se trouve openClassrooms', db_number=1)
    #     print(f'3 = {request.user_behavior[request.__class__.get_user_behavior_key(8)]}')
    #     # number_of_user_entries == 3
    #     assert request.user_behavior[request.__class__.get_user_behavior_key(8)] == 3
    #     request = main.main('ou se trouve openClassrooms', db_number=1)
    #     print(f'4 = {request.user_behavior[request.__class__.get_user_behavior_key(8)]}')
    #     # number_of_user_entries == 4
    #     assert request.user_behavior[request.__class__.get_user_behavior_key(8)] == 4
    #     request = main.main('ou se trouve openClassrooms', db_number=1)
    #     print(f'5 = {request.user_behavior[request.__class__.get_user_behavior_key(8)]}')
    #     # number_of_user_entries == 5
    #     assert request.user_behavior[request.__class__.get_user_behavior_key(8)] == 5
    #     expected_result1 = {
    #         'candidates': [{'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}],
    #         'status': 'OK'
    #     }
    #     expected_result2 = {
    #         'html_attributions': [],
    #         'result': {
    #             'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
    #             'geometry': {
    #                 'location': {'lat': 48.8975156, 'lng': 2.3833993},
    #                 'viewport': {
    #                     'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
    #                     'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}
    #                 }
    #             }
    #         },
    #         'status': 'OK'
    #     }
    #
    #     mock_result1 = expected_result1
    #     mockreturn1 = get_mockreturn(mock_result1)
    #     monkeypatch.setattr(requests, 'get', mockreturn1)
    #     place_id = google_api.get_placeid_from_address('openClassrooms')
    #
    #     mock_result2 = expected_result2
    #     mockreturn2 = get_mockreturn(mock_result2)
    #     monkeypatch.setattr(requests, 'get', mockreturn2)
    #     address_placeid = google_api.get_address_api_from_placeid('ChIJIZX8lhRu5kcRGwYk8Ce3Vc8')
    #
    #     assert expected_result1 == place_id
    #     assert expected_result2 == address_placeid

    # 11) TODO incivility query X1
    # 13) TODO incivility query X3
    # 15) TODO indecency query X1
    # 17) TODO indecency query X3
    # 19) TODO incomprehension query X1
    # 21) TODO incomprehension query X3
    # 23) TODO incivility conditional
    # 25) TODO indecency conditional
    # 27) TODO incomprehension conditional
