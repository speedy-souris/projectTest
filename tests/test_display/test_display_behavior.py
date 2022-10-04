from . import pytest
from . import RedisDataManagement
from . import Conversation
from . import display_behavior
from src.redis_utilities import get_database_access


# @pytest.mark.skip()
class TestDisplay:
    def setup_method(self):
        self.db_session = RedisDataManagement(db_number=1)
        self.db_session.erasing_data()
        self.chat_session = Conversation('', self.db_session)

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_home(self):
        display_behavior.display_grandpy_status_code_to_home(self.chat_session)
        assert self.chat_session.__class__.read_grandpy_answer('home')\
            == self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('home')]
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('home')

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_benevolent(self):
        display_behavior.display_grandpy_status_code_to_benevolent(self.chat_session)
        assert self.chat_session.__class__.read_grandpy_answer('benevolent')\
            == self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('benevolent')]
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('benevolent')

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_response(self):
        display_behavior.display_grandpy_status_code_to_response(self.chat_session)
        assert self.chat_session.__class__.read_grandpy_answer('response')\
            == self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('response')]
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('response')

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_tired(self):
        display_behavior.display_grandpy_status_code_to_tired(self.chat_session)
        assert self.chat_session.__class__.read_grandpy_answer('tired')\
            == self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('tired')]
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('tired')

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_incomprehension(self):
        display_behavior.display_grandpy_status_code_to_inconsistency(self.chat_session)
        assert self.chat_session.__class__.read_grandpy_answer('inconsistency')\
            == self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('inconsistency')]
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('inconsistency')

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_mannerless(self):
        display_behavior.display_grandpy_status_code_to_mannerless(self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('mannerless')]
        display_response = self.chat_session.__class__.read_grandpy_answer('mannerless')
        display_incivility_status\
            = self.chat_session.user_behavior[
                self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]
        incivility_status\
            = self.chat_session.__class__.get_grandpy_status_key('mannerless')

        assert display_response == response_status
        assert display_incivility_status == incivility_status

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_disrespectful(self):
        display_behavior.display_grandpy_status_code_to_disrespectful(self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('disrespectful')]
        display_response = self.chat_session.__class__.read_grandpy_answer('disrespectful')
        display_indecency_status\
            = self.chat_session.user_behavior[
                self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]
        indecency_status\
            = self.chat_session.__class__.get_grandpy_status_key('disrespectful')

        assert display_response == response_status
        assert display_indecency_status == indecency_status

    def test_display_grandpy_status_code_to_incivility_limit(self):
        display_behavior.display_grandpy_status_code_to_incivility_limit(self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('incivility_limit')]
        display_response = self.chat_session.__class__.read_grandpy_answer('incivility_limit')
        display_incivility_limit_status\
            = self.chat_session.user_behavior[
                self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]
        incivility_limit_status\
            = self.chat_session.__class__.get_grandpy_status_key('incivility_limit')

        assert display_response == response_status
        assert display_incivility_limit_status == incivility_limit_status

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_indecency_limit(self):
        display_behavior.display_grandpy_status_code_to_indecency_limit(self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('indecency_limit')]
        display_response = self.chat_session.__class__.read_grandpy_answer('indecency_limit')
        display_indecency_limit_status\
            = self.chat_session.user_behavior[
                self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]
        indecency_limit_status\
            = self.chat_session.__class__.get_grandpy_status_key('indecency_limit')

        assert display_response == response_status
        assert display_indecency_limit_status == indecency_limit_status

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_incomprehension_limit(self):
        display_behavior.display_grandpy_status_code_to_incomprehension_limit(
            self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('incomprehension_limit')]
        display_response = self.chat_session.__class__.read_grandpy_answer('incomprehension_limit')
        display_incomprehension_limit_status\
            = self.chat_session.user_behavior[
                self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]
        incomprehension_limit_status\
            = self.chat_session.__class__.get_grandpy_status_key('incomprehension_limit')

        assert display_response == response_status
        assert display_incomprehension_limit_status == incomprehension_limit_status

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_exhausted(self):
        display_response =\
            display_behavior.display_grandpy_status_code_to_exhausted(self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('exhausted')]

        assert display_response == response_status

    # @pytest.mark.skip()
    def test_display_last_user_request(self):
        chat_access = get_database_access(db_number=1)
        response_grandpy = self.chat_session.__class__.read_grandpy_answer('response_limit')
        display_behavior.display_last_user_request(self.chat_session, response_grandpy)
        response_grandpy = chat_access.ttl(str(self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]))

        assert response_grandpy == -2
