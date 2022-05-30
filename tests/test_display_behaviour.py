from . import pytest
from . import erasing_data
from . import Conversation
from ..src import display_behaviour
from ..src.redis_utilities import get_database_access


# @pytest.mark.skip()
class TestDisplay:
    def setup_method(self):
        erasing_data(1)
        self.chat_session = Conversation('', 1)

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_home(self):
        display_behaviour.display_grandpy_status_code_to_home(self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('home')]
        display_response = self.chat_session.__class__.read_grandpy_answer('home')

        assert display_response == response_status

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_benevolent(self):
        display_behaviour.display_grandpy_status_code_to_benevolent(self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('benevolent')]
        display_response = self.chat_session.__class__.read_grandpy_answer('benevolent')

        assert display_response == response_status

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_response(self):
        display_behaviour.display_grandpy_status_code_to_response(self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('response')]
        display_response = self.chat_session.__class__.read_grandpy_answer('response')

        assert display_response == response_status

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_tired(self):
        display_behaviour.display_grandpy_status_code_to_tired(self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('tired')]
        display_response = self.chat_session.__class__.read_grandpy_answer('tired')

        assert display_response == response_status

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_incomprehension(self):
        display_behaviour.display_grandpy_status_code_to_incomprehension(self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('incomprehension')]
        display_response = self.chat_session.__class__.read_grandpy_answer('incomprehension')

        assert display_response == response_status

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_mannerless(self):
        display_behaviour.display_grandpy_status_code_to_mannerless(self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('mannerless')]
        display_response = self.chat_session.__class__.read_grandpy_answer('mannerless')

        assert display_response == response_status

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_disrespectful(self):
        display_behaviour.display_grandpy_status_code_to_disrespectful(self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('disrespectful')]
        display_response = self.chat_session.__class__.read_grandpy_answer('disrespectful')

        assert display_response == response_status

    def test_display_grandpy_status_code_to_incivility_limit(self):
        display_behaviour.display_grandpy_status_code_to_incivility_limit(self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('incivility_limit')]
        display_response = self.chat_session.__class__.read_grandpy_answer('incivility_limit')

        assert display_response == response_status

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_indecency_limit(self):
        display_behaviour.display_grandpy_status_code_to_indecency_limit(self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('indecency_limit')]
        display_response = self.chat_session.__class__.read_grandpy_answer('indecency_limit')

        assert display_response == response_status

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_incomprehension_limit(self):
        display_behaviour.display_grandpy_status_code_to_incomprehension_limit(
            self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('incomprehension_limit')]
        display_response = self.chat_session.__class__.read_grandpy_answer('incomprehension_limit')

        assert display_response == response_status

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_exhausted(self):
        display_response =\
            display_behaviour.display_grandpy_status_code_to_exhausted(self.chat_session)
        response_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.chat_session.__class__.get_grandpy_status_key('exhausted')]

        assert display_response == response_status

    # @pytest.mark.skip()
    def test_display_last_user_request(self):
        chat_access = get_database_access(db_number=1)
        response_grandpy = self.chat_session.__class__.read_grandpy_answer('response_limit')
        display_behaviour.display_last_user_request(self.chat_session, response_grandpy)
        response_grandpy = chat_access.ttl(str(self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]))

        assert response_grandpy == -2
