"""behavior parameters management module for a user"""
from . import Conversation
from . import get_placeid_from_address


class BehaviorParams(Conversation):
    """user behavior setting class"""
    def __init__(self, user_entry, db_number):
        Conversation.__init__(self, user_entry, db_number)

    @staticmethod
    def level_parameters(parameter):
        """level configuration with parameter --> 1 / 2
            ==> level[1] = 'presentation', level[2] = 'chat_session'"""
        level = {
            1: 'presentation',
            2: 'chat_session'}
        return level[parameter]

    def level_name_user(self, level, behavior_level) -> str:
        """returns the name of has_user_indecency_status , has_incomprehension_status attributes
        during user's presentation/chat_session args --> level = presentation / chat_session
        --> behavior_level = indecency / incomprehension
        ==> behavior_name = has_user_incivility_user / has_user_incivility_status2 /
            has_user_incomprehension_status / has_user_incomprehension_status2"""
        behavior_name = {
            # user_behavior['behavior_level'] == 'presentation'
            'presentation': {
                'has_user_indecency_status':
                    self.__class__.get_user_behavior_key('has_user_indecency_status'),
                'number_of_user_indecency':
                    self.__class__.get_user_behavior_key('number_of_user_indecency'),
                'has_user_incomprehension_status':
                    self.__class__.get_user_behavior_key('has_user_incomprehension_status'),
                'number_of_user_incomprehension':
                    self.__class__.get_user_behavior_key('number_of_user_incomprehension')},
            # user_behavior['behavior_level'] == 'chat_session'
            'chat_session': {
                'has_user_indecency_status2':
                    self.__class__.get_user_behavior_key('has_user_indecency_status2'),
                'number_of_user_indecency2':
                    self.__class__.get_user_behavior_key('number_of_user_indecency2'),
                'has_user_incomprehension_status2':
                    self.__class__.get_user_behavior_key('has_user_incomprehension_status2'),
                'number_of_user_incomprehension2':
                    self.__class__.get_user_behavior_key('number_of_user_incomprehension2')}}
        return behavior_name[level][behavior_level]

    def set_has_user_incivility_status(self, incivility_value) -> None:
        """determine user incivility status in the conversation"""
        self.user_behavior[
            self.__class__.get_user_behavior_key('has_user_incivility_status')] = incivility_value

    def set_has_user_status(self, level_parameter_names, behavior_status) -> None:
        """determine user incivility status / user indecency status in the conversation
        args ==> level = presentation / chat_session,
            ==> behavior_status = has_user_indecency_status / has_user_indecency_status2
                / has_user_incomprehension_status / has_user_incomprehension_status2
             ==> status_value = True / False """
        self.user_behavior[level_parameter_names] = behavior_status

    def set_has_fatigue_quotas_of_grandpy(self, quotas_value) -> None:
        """determine fatigue quotas in the conversation"""
        self.user_behavior[
            self.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')] = quotas_value

    def calculate_the_incivility_status(self) -> None:
        """update the attribut has_user_incivility_status since INCIVILITY_SET_DATA set"""
        user_entry_lowercase = self.lower_and_split_user_entry()
        incivility_set_data = self.__class__.INCIVILITY_SET_DATA
        self.set_has_user_incivility_status(incivility_set_data.isdisjoint(user_entry_lowercase))

    def calculate_the_indecency_status(self, has_user_indecency_status) -> None:
        """update the attribut has_user_indecency_status since INDECENCY_SET_DATA set"""
        user_entry_lowercase = self.lower_and_split_user_entry()
        indecency_set_data = self.__class__.INDECENCY_SET_DATA
        indecency_status = not indecency_set_data.isdisjoint(user_entry_lowercase)
        print(f"user_entry calculate = {user_entry_lowercase}")
        print(f"has_user_indecency calculate = {has_user_indecency_status}")
        print(f"indecency_status calculate = {indecency_status}")
        self.set_has_user_status(has_user_indecency_status, indecency_status)

    # DONE create a behaviour incomprehension for the user
    def calculate_the_incomprehension_status(self, has_user_incomprehension) -> None:
        """update the attribut has_user_indecency_status since GoogleMap API"""
        incomprehension_status = None
        result_api = get_placeid_from_address(self.user_entry)
        if result_api in (
                {'candidates': [], 'status': 'ZERO_RESULTS'},
                {'candidates': [], 'status': 'INVALID_REQUEST'}):
            incomprehension_status = True
        elif result_api not in (
                {'candidates': [], 'status': 'ZERO_RESULTS'},
                {'candidates': [], 'status': 'INVALID_REQUEST'}):
            incomprehension_status = False
        self.set_has_user_status(has_user_incomprehension, incomprehension_status)
