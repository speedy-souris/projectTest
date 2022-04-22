#!/usr/bin/env python
from redis_utilities import erasing_data
from main import main
import pytest


# @pytest.mark.skip()
class TestBehavior:
    def setup_method(self):
        erasing_data(1)
        self.chat_session = main('', 1)

    def test_get_user_behavior_key(self):
        grandpy_status = self.chat_session.__class__.get_user_behavior_key(4)
        grandpy_status_value =\
            self.chat_session.__class__.USER_BEHAVIOR_DEFAULT_DATA[grandpy_status]

        assert (grandpy_status, grandpy_status_value) == ('grandpy_status_code', 'home')

    def test_get_grandpy_status_key(self):
        grandpy_status = self.chat_session.__class__.get_grandpy_status_key(4)
        grandpy_status_value = self.chat_session.__class__.read_grandpy_answer(grandpy_status)

        assert (grandpy_status, grandpy_status_value) ==\
               ('incomprehension', "Ha, je ne comprends pas, essaye d'être plus précis ... !")
