#!/usr/bin/env python
import requests
from conversation import Conversation


class TestConversation:
    def setup_method(self):
        Conversation.database_init(1)
        self.entry_bonjour = Conversation('bonjour', db_number=1)

    def test_do_this_from_attribut(self):
        user_request = self.entry_bonjour
        expected_result = ['bonjour']
        result = user_request.do_this_from_attribut()
        assert expected_result == result