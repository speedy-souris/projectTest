#!/usr/bin/env python
import requests
from mock_api import get_mockreturn
from conversation import Conversation
import main


def setup_method():
    Conversation.database_init(1)


# class TestBehavior:
#
#     def test_get_grandpy_status(self):
#         expected_message = 'home'
#         user_request = search_address_to_wiki('bonjour')
#         result = user_request.user_behavior['grandpy_code']
#         assert expected_message == result
#
#     def test_grandpy_code(self):
#         expected_message = "Bonjour Mon petit, en quoi puis-je t'aider ?"
#         user_request = search_address_to_wiki('bonjour')
#         grandpy_code = user_request.user_behavior['grandpy_code']
#         result = user_request.GRANDPY_CODE[grandpy_code]
#         assert expected_message == result
