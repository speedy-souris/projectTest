#!/usr/bin/env python
import requests
from mock_api import get_mockreturn
import main


def setup_method():
    main.Conversation.database_init(1)


class TestMain:
    # 7) DONE correct query X1
    def test_correct_user_request_X1(self):
        dialog = main.main('bonjour', db_number=1)
        expected_result = (False, 'user_question')
        result = (
            dialog.user_behavior[dialog.__class__.USER_BEHAVIOR_DEFAULT_DATA_KEY[0]],
            dialog.user_behavior[dialog.__class__.USER_BEHAVIOR_DEFAULT_DATA_KEY[4]]
        )
        print(f"user_behavior {dialog.user_behavior}")
        assert result == expected_result

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



