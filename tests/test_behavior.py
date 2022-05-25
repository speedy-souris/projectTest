#!/usr/bin/env python
"""test user behaviour module """
from . import pytest
from . import Conversation
from . import erasing_data


# @pytest.mark.skip()
class TestBehavior:
    def setup_method(self):
        erasing_data(1)
        self.chat_session = Conversation('', 1)
        self.grandpy_status = {
            'home': self.chat_session.__class__.get_grandpy_status_key('home'),
            'benevolent': self.chat_session.__class__.get_grandpy_status_key('benevolent'),
            'response': self.chat_session.__class__.get_grandpy_status_key('response'),
            'tired': self.chat_session.__class__.get_grandpy_status_key('tired'),
            'incomprehension':
                self.chat_session.__class__.get_grandpy_status_key('incomprehension'),
            'mannerless': self.chat_session.__class__.get_grandpy_status_key('mannerless'),
            'disrespectful': self.chat_session.__class__.get_grandpy_status_key('disrespectful'),
            'incivility_limit':
                self.chat_session.__class__.get_grandpy_status_key('incivility_limit'),
            'indecency_limit':
                self.chat_session.__class__.get_grandpy_status_key('indecency_limit'),
            'incomprehension_limit':
                self.chat_session.__class__.get_grandpy_status_key('incomprehension_limit'),
            'exhausted': self.chat_session.__class__.get_grandpy_status_key('exhausted')
        }

    def test_get_user_behavior_key(self):
        user_behavior = {
            'has_user_incivility_status':
                self.chat_session.__class__.get_user_behavior_key('has_user_incivility_status'),
            'has_user_indecency_status':
                self.chat_session.__class__.get_user_behavior_key('has_user_indecency_status'),
            'has_user_incomprehension_status': self.chat_session.__class__.get_user_behavior_key(
                'has_user_incomprehension_status'),
            'has_fatigue_quotas_of_grandpy':
                self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy'),
            'grandpy_status_code':
                self.chat_session.__class__.get_user_behavior_key('grandpy_status_code'),
            'number_of_user_incivility':
                self.chat_session.__class__.get_user_behavior_key('number_of_user_incivility'),
            'number_of_user_indecency':
                self.chat_session.__class__.get_user_behavior_key('number_of_user_indecency'),
            'number_of_user_incomprehension':
                self.chat_session.__class__.get_user_behavior_key('number_of_user_incomprehension'),
            'number_of_user_entries':
                self.chat_session.__class__.get_user_behavior_key('number_of_user_entries')
        }
        user_incivility_value\
            = self.chat_session.__class__.USER_BEHAVIOR_DEFAULT_DATA[
                user_behavior['has_user_incivility_status']]
        user_indecency_value\
            = self.chat_session.__class__.USER_BEHAVIOR_DEFAULT_DATA[
                user_behavior['has_user_indecency_status']]
        user_incomprehension_value\
            = self.chat_session.__class__.USER_BEHAVIOR_DEFAULT_DATA[
                user_behavior['has_user_incomprehension_status']]
        fatigue_quotas_value\
            = self.chat_session.__class__.USER_BEHAVIOR_DEFAULT_DATA[
                user_behavior['has_fatigue_quotas_of_grandpy']]
        grandpy_status_value\
            = self.chat_session.__class__.USER_BEHAVIOR_DEFAULT_DATA[
                user_behavior['grandpy_status_code']]
        number_incivility_value\
            = self.chat_session.__class__.USER_BEHAVIOR_DEFAULT_DATA[
                user_behavior['number_of_user_incivility']]
        number_indecency_value\
            = self.chat_session.__class__.USER_BEHAVIOR_DEFAULT_DATA[
                user_behavior['has_user_indecency_status']]
        number_incomprehension_value\
            = self.chat_session.__class__.USER_BEHAVIOR_DEFAULT_DATA[
                user_behavior['has_user_incomprehension_status']]
        number_entries_value\
            = self.chat_session.__class__.USER_BEHAVIOR_DEFAULT_DATA[
                user_behavior['number_of_user_entries']]

        assert (user_behavior['has_user_incivility_status'], user_incivility_value)\
               == ('has_user_incivility_status', False)
        assert (user_behavior['has_user_indecency_status'], user_indecency_value)\
               == ('has_user_indecency_status', False)
        assert (user_behavior['has_user_incomprehension_status'], user_incomprehension_value)\
               == ('has_user_incomprehension_status', False)
        assert (user_behavior['has_fatigue_quotas_of_grandpy'], fatigue_quotas_value)\
               == ('has_fatigue_quotas_of_grandpy', False)
        assert (user_behavior['grandpy_status_code'], grandpy_status_value)\
               == ('grandpy_status_code', 'home')
        assert (user_behavior['number_of_user_incivility'], number_incivility_value)\
               == ('number_of_user_incivility', 0)
        assert (user_behavior['number_of_user_indecency'], number_indecency_value)\
               == ('number_of_user_indecency', 0)
        assert (user_behavior['number_of_user_incomprehension'], number_incomprehension_value)\
               == ('number_of_user_incomprehension', 0)
        assert (user_behavior['number_of_user_entries'], number_entries_value)\
               == ('number_of_user_entries', 0)

    # @pytest.mark.skip()
    def test_get_grandpy_status_key(self):
        home_value = self.chat_session.__class__.GRANDPY_STATUS_DATA[self.grandpy_status['home']]
        benevolent_value\
            = self.chat_session.__class__.GRANDPY_STATUS_DATA[self.grandpy_status['benevolent']]
        response_value = self.chat_session.__class__.GRANDPY_STATUS_DATA[
            self.grandpy_status['response']]
        tired_value = self.chat_session.__class__.GRANDPY_STATUS_DATA[self.grandpy_status['tired']]
        incomprehension_value\
            = self.chat_session.__class__.GRANDPY_STATUS_DATA[
                self.grandpy_status['incomprehension']]
        mannerless_value\
            = self.chat_session.__class__.GRANDPY_STATUS_DATA[self.grandpy_status['mannerless']]
        disrespectful_value\
            = self.chat_session.__class__.GRANDPY_STATUS_DATA[self.grandpy_status['disrespectful']]
        incivility_limit_value\
            = self.chat_session.__class__.GRANDPY_STATUS_DATA[
                self.grandpy_status['incivility_limit']]
        indecency_limit_value\
            = self.chat_session.__class__.GRANDPY_STATUS_DATA[
                self.grandpy_status['indecency_limit']]
        incomprehension_limit_value =\
            self.chat_session.__class__.GRANDPY_STATUS_DATA[
                self.grandpy_status['incomprehension_limit']]
        exhausted_value\
            = self.chat_session.__class__.GRANDPY_STATUS_DATA[self.grandpy_status['exhausted']]

        assert (self.grandpy_status['home'], home_value)\
               == ('home', "Bonjour Mon petit, en quoi puis-je t'aider ?")
        assert (self.grandpy_status['benevolent'], benevolent_value)\
               == ('benevolent', "Ok, c'est très bien mon petit !")
        assert (self.grandpy_status['response'], response_value)\
               == ('response', 'Voici la réponse à tas question !')
        assert (self.grandpy_status['tired'], tired_value)\
               == ('tired', 'Houla, maintenant ma memoire commence à fatiguée !')
        assert (self.grandpy_status['incomprehension'], incomprehension_value)\
               == ('incomprehension', "Ha, je ne comprends pas, essaye d'être plus précis ... !")
        assert (self.grandpy_status['mannerless'], mannerless_value)\
               == ('mannerless', "S'il te plait, reformule ta question en étant plus polis ... !")
        assert (self.grandpy_status['disrespectful'], disrespectful_value)\
               == (
               'disrespectful', "Hola, sois plus RESPECTUEUX ENVERS TES AINES 'MON PETIT' ... !")
        assert (self.grandpy_status['incivility_limit'], incivility_limit_value)\
               == ('incivility_limit', 'Cette impolitesse me FATIGUE ... !')
        assert (self.grandpy_status['indecency_limit'], indecency_limit_value)\
               == ('indecency_limit', 'Cette grossièreté me FATIGUE ... !')
        assert (self.grandpy_status['incomprehension_limit'], incomprehension_limit_value)\
               == ('incomprehension_limit', 'Cette incomprehension me FATIGUE ... !')
        assert (self.grandpy_status['exhausted'], exhausted_value)\
               == ('exhausted', 'Je suis fatigué reviens me voir demain !')

    def test_read_grandpy_answer(self):
        home_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[self.grandpy_status['home']]
        home_response = self.chat_session.__class__.read_grandpy_answer('home')
        assert home_response == home_status

        presentation_status\
            = self.chat_session.__class__.GRANDPY_STATUS_DATA[self.grandpy_status['benevolent']]
        presentation_response = self.chat_session.__class__.read_grandpy_answer('benevolent')
        assert presentation_response == presentation_status

        answer_status\
            = self.chat_session.__class__.GRANDPY_STATUS_DATA[self.grandpy_status['response']]
        answer_response = self.chat_session.__class__.read_grandpy_answer('response')
        assert answer_response == answer_status

        tired_status = self.chat_session.__class__.GRANDPY_STATUS_DATA[self.grandpy_status['tired']]
        tired_response = self.chat_session.__class__.read_grandpy_answer('tired')
        assert tired_response == tired_status

        incomprehension_status\
            = self.chat_session.__class__.GRANDPY_STATUS_DATA[
                self.grandpy_status['incomprehension']]
        incomprehension_response\
            = self.chat_session.__class__.read_grandpy_answer('incomprehension')
        assert incomprehension_response == incomprehension_status

        mannerless_status\
            = self.chat_session.__class__.GRANDPY_STATUS_DATA[self.grandpy_status['mannerless']]
        mannerless_response = self.chat_session.__class__.read_grandpy_answer('mannerless')
        assert mannerless_response == mannerless_status

        disrespectful_status\
            = self.chat_session.__class__.GRANDPY_STATUS_DATA[self.grandpy_status['disrespectful']]
        disrespectful_response = self.chat_session.__class__.read_grandpy_answer('disrespectful')
        assert disrespectful_response == disrespectful_status

        incivility_limit_status\
            = self.chat_session.__class__.GRANDPY_STATUS_DATA[
                self.grandpy_status['incivility_limit']]
        incivility_limit_response\
            = self.chat_session.__class__.read_grandpy_answer('incivility_limit')
        assert incivility_limit_response == incivility_limit_status

        indecency_limit_status\
            = self.chat_session.__class__.GRANDPY_STATUS_DATA[
                self.grandpy_status['indecency_limit']]
        indecency_limit_response\
            = self.chat_session.__class__.read_grandpy_answer('indecency_limit')
        assert indecency_limit_response == indecency_limit_status

        incomprehension_limit_status\
            = self.chat_session.__class__.GRANDPY_STATUS_DATA[
                self.grandpy_status['incomprehension_limit']]
        incomprehension_limit_response\
            = self.chat_session.__class__.read_grandpy_answer('incomprehension_limit')
        assert incomprehension_limit_response == incomprehension_limit_status

        exhausted_status\
            = self.chat_session.__class__.GRANDPY_STATUS_DATA[self.grandpy_status['exhausted']]
        exhausted_response = self.chat_session.__class__.read_grandpy_answer('exhausted')
        assert exhausted_response == exhausted_status

    def test_set_has_user_incivility_status(self):
        self.chat_session.set_has_user_incivility_status(True)
        user_incivility\
            = self.chat_session.user_behavior[
                self.chat_session.__class__.get_user_behavior_key('has_user_incivility_status')]
        assert user_incivility

        self.chat_session.set_has_user_incivility_status(False)
        user_incivility\
            = self.chat_session.user_behavior[
                self.chat_session.__class__.get_user_behavior_key('has_user_incivility_status')]
        assert not user_incivility

    def test_set_has_user_indecency_status(self):
        self.chat_session.set_has_user_indecency_status(True)
        user_indecency\
            = self.chat_session.user_behavior[
                self.chat_session.__class__.get_user_behavior_key('has_user_indecency_status')]
        assert user_indecency

        self.chat_session.set_has_user_indecency_status(False)
        user_indecency\
            = self.chat_session.user_behavior[
                self.chat_session.__class__.get_user_behavior_key('has_user_indecency_status')]
        assert not user_indecency

    def test_set_has_user_incomprehension_status(self):
        self.chat_session.set_has_user_incomprehension_status(True)
        user_incomprehension\
            = self.chat_session.user_behavior[self.chat_session.__class__.get_user_behavior_key(
                'has_user_incomprehension_status')]
        assert user_incomprehension

        self.chat_session.set_has_user_incomprehension_status(False)
        user_incomprehension\
            = self.chat_session.user_behavior[self.chat_session.__class__.get_user_behavior_key(
                'has_user_incomprehension_status')]
        assert not user_incomprehension

    def test_set_has_fatigue_quotas_of_grandpy(self):
        self.chat_session.set_has_fatigue_quotas_of_grandpy(True)
        grandpy_status\
            = self.chat_session.user_behavior[
                self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]
        assert grandpy_status

        self.chat_session.set_has_fatigue_quotas_of_grandpy(False)
        grandpy_status\
            = self.chat_session.user_behavior[
                self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]
        assert not grandpy_status
