#!/usr/bin/env python
import requests
from mock_api import get_mockreturn
import google_api
import main


def setup_method():
    main.Conversation.database_init(1)


class TestMain:
    # 7) DONE correct query X1
    def test_correct_user_request_X1(self, monkeypatch):
        dialog = main.main('bonjour', db_number=1)
        user_incivility_status, grandpy_status_code = False, 'user_question'
        expected_result = (user_incivility_status, grandpy_status_code)

        user_incivility_status_to_false, grandpy_status_code_user_question = \
            dialog.user_behavior[dialog.__class__.get_user_behavior_key(0)], \
            dialog.user_behavior[dialog.__class__.get_user_behavior_key(4)]

        result = (user_incivility_status_to_false, grandpy_status_code_user_question)
        assert result == expected_result
        # dialog = main.main('ou se trouve openClassrooms', db_number=1)
        # expected_result = (
        #     False, False, False, 'response', 1,
        #     {
        #         'candidates': [{'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'}],
        #         'status': 'OK'
        #     },
        #     {
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
        # )
        # mock_result = expected_result
        # mockreturn = get_mockreturn(mock_result)
        # monkeypatch.setattr(requests, 'get', mockreturn)
        # place_id = google_api.get_placeid_from_address('openClassrooms')
        # address_placeid = google_api.get_address_api_from_placeid('ChIJIZX8lhRu5kcRGwYk8Ce3Vc8')
        #
        # result = (
        #     dialog.user_behavior[dialog.__class__.get_user_behavior_key(0)],
        #     dialog.user_behavior[dialog.__class__.get_user_behavior_key(1)],
        #     dialog.user_behavior[dialog.__class__.get_user_behavior_key(2)],
        #     dialog.user_behavior[dialog.__class__.get_user_behavior_key(4)],
        #     dialog.user_behavior[dialog.__class__.get_user_behavior_key(8)],
        #     place_id,
        #     address_placeid
        # )
        # assert result == expected_result

    # 9) TODO correct query X10
    # 11) TODO incivility query X1
    # 13) TODO incivility query X3
    # 15) TODO indecency query X1
    # 17) TODO indecency query X3
    # 19) TODO incomprehension query X1
    # 21) TODO incomprehension query X3
    # 23) TODO incivility conditional
    # 25) TODO indecency conditional
    # 27) TODO incomprehension conditional



