from . import pytest
from . import RedisDataManagement
from . import Conversation
from . import display_behavior


# @pytest.mark.skip()
class TestDisplay:
    def setup_method(self):
        self.db_session = RedisDataManagement(db_number=1)
        self.db_session.erasing_redis_databases()
        self.chat_session = Conversation('', 1)

    # @pytest.mark.skip()
    def test_display_grandpy_status_code_to_home(self):
        display_behavior.display_grandpy_status_code_to_home(self.chat_session)
        assert self.chat_session.grandpy_status_code == 'home'
        assert self.chat_session.__class__.grandpy_status_code_value[self.chat_session.grandpy_status_code] ==\
         "Bonjour Mon petit, en quoi puis-je t'aider ?"

    #@pytest.mark.skip()
    def test_display_grandpy_status_code_to_benevolent(self):
        display_behavior.display_grandpy_status_code_to_benevolent(self.chat_session)
        assert self.chat_session.grandpy_status_code == 'benevolent'
        assert self.chat_session.__class__.grandpy_status_code_value[self.chat_session.grandpy_status_code] ==\
            "Ok, c'est tres bien mon petit !"
        assert self.chat_session.level == 2

    #@pytest.mark.skip()
    def test_display_grandpy_status_code_to_response(self):
        display_behavior.display_grandpy_status_code_to_response(self.chat_session)
        assert self.chat_session.grandpy_status_code == 'response'
        assert self.chat_session.__class__.grandpy_status_code_value[self.chat_session.grandpy_status_code] ==\
            "Voici la reponse à t'as questions !"

    #@pytest.mark.skip()
    def test_display_grandpy_status_code_to_tired(self):
        display_behavior.display_grandpy_status_code_to_tired(self.chat_session)
        assert self.chat_session.grandpy_status_code == 'tired'
        assert self.chat_session.__class__.grandpy_status_code_value[self.chat_session.grandpy_status_code] ==\
            "Houla, maintenant ma memoire commence à fatiguée !"

    #@pytest.mark.skip()
    def test_display_grandpy_status_code_to_incomprehension(self):
        display_behavior.display_grandpy_status_code_to_incomprehension(self.chat_session)
        assert self.chat_session.grandpy_status_code == 'incomprehension'
        assert self.chat_session.__class__.grandpy_status_code_value[self.chat_session.grandpy_status_code] ==\
            "Ha, je ne comprends pas, essaye d'être plus précis ... !"

    #@pytest.mark.skip()
    def test_display_grandpy_status_code_to_mannerless(self):
        display_behavior.display_grandpy_status_code_to_mannerless(self.chat_session)
        assert self.chat_session.grandpy_status_code == 'mannerless'
        assert self.chat_session.__class__.grandpy_status_code_value[self.chat_session.grandpy_status_code] ==\
            "S'il te plait, reformule ta question en étant plus polis ... !"

    #@pytest.mark.skip()
    def test_display_grandpy_status_code_to_disrespectful(self):
        display_behavior.display_grandpy_status_code_to_disrespectful(self.chat_session)
        assert self.chat_session.grandpy_status_code == 'disrespectful'
        assert self.chat_session.__class__.grandpy_status_code_value[self.chat_session.grandpy_status_code] ==\
            "Hola, sois plus RESPECTUEUX ENVERS TES AINES 'MON PETIT' ... !"

    #@pytest.mark.skip()
    def test_display_grandpy_status_code_to_incivility_limit(self):
        display_behavior.display_grandpy_status_code_to_incivility_limit(self.chat_session)
        assert self.chat_session.grandpy_status_code == 'exhausted'
        assert self.chat_session.__class__.grandpy_status_code_value[self.chat_session.grandpy_status_code] ==\
            "Je suis fatigué reviens me voir demain !"

    #@pytest.mark.skip()
    def test_display_grandpy_status_code_to_indecency_limit(self):
        display_behavior.display_grandpy_status_code_to_indecency_limit(self.chat_session)
        assert self.chat_session.grandpy_status_code == 'exhausted'
        assert self.chat_session.__class__.grandpy_status_code_value[self.chat_session.grandpy_status_code] ==\
            "Je suis fatigué reviens me voir demain !"

    #@pytest.mark.skip()
    def test_display_grandpy_status_code_to_incomprehension_limit(self):
        display_behavior.display_grandpy_status_code_to_incomprehension_limit(self.chat_session)
        assert self.chat_session.grandpy_status_code == 'exhausted'
        assert self.chat_session.__class__.grandpy_status_code_value[self.chat_session.grandpy_status_code] ==\
            "Je suis fatigué reviens me voir demain !"

    #@pytest.mark.skip()
    def test_display_grandpy_status_code_to_exhausted(self):
        display_response = display_behavior.display_grandpy_status_code_to_exhausted(self.chat_session)
        assert self.chat_session.grandpy_status_code == 'exhausted'
        assert self.chat_session.__class__.grandpy_status_code_value[self.chat_session.grandpy_status_code] ==\
            "Je suis fatigué reviens me voir demain !"

    # ~ @pytest.mark.skip()
    # ~ def test_display_last_user_request(self):
        # ~ response_grandpy = self.chat_session.__class__.read_grandpy_answer('response_limit')
        # ~ display_behavior.display_last_user_request(self.chat_session, response_grandpy)
        # ~ response_grandpy = chat_access.ttl(str(self.chat_session.user_behavior[
            # ~ self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]))

        # ~ assert response_grandpy == -2
