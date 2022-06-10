from . import pytest
from . import erasing_data
from . import BehaviorParams
from . import counting_behavior


# @pytest.mark.skip()
class TestCounting:
    def setup_method(self):
        erasing_data(1)
        self.chat_session = BehaviorParams('', 1)

    # @pytest.mark.skip()
    def test_user_incivility_count(self):
        self.chat_session.set_has_user_incivility_status(True)
        counting_behavior.user_incivility_count(self.chat_session)
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_incivility')] == 1
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('mannerless')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_incivility_status')]
        assert not self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

        counting_behavior.user_incivility_count(self.chat_session)
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_incivility')] == 2
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('mannerless')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_incivility_status')]
        assert not self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

        counting_behavior.user_incivility_count(self.chat_session)
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_incivility')] == 3
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('mannerless')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_incivility_status')]
        assert not self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

        counting_behavior.user_incivility_count(self.chat_session)
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_incivility')] == 3
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('incivility_limit')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_incivility_status')]
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

    # @pytest.mark.skip()
    def test_user_indecency_count(self):
        self.chat_session.set_has_user_status('has_user_indecency_status', True)
        counting_behavior.user_indecency_count(self.chat_session, 'number_of_user_indecency')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_indecency')] == 1
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('disrespectful')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_indecency_status')]
        assert not self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

        counting_behavior.user_indecency_count(self.chat_session, 'number_of_user_indecency')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_indecency')] == 2
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('disrespectful')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_indecency_status')]
        assert not self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

        counting_behavior.user_indecency_count(self.chat_session, 'number_of_user_indecency')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_indecency')] == 3
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('disrespectful')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_indecency_status')]
        assert not self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

        counting_behavior.user_indecency_count(self.chat_session, 'number_of_user_indecency')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_indecency')] == 3
        assert self.chat_session.user_behavior[
                   self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')] \
               == self.chat_session.__class__.get_grandpy_status_key('indecency_limit')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_indecency_status')]
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

    # @pytest.mark.skip()
    def test_user_indecency2_count(self):
        self.chat_session.set_has_user_status('has_user_indecency_status2', True)
        counting_behavior.user_indecency_count(self.chat_session, 'number_of_user_indecency2')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_indecency2')] == 1
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('disrespectful')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_indecency_status2')]
        assert not self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

        counting_behavior.user_indecency_count(self.chat_session, 'number_of_user_indecency2')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_indecency2')] == 2
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('disrespectful')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_indecency_status2')]
        assert not self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

        counting_behavior.user_indecency_count(self.chat_session, 'number_of_user_indecency2')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_indecency2')] == 3
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('disrespectful')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_indecency_status2')]
        assert not self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

        counting_behavior.user_indecency_count(self.chat_session, 'number_of_user_indecency2')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_indecency2')] == 3
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('indecency_limit')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_indecency_status2')]
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

    # @pytest.mark.skip()
    def test_user_incomprehension_count(self):
        self.chat_session.set_has_user_status('has_user_incomprehension_status', True)
        counting_behavior.user_incomprehension_count(
            self.chat_session, 'number_of_user_incomprehension')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_incomprehension')]\
            == 1
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('inconsistency')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_incomprehension_status')]
        assert not self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

        counting_behavior.user_incomprehension_count(
            self.chat_session, 'number_of_user_incomprehension')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_incomprehension')]\
            == 2
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('inconsistency')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_incomprehension_status')]
        assert not self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

        counting_behavior.user_incomprehension_count(
            self.chat_session, 'number_of_user_incomprehension')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_incomprehension')]\
            == 3
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('inconsistency')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_incomprehension_status')]
        assert not self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

        counting_behavior.user_incomprehension_count(
            self.chat_session, 'number_of_user_incomprehension')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_incomprehension')]\
            == 3
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('incomprehension_limit')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_incomprehension_status')]
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

    # @pytest.mark.skip()
    def test_user_incomprehension2_count(self):
        self.chat_session.set_has_user_status('has_user_incomprehension_status2', True)
        counting_behavior.user_incomprehension_count(
            self.chat_session, 'number_of_user_incomprehension2')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_incomprehension2')]\
            == 1
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('inconsistency')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_incomprehension_status2')]
        assert not self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

        counting_behavior.user_incomprehension_count(
            self.chat_session, 'number_of_user_incomprehension2')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_incomprehension2')]\
            == 2
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('inconsistency')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_incomprehension_status2')]
        assert not self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

        counting_behavior.user_incomprehension_count(
            self.chat_session, 'number_of_user_incomprehension2')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_incomprehension2')]\
            == 3
        assert self.chat_session.user_behavior[
                   self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')] \
               == self.chat_session.__class__.get_grandpy_status_key('inconsistency')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_incomprehension_status2')]
        assert not self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

        counting_behavior.user_incomprehension_count(
            self.chat_session, 'number_of_user_incomprehension2')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_incomprehension2')]\
            == 3
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == self.chat_session.__class__.get_grandpy_status_key('incomprehension_limit')
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_user_incomprehension_status2')]
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')]

    def test_user_question_answer_count_1_to_4(self):
        self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')] = 'benevolent'
        counting_behavior.user_question_answer_count(self.chat_session)
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_entries')] == 1
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')] == 'response'

        counting_behavior.user_question_answer_count(self.chat_session)
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_entries')] == 2
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')] == 'response'

        counting_behavior.user_question_answer_count(self.chat_session)
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_entries')] == 3
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')] == 'response'

        counting_behavior.user_question_answer_count(self.chat_session)
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_entries')] == 4
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')] == 'response'

    # @pytest.mark.skip()
    def test_user_question_answer_count_to_5(self):
        self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')] = 'response'
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_entries')] == 6
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')] == 'response'

    # @pytest.mark.skip()
    def test_user_question_answer_count_6_to_9(self):
        self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')] = 'response'
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        counting_behavior.user_question_answer_count(self.chat_session)
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_entries')] == 7
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')] == 'response'

        counting_behavior.user_question_answer_count(self.chat_session)
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_entries')] == 8
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')] == 'response'

        counting_behavior.user_question_answer_count(self.chat_session)
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_entries')] == 9
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')] == 'response'

        counting_behavior.user_question_answer_count(self.chat_session)
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_entries')] == 10
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')] == 'response'

        counting_behavior.user_question_answer_count(self.chat_session)
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('number_of_user_entries')] == 10
        assert self.chat_session.user_behavior[
            self.chat_session.__class__.get_user_behavior_key('grandpy_status_code')]\
            == 'response_limit'
