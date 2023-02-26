from . import requests
from . import pytest
from . import RedisDataManagement
from . import get_mockreturn
from . import main
# from . import BehaviorParams


#@pytest.mark.skip()
class TestHomeMain:
    def setup_method(self):
        self.db_session = RedisDataManagement(db_number=1)
        self.db_session.erasing_data()
        self.db_session.database_init_by_default()

    # 11) DONE incivility query X1
    # ~ @pytest.mark.skip()
    def test_incorrect_presentation_user_to_1(self, monkeypatch):
        # incorrect presentation of the user X1 ==> question without ('bonjour'...)
        expected_result = {
            'html_attributions': [],
            'result': {
                'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                'geometry': {
                    'location': {'lat': 48.8975156, 'lng': 2.3833993},
                    'viewport': {
                        'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                        'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}}}},
            'status': 'OK'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_result))
        presentation_user = main.main('ou se trouve openClassrooms', db_number=1)
        # has_user_incivility_status = True
        assert presentation_user.has_user_incivility_status
        # has_user_indecency_status = False
        assert not presentation_user.has_user_indecency_status
        # has_user_incomprehension_status = False
        assert not presentation_user.has_user_incomprehension_status
        # has_fatigue_quotas_of_grandpy = False
        assert not presentation_user.has_fatigue_quotas_of_grandpy
        # grandpy_status_code = 'mannerless'
        assert presentation_user.grandpy_status_code == 'mannerless'
        # number_of_user_incivility = 1
        assert presentation_user.number_of_user_incivility == 1
        # number_of_user_indecency = 0
        assert presentation_user.number_of_user_indecency == 0
        # number_of_user_incomprehension = 0
        assert presentation_user.number_of_user_incomprehension == 0
        # number_of_user_entries = 0
        assert presentation_user.number_of_user_entries == 0

    # ~ @pytest.mark.skip()
    def test_incorrect_presentation_user_to_2(self, monkeypatch):
        # incorrect presentation of the user X2 ==> question without ('bonjour'...)
        expected_result = {
            'html_attributions': [],
            'result': {
                'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                'geometry': {
                    'location': {'lat': 48.8975156, 'lng': 2.3833993},
                    'viewport': {
                        'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                        'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}}}},
            'status': 'OK'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_result))
        main.main('ou se trouve openClassrooms', db_number=1)
        presentation_user_incivility = main.main('ou se trouve openClassrooms', db_number=1)
        # has_user_incivility_status = True
        assert presentation_user_incivility.has_user_incivility_status
        # has_user_indecency_status = False
        assert not presentation_user_incivility.has_user_indecency_status
        # has_user_incomprehension_status = False
        assert not presentation_user_incivility.has_user_incomprehension_status
        # has_fatigue_quotas_of_grandpy = False
        assert not presentation_user_incivility.has_fatigue_quotas_of_grandpy
        # grandpy_status_code = 'mannerless'
        assert presentation_user_incivility.grandpy_status_code == 'mannerless'
        # number_of_user_incivility = 2
        assert presentation_user_incivility.number_of_user_incivility == 2
        # number_of_user_indecency = 0
        assert presentation_user_incivility.number_of_user_indecency == 0
        # number_of_user_incomprehension = 0
        assert presentation_user_incivility.number_of_user_incomprehension == 0
        # number_of_user_entries = 0
        assert presentation_user_incivility.number_of_user_entries == 0

    # 13) DONE incivility query X3
    # ~ @pytest.mark.skip()
    def test_incorrect_presentation_user_to_3(self, monkeypatch):
        # incorrect presentation of the user X3 ==> question without ('bonjour'...)
        expected_result = {
            'html_attributions': [],
            'result': {
                'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                'geometry': {
                    'location': {'lat': 48.8975156, 'lng': 2.3833993},
                    'viewport': {
                        'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                        'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}}}},
            'status': 'OK'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_result))
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        # incorrect presentation of the user ==> question without ('bonjour'...)
        presentation_user_incivility = main.main('ou se trouve openClassrooms', db_number=1)
        # has_user_incivility_status = True
        assert presentation_user_incivility.has_user_incivility_status
        # has_user_indecency_status = False
        assert not presentation_user_incivility.has_user_indecency_status
        # has_user_incomprehension_status = False
        assert not presentation_user_incivility.has_user_incomprehension_status
        # grandpy_status_code = 'exhausted'
        assert presentation_user_incivility.grandpy_status_code == 'exhausted'
        # number_of_user_incivility = 3
        assert presentation_user_incivility.number_of_user_incivility == 3
        # has_fatigue_quotas_of_grandpy = True
        assert presentation_user_incivility.has_fatigue_quotas_of_grandpy
        # TTL has_fatigue_quotas_of_grandpy > 0
        assert self.db_session.db_session.ttl('has_fatigue_quotas_of_grandpy') > 0

    # 15) DONE indecency query (home) 1 to X2
    # ~ @pytest.mark.skip()
    def test_indecency_request_user_to_1(self, monkeypatch):
        # incorrect request of the user X1 ==> indecency presentation without ('bonjour'....)
        expected_result = {
            'html_attributions': [], 
            'result': {
                'formatted_address': '81140 Vieux, France', 'geometry': 
                    {
                        'location': {'lat': 43.993618, 'lng': 1.873189},
                        'viewport': {
                            'northeast': {'lat': 44.0216093678828, 'lng': 1.883779833710719},
                            'southwest': {'lat': 43.97977603685276, 'lng': 1.84876291855722}}}},
            'status': 'OK'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_result))
        presentation_user_indecency = main.main('vieux', db_number=1)
        # has_user_incivility_status = True
        assert presentation_user_indecency.has_user_incivility_status
        # has_user_indecency_status = True
        assert presentation_user_indecency.has_user_indecency_status
        # has_user_incomprehension_status = False
        assert not presentation_user_indecency.has_user_incomprehension_status
        # has_fatigue_quotas_of_grandpy = False
        assert not presentation_user_indecency.has_fatigue_quotas_of_grandpy
        # grandpy_status_code = 'disrespectful'
        assert presentation_user_indecency.grandpy_status_code == 'disrespectful'
        # number_of_user_incivility = 1
        assert presentation_user_indecency.number_of_user_incivility == 1
        # number_of_user_indecency = 1
        assert presentation_user_indecency.number_of_user_indecency == 1
        # 'number_of_user_incomprehension = 0
        assert presentation_user_indecency.number_of_user_incomprehension == 0
        # 'number_of_user_entries = 0
        assert presentation_user_indecency.number_of_user_entries == 0

    # ~ @pytest.mark.skip()
    def test_indecency_request_user_to_2(self, monkeypatch):
        # incorrect request of the user X2 ==> indecency presentation without ('bonjour'....)
        expected_result = {
            'html_attributions': [], 
            'result': {
                'formatted_address': '81140 Vieux, France', 'geometry': 
                    {
                        'location': {'lat': 43.993618, 'lng': 1.873189},
                        'viewport': {
                            'northeast': {'lat': 44.0216093678828, 'lng': 1.883779833710719},
                            'southwest': {'lat': 43.97977603685276, 'lng': 1.84876291855722}}}},
            'status': 'OK'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_result))
        main.main('vieux', db_number=1)
        presentation_user_indecency = main.main('vieux', db_number=1)

        # has_user_incivility_status = True
        assert presentation_user_indecency.has_user_incivility_status
        # has_user_indecency_status = True
        assert presentation_user_indecency.has_user_indecency_status
        # has_user_incomprehension_status = False
        assert not presentation_user_indecency.has_user_incomprehension_status
        # has_fatigue_quotas_of_grandpy = False
        assert not presentation_user_indecency.has_fatigue_quotas_of_grandpy
        # grandpy_status_code = 'disrespectful'
        assert presentation_user_indecency.grandpy_status_code == 'disrespectful'
        # 'number_of_user_incivility = 1
        assert presentation_user_indecency.number_of_user_incivility == 2
        # number_of_user_indecency = 2
        assert presentation_user_indecency.number_of_user_indecency == 2
        # number_of_user_incomprehension = 0
        assert presentation_user_indecency.number_of_user_incomprehension == 0
        # number_of_user_entries = 0
        assert presentation_user_indecency.number_of_user_entries == 0

    # 17) DONE indecency query (home) X3
    # ~ @pytest.mark.skip()
    def test_indecency_request_user_to_3(self, monkeypatch):
        # incorrect request of the user X3 ==> indecency presentation without ('bonjour'....)
        expected_result = {
            'html_attributions': [], 
            'result': {
                'formatted_address': '81140 Vieux, France', 'geometry': 
                    {
                        'location': {'lat': 43.993618, 'lng': 1.873189},
                        'viewport': {
                            'northeast': {'lat': 44.0216093678828, 'lng': 1.883779833710719},
                            'southwest': {'lat': 43.97977603685276, 'lng': 1.84876291855722}}}},
            'status': 'OK'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_result))
        main.main('vieux', db_number=1)
        main.main('vieux', db_number=1)
        # incorrect request of the user X4 ==> indecency presentation without ('bonjour'....)
        presentation_user_indecency = main.main('vieux', db_number=1)

        # has_fatigue_quotas_of_grandpy = False
        assert not presentation_user_indecency.has_fatigue_quotas_of_grandpy
        # grandpy_status_code = 'disrespectful'
        assert presentation_user_indecency.grandpy_status_code == 'disrespectful'
        # number_of_user_indecency = 3
        assert presentation_user_indecency.number_of_user_indecency == 3

        presentation_user_indecency = main.main('vieux', db_number=1)
        # has_fatigue_quotas_of_grandpy = True
        assert presentation_user_indecency.has_fatigue_quotas_of_grandpy
        # grandpy_status_code = 'exhausted'
        assert presentation_user_indecency.grandpy_status_code == 'exhausted'
        # number_of_user_indecency = 3
        assert presentation_user_indecency.number_of_user_indecency == 3

    # 19) DONE incomprehension query (home) 1 to X2
    # ~ @pytest.mark.skip()
    def test_incomprehension_request_user_to_1(self, monkeypatch):
        # incomprehension presentation of the user X1 ==> question without ('bonjour'...)
        expected_mock_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_mock_result))
        presentation_user_incomprehension = main.main('', db_number=1)

        # user_behavior['has_user_incivility_status'] = True
        assert presentation_user_incomprehension.has_user_incivility_status
        # user_behavior['has_user_indecency_status'] = False
        assert not presentation_user_incomprehension.has_user_indecency_status
        # user_behavior['has_user_incomprehension_status'] = True
        assert presentation_user_incomprehension.has_user_incomprehension_status
        # user_behavior['has_fatigue_quotas_of_grandpy'] = False
        assert not presentation_user_incomprehension.has_fatigue_quotas_of_grandpy
        # user_behavior['grandpy_status_code'] = 'incomprehension'
        assert presentation_user_incomprehension.grandpy_status_code == 'incomprehension'
        # user_behavior['number_of_user_incivility'] = 1
        assert presentation_user_incomprehension.number_of_user_incivility == 1
        # user_behavior['number_of_user_indecency'] = 0
        assert presentation_user_incomprehension.number_of_user_indecency == 0
        # user_behavior['number_of_user_incomprehension'] = 1
        assert presentation_user_incomprehension.number_of_user_incomprehension == 1
        # user_behavior['number_of_user_entries'] = 0
        assert presentation_user_incomprehension.number_of_user_entries == 0

    # ~ @pytest.mark.skip()
    def test_incomprehension_request_user_to_2(self, monkeypatch):
        # incomprehension presentation of the user X2 ==> question without ('bonjour'...)
        expected_mock_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_mock_result))
        main.main('', db_number=1)
        presentation_user_incomprehension = main.main('', db_number=1)

        # user_behavior['has_user_incivility_status'] = True
        assert presentation_user_incomprehension.has_user_incivility_status
        # user_behavior['has_user_indecency_status'] = False
        assert not presentation_user_incomprehension.has_user_indecency_status
        # user_behavior['has_user_incomprehension_status'] = True
        assert presentation_user_incomprehension.has_user_incomprehension_status
        # user_behavior['has_fatigue_quotas_of_grandpy'] = False
        assert not presentation_user_incomprehension.has_fatigue_quotas_of_grandpy
        # user_behavior['grandpy_status_code'] = 'incomprehension'
        assert presentation_user_incomprehension.grandpy_status_code == 'incomprehension'
        # user_behavior['number_of_user_incivility'] = 2
        assert presentation_user_incomprehension.number_of_user_incivility == 2
        # user_behavior['number_of_user_indecency'] = 0
        assert presentation_user_incomprehension.number_of_user_indecency == 0
        # user_behavior['number_of_user_incomprehension'] = 2
        assert presentation_user_incomprehension.number_of_user_incomprehension == 2
        # user_behavior['number_of_user_entries'] = 0
        assert presentation_user_incomprehension.number_of_user_entries == 0

    # 21) DONE incomprehension query X3
    # ~ @pytest.mark.skip()
    def test_incomprehension_request_user_to_3(self, monkeypatch):
        # incomprehension presentation of the user ==> question without ('bonjour'...)
        expected_mock_result = {'candidates': [], 'status': 'INVALID_REQUEST'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_mock_result))
        main.main('', db_number=1)
        main.main('', db_number=1)
        main.main('', db_number=1)
        # incomprehension presentation of the user X4 ==> question without ('bonjour'...)
        presentation_user_incomprehension = main.main('', db_number=1)

        # user_behavior['has_fatigue_quotas_of_grandpy'] = True
        assert presentation_user_incomprehension.has_fatigue_quotas_of_grandpy
        # user_behavior['grandpy_status_code'] = 'incomprehension_limit'
        assert presentation_user_incomprehension.grandpy_status_code == 'exhausted'
        # user_behavior['number_of_user_incomprehension'] = 3
        assert presentation_user_incomprehension.number_of_user_incomprehension == 3

    # # 7) DONE correct query X1
    # ~ @pytest.mark.skip()
    def test_correct_presentation_userX1(self, monkeypatch):
        # correct presentation of the user ==> ('bonjour'....)
        expected_result = {
            'html_attributions': [],
            'result': {
                'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                'geometry': {
                    'location': {'lat': 48.8975156, 'lng': 2.3833993},
                    'viewport': {
                        'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                        'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}}}},
            'status': 'OK'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_result))
        main.main('bonjour', db_number=1)
        dialogue_of_presentation = main.main('ou se trouve openClassrooms', db_number=1)
        # level == 2
        assert dialogue_of_presentation.level == 2
        # has_user_incivility_status == False
        assert not dialogue_of_presentation.has_user_incivility_status
        # has_user_indecency_status == False
        assert not dialogue_of_presentation.has_user_indecency_status
        # has_user_incomprehension_status == False
        assert not dialogue_of_presentation.has_user_incomprehension_status
        # has_fatigue_quotas_of_grandpy == False
        assert not dialogue_of_presentation.has_fatigue_quotas_of_grandpy
        # grandpy_status_code == 'benevolent'
        assert dialogue_of_presentation.grandpy_status_code == 'response'
        # number_of_user_incivility == 0
        assert dialogue_of_presentation.number_of_user_incivility == 0
        # number_of_user_indecency == 0
        assert dialogue_of_presentation.number_of_user_indecency == 0
        # number_of_user_incomprehension == 0
        assert dialogue_of_presentation.number_of_user_incomprehension == 0
        # number_of_user_entries == 1
        assert dialogue_of_presentation.number_of_user_entries == 1

    # ~ @pytest.mark.skip()
    def test_correct_presentation_userX5(self, monkeypatch):
        # correct presentation of the user ==> ('bonjour'....)
        expected_result = {
            'html_attributions': [],
            'result': {
                'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                'geometry': {
                    'location': {'lat': 48.8975156, 'lng': 2.3833993},
                    'viewport': {
                        'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                        'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}}}},
            'status': 'OK'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_result))
        main.main('bonjour', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        # level == 2
        dialogue_of_presentation = main.main('ou se trouve openClassrooms', db_number=1)
        # level == 2
        assert dialogue_of_presentation.level == 2
        # has_user_incivility_status == False
        assert not dialogue_of_presentation.has_user_incivility_status
        # has_user_indecency_status == False
        assert not dialogue_of_presentation.has_user_indecency_status
        # has_user_incomprehension_status == False
        assert not dialogue_of_presentation.has_user_incomprehension_status
        # has_fatigue_quotas_of_grandpy == False
        assert not dialogue_of_presentation.has_fatigue_quotas_of_grandpy
        # grandpy_status_code == 'tired'
        assert dialogue_of_presentation.grandpy_status_code == 'tired'
        # number_of_user_incivility == 0
        assert dialogue_of_presentation.number_of_user_incivility == 0
        # number_of_user_indecency == 0
        assert dialogue_of_presentation.number_of_user_indecency == 0
        # number_of_user_incomprehension == 0
        assert dialogue_of_presentation.number_of_user_incomprehension == 0
        # number_of_user_entries == 5
        assert dialogue_of_presentation.number_of_user_entries == 6

    # ~ @pytest.mark.skip()
    def test_correct_presentation_userX10(self, monkeypatch):
        # correct presentation of the user ==> ('bonjour'....)
        expected_result = {
            'html_attributions': [],
            'result': {
                'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                'geometry': {
                    'location': {'lat': 48.8975156, 'lng': 2.3833993},
                    'viewport': {
                        'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                        'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}}}},
            'status': 'OK'}
        monkeypatch.setattr(requests, 'get', get_mockreturn(expected_result))
        main.main('bonjour', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        main.main('ou se trouve openClassrooms', db_number=1)
        # level == 2
        dialogue_of_presentation = main.main('ou se trouve openClassrooms', db_number=1)
        print(f"number_entries[test] = {dialogue_of_presentation.number_of_user_entries}")
        # level == 2
        assert dialogue_of_presentation.level == 2
        # has_user_incivility_status == False
        assert not dialogue_of_presentation.has_user_incivility_status
        # has_user_indecency_status == False
        assert not dialogue_of_presentation.has_user_indecency_status
        # has_user_incomprehension_status == False
        assert not dialogue_of_presentation.has_user_incomprehension_status
        # has_fatigue_quotas_of_grandpy == True
        assert dialogue_of_presentation.has_fatigue_quotas_of_grandpy
        # grandpy_status_code == 'exhausted'
        assert dialogue_of_presentation.grandpy_status_code == 'exhausted'
        # number_of_user_incivility == 0
        assert dialogue_of_presentation.number_of_user_incivility == 0
        # number_of_user_indecency == 0
        assert dialogue_of_presentation.number_of_user_indecency == 0
        # number_of_user_incomprehension == 0
        assert dialogue_of_presentation.number_of_user_incomprehension == 0
        # number_of_user_entries == 10
        assert dialogue_of_presentation.number_of_user_entries == 10
