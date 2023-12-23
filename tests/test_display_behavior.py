from . import pytest
from . import RedisDataManagement
from . import Conversation
from . import display_behavior


# @pytest.mark.skip()
class TestDisplay:
    def setup_method(self):
        self.db_session = RedisDataManagement(database_redis_number=1)
        self.db_session.erasing_redis_databases()
        self.chat_session = Conversation('', 1)

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_home(self):
        display_behavior.display_grandpy_status_code_to_home(self.chat_session)
        assert self.chat_session.grandpy_status_code == 'home'
        assert self.chat_session.__class__.grandpy_status_code_value[self.chat_session.grandpy_status_code] ==\
         "Bonjour Mon petit, en quoi puis-je t'aider ?"

    

    #@pytest.mark.skip()
    def test_display_grandpy_status_code_to_response(self):
        display_behavior.display_grandpy_status_code_to_response(self.chat_session)
        assert self.chat_session.grandpy_status_code == 'response'
        assert self.chat_session.__class__.grandpy_status_code_value[self.chat_session.grandpy_status_code] ==\
            "Voici la reponse à t'as questions !"

   
    #@pytest.mark.skip()
    def test_display_grandpy_status_code_to_exhausted(self):
        display_response = display_behavior.display_grandpy_status_code_to_exhausted(self.chat_session)
        assert self.chat_session.grandpy_status_code == 'exhausted'
        assert self.chat_session.__class__.grandpy_status_code_value[self.chat_session.grandpy_status_code] ==\
            "Je suis fatigué reviens me voir demain !"

    # ~ @pytest.mark.skip()
    def test_display_last_user_request(self):
        response_grandpy = self.chat_session.__class__.read_grandpy_answer('response_limit')
        display_behavior.display_last_user_request(self.chat_session, response_grandpy)
        response_grandpy = chat_access.ttl(str(self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]))

        assert response_grandpy == -2
