"""conversation management module between grandpyRobot and a user"""
# from collections import OrderedDict
# from frozenordereddict import FrozenOrderedDict
from src.display import display_behavior
from src.APIs.google_api import get_placeid_from_address
from src.redis_utilities import write_access_conversation_data, read_access_conversation_data
from src.redis_utilities import byte_to_boolean_conversion, value_to_string_conversion
from src.redis_utilities import byte_to_int_conversion


class Conversation:
    """conversation setting class"""
    # Default value of grandpy status attributes
    grandpy_status_code_value = {
        'home': "Bonjour Mon petit, en quoi puis-je t'aider ?",
        'benevolent': "Ok, c'est très bien mon petit !",
        'response': 'Voici la réponse à tas question !',
        'tired': 'Houla, maintenant ma memoire commence à fatiguée !',
        'incomprehension': "Ha, je ne comprends pas, essaye d'être plus précis ... !",
        'mannerless': "S'il te plait, reformule ta question en étant plus polis ... !",
        'disrespectful': "Hola, sois plus RESPECTUEUX ENVERS TES AINES 'MON PETIT' ... !",
        'incivility_limit': 'Cette impolitesse me FATIGUE ... !',
        'indecency_limit': 'Cette grossièreté me FATIGUE ... !',
        'incomprehension_limit': 'Cette incomprehension me FATIGUE ... !',
        'response_limit': 'HEY ! CA SUFFIT mon petit, ma mémoire est saturé ... !',
        'exhausted': 'Je suis fatigué reviens me voir demain !'}
    # -------------------------
    # Data for check incivility user behavior
    INCIVILITY_SET_DATA = frozenset({'bonjour', 'bonsoir', 'salut', 'hello', 'hi'})
    # Data for check indecency user behavior
    INDECENCY_SET_DATA = frozenset({
        'vieux', 'con', 'ancetre', 'poussierieux', 'vieillard', 'demoder', 'dinosaure',
        'senile', 'arrierer', 'decrepit', 'centenaire', 'rococo', 'antiquite', 'gateux',
        'archaique', 'croulant', 'vieille', 'baderne', 'fossile', 'foutu', 'bjr', 'bsr', 'slt'})
    # Data for parser (Words deleted for search)
    UNNECESSARY_SET_DATA = frozenset({
        'a', 'abord', 'absolument', 'afin', 'ah', 'ai', 'aie', 'ailleurs', 'ainsi', 'ait',
        'allaient', 'allo', 'allons', 'allô', 'alors', 'ancetre', 'ancetre demode',
        'anterieur', 'anterieure', 'anterieures', 'antiquite', 'apres', 'après',
        'arriere rococo', 'as', 'assez', 'attendu', 'au', 'aucun', 'aucune', 'aujourd',
        "aujourd'hui", 'aupres', 'auquel', 'aura', 'auraient', 'aurait', 'auront', 'aussi',
        'autre', 'autrefois', 'autrement', 'autres', 'autrui', 'aux', 'auxquelles',
        'auxquels', 'avaient', 'avais', 'avait', 'avant', 'avec', 'avoir', 'avons', 'ayant',
        'b', 'bah', 'bas', 'basee', 'bat', 'beau', 'beaucoup', 'bien', 'bigre', 'bonjour',
        'bonjour grandpy', 'comment vas tu', 'bonsoir grandpy', 'boum', 'bravo', 'brrr',
        'c', 'car', 'ce', 'ceci', 'cela', 'celle', 'celle-ci', 'celle-là', 'celles',
        'celles-ci', 'celles-là', 'celui', 'celui-ci', 'celui-là', 'cent',
        'centenaire senille', 'cependant', 'certain', 'certaine', 'certaines', 'certains',
        'certes', 'ces', 'cet', 'cette', 'ceux', 'ceux-ci', 'ceux-là', 'chacun', 'chacune',
        'chaque', 'cher', 'chers', 'chez', 'chiche', 'chut', 'chère', 'chères', 'ci', 'cinq',
        'cinquantaine', 'cinquante', 'cinquantième', 'cinquième', 'clac', 'clic', 'combien',
        'comme', 'comment', 'comment allez vous, grandpy', 'comparable', 'comparables',
        'compris', 'concernant', 'contre', 'couic', 'crac', 'd', 'da', 'dans', 'de',
        'debout', 'dedans', 'dehors', 'deja', 'delà', 'depuis', 'dernier', 'derniere',
        'derriere', 'derrière', 'des', 'desormais', 'desquelles', 'desquels', 'dessous',
        'dessus', 'deux', 'deuxième', 'deuxièmement', 'devant', 'devers', 'devra',
        'different', 'differentes', 'differents', 'différent', 'différente', 'différentes',
        'différents', 'dinosaure decrepit', 'dire', 'directe', 'directement', 'dit', 'dite',
        'dits', 'divers', 'diverse', 'diverses', 'dix', 'e', 'effet', 'egale', 'egalement',
        'egales', 'eh', 'elle', 'elle-même', 'elles', 'elles-mêmes', 'en', 'encore',
        'enfin', 'entre', 'envers', 'environ', 'es', 'est', 'et', 'etant', 'etc', 'etre',
        'eu', 'euh', 'eux', 'eux-mêmes', 'exactement', 'excepté', 'extenso', 'exterieur',
        'f', 'fais', 'faisaient', 'faisant', 'fait', 'façon', 'feront', 'fi', 'flac',
        'floc', 'font', 'g', 'gens', 'grandpy', 'h', 'ha', 'hello grandpy', 'hein', 'hem',
        'hep', 'hey', 'hi', 'ho', 'holà', 'hop', 'hormis', 'hors', 'hou', 'houp', 'hue',
        'hui', 'huit', 'huitième', 'hum', 'hurrah', 'hé', 'hélas', 'i', 'il', 'ils',
        'importe', 'j', 'je', 'jusqu', 'jusque', 'juste', 'k', 'l', 'la', 'laisser',
        'laquelle', 'las', 'le', 'lequel', 'les', 'lesquelles', 'lesquels', 'leur', 'leurs',
        'longtemps', 'lors', 'lorsque', 'lui', 'lui-meme', 'lui-même', 'là', 'lès', 'm',
        'ma', 'maint', 'maintenant', 'mais', 'malgre', 'malgré', 'maximale', 'me', 'meme',
        'memes', 'merci', 'mes', 'mien', "m'indiquer", "m'orienter", 'mienne', 'miennes',
        'miens', 'mille', 'mince', 'minimale', 'moi', 'moi-meme', 'moi-même', 'moindres',
        'moins', 'mon', 'moyennant', 'multiple', 'multiples', 'même', 'mêmes', 'n', 'na',
        'naturel', 'naturelle', 'naturelles', 'ne', 'neanmoins', 'necessaire',
        'necessairement', 'neuf', 'neuvième', 'ni', 'nombreuses', 'nombreux', 'non', 'nos',
        'notamment', 'notre', 'nous', 'nous-mêmes', 'nouveau', 'nul', 'néanmoins', 'nôtre',
        'nôtres', 'o', 'oh', 'ohé', 'ollé', 'olé', 'on', 'ont', 'onze', 'onzième', 'ore',
        'ou', 'ouf', 'ouias', 'oust', 'ouste', 'outre', 'ouvert', 'ouverte', 'ouverts',
        'o|', 'où', 'p', 'paf', 'pan', 'papi', 'papy', 'par', 'parce', 'parfois', 'parle',
        'parlent', 'parler', 'parmi', 'parseme', 'partant', 'particulier', 'particulière',
        'particulièrement', 'pas', 'passé', 'pendant', 'pense', 'permet', 'personne', 'peu',
        'peut', 'peuvent', 'peux', 'pff', 'pfft', 'pfut', 'pif', 'pire', 'plein', 'plouf',
        'plus', 'plusieurs', 'plutôt', 'possessif', 'possessifs', 'possible', 'possibles',
        'pouah', 'pour', 'pourquoi', 'pourrais', 'pourrait', 'pouvait', 'prealable',
        'precisement', 'premier', 'première', 'premièrement', 'pres', 'probable',
        'probante', 'procedant', 'proche', 'près', 'psitt', 'pu', 'puis', 'puisque', 'pur',
        'pure', 'q', 'qu', 'quand', 'quant', 'quant-à-soi', 'quanta', 'quarante',
        'quatorze', 'quatre', 'quatre-vingt', 'quatrième', 'quatrièmement', 'que', 'quel',
        'quelconque', 'quelle', 'quelles', "quelqu'un", 'quelque', 'quelques', 'quels',
        'qui', 'quiconque', 'quinze', 'quoi', 'quoique', 'r', 'rare', 'rarement', 'rares',
        'relative', 'relativement', 'remarquable', 'rend', 'rendre', 'restant', 'reste',
        'restent', 'restrictif', 'retour', 'revoici', 'revoilà', 'rien', 's', 'sa',
        'sacrebleu', 'sait', 'salut', 'salut grandpy, comment ca va', 'sans', 'sapristi',
        'sauf', 'se', 'sein', 'seize', 'selon', 'semblable', 'semblaient', 'semble',
        'semblent', 'sent', 'sept', 'septième', 'sera', 'seraient', 'serait', 'seront',
        'ses', 'seul', 'seule', 'seulement', 'si', 'sien', 'sienne', 'siennes', 'siens',
        'sinon', 'situe', 'situé', 'six', 'sixième', 'soi', 'soi-même', 'soit', 'soixante',
        'son', 'sont', 'sous', 'souvent', 'specifique', 'specifiques', 'speculatif', 'stop',
        'strictement', 'subtiles', 'suffisant', 'suffisante', 'suffit', 'suis', 'suit',
        'suivant', 'suivante', 'suivantes', 'suivants', 'suivre', 'superpose', 'sur',
        'surtout', 't', 'ta', 'tac', 'tant', 'tardive', 'te', 'tel', 'telle', 'tellement',
        'telles', 'tels', 'tenant', 'tend', 'tenir', 'tente', 'tes', 'tic', 'tien',
        'tienne', 'tiennes', 'tiens', 'toc', 'toi', 'toi-même', 'ton', 'touchant',
        'toujours', 'tous', 'tout', 'toute', 'toutefois', 'toutes', 'treize', 'trente',
        'tres', 'trois', 'troisième', 'troisièmement', 'trop', 'trouve', 'très', 'tsoin',
        'tsouin', 'tu', 'té', 'u', 'un', 'une', 'unes', 'uniformement', 'unique', 'uniques',
        'uns', 'v', 'va', 'vais', 'vas', 'vers', 'via', 'vieillard senille',
        'vieille baderne', 'vieillot archaique', 'vieux', 'vieux croulant', 'vieux fossile',
        'vieux gateux', 'vieux poussierieux', 'vif', 'vifs', 'vingt', 'vivat', 'vive',
        'vives', 'vlan', 'voici', 'voilà', 'vont', 'vos', 'votre', 'vous', 'vous-mêmes',
        'vu', 'vé', 'vôtre', 'vôtres', 'w', 'x', 'y', 'z', 'zut', 'à', 'â', 'ça', 'ès',
        'étaient', 'étais', 'était', 'étant', 'été', 'être', 'ô', ',', ';', '.', '?', '!',
        'donner', "l'adresse", 'du', 'connais', 'donnez', 'connaissez'})

    def __init__(self, user_entry, db_number, **args):
        self.user_entry = user_entry
        self.db_number = db_number
        self.level = args.get('level', 1)
        # Leve1 1 --> Presentation
        self.has_user_incivility_status = args.get('has_user_incivility_status', False)
        self.number_of_user_incivility = args.get('number_of_user_incivility', 0)
        # Level 1 --> Presentation and Level 2 --> Chat_session
        self.has_user_indecency_status = args.get('has_user_indecency_status', False)
        self.has_user_incomprehension_status = args.get('has_user_incomprehension_status', False)
        self.number_of_user_indecency = args.get('number_of_user_indecency', 0)
        self.number_of_user_incomprehension = args.get('number_of_user_incomprehension', 0)
        self.number_of_user_entries = args.get('number_of_user_entries', 0)
        # without Level
        self.has_fatigue_quotas_of_grandpy = args.get('has_fatigue_quotas_of_grandpy', False)
        self.grandpy_status_code =\
            args.get('grandpy_status_code', self.__class__.grandpy_status_code_value['home'])
        # self.user_behavior = self.user_behavior_init_ordered()

    def __str__(self):
        text = ''
        if self.level == 1:
            text = \
                f"Niveau : {self.level}, incivility / indecency / incomprehension"
        elif self.level == 2:
            text = f"Niveau : {self.level}, indecency / incomprehension"
        return text

    def from_level1_to_level2(self):
        """transition method from level 1 (Presentation) to level 2 (chat_session)"""
        self.level = 2
        self.has_user_indecency_status = False
        self.number_of_user_indecency = 0
        self.has_user_incomprehension_status = False
        self.number_of_user_incomprehension = 0

    def get_user_behavior(self) -> dict:
        """initializes the default values of status and count attributes
        with a name that takes one of the following values:
            has_user_incivility_status, has_user_indecency_status, has_user_incomprehension_status,
            behavior_level, number_of_user_incivility, number_of_user_indecency,
            number_of_user_incomprehension, has_fatigue_quotas_of_grandpy, grandpy_status_code"""
        self.level = 1
        self.has_user_incivility_status = False
        self.number_of_user_incivility = 0
        self.has_user_indecency_status = False
        self.has_user_incomprehension_status = False
        self.number_of_user_indecency = 0
        self.number_of_user_incomprehension = 0
        self.number_of_user_entries = 0
        self.has_fatigue_quotas_of_grandpy = False
        self.grandpy_status_code = 'home'
        behavior_data = {
            'level': self.level,
            'has_user_incivility_status': self.has_user_incivility_status,
            'has_user_indecency_status': self.has_user_indecency_status,
            'has_user_incomprehension_status': self.has_user_incomprehension_status,
            'number_of_user_incivility': self.number_of_user_incivility,
            'number_of_user_indecency': self.number_of_user_indecency,
            'number_of_user_incomprehension': self.number_of_user_incomprehension,
            'number_of_user_entries': self.number_of_user_entries,
            'has_fatigue_quotas_of_grandpy': self.has_fatigue_quotas_of_grandpy,
            'grandpy_status_code': self.grandpy_status_code}
        print(f"number incivility -> Initialisation dans get user_behavior =\
                {behavior_data['number_of_user_incivility']}")
        return behavior_data

    @staticmethod
    def set_user_behavior(behavior_status, behavior_value) -> dict:
        behavior_data = {behavior_status: behavior_value}
        return behavior_data

    def calculate_the_incivility_status(self) -> None:
        """update the attribut has_user_incivility_status since INCIVILITY_SET_DATA set"""
        user_entry_lowercase = self.lower_and_split_user_entry()
        incivility_set_data = self.__class__.INCIVILITY_SET_DATA
        self.has_user_incivility_status = incivility_set_data.isdisjoint(user_entry_lowercase)
        print(f"j'arrive ici avant le if [calculate incivility] = {self.number_of_user_incivility}")
        if self.has_user_incivility_status:
            self.number_of_user_incivility = self.has_user_incivility_status + 1
            print(f'dans le if = {self.number_of_user_incivility}')
            display_behavior.display_grandpy_status_code_to_mannerless(self)

    def calculate_the_indecency_status(self, chat_session) -> None:
        """update the attribut has_user_indecency_status since INDECENCY_SET_DATA set"""
        user_entry_lowercase = self.lower_and_split_user_entry()
        indecency_set_data = self.__class__.INDECENCY_SET_DATA
        self.has_user_indecency_status = not indecency_set_data.isdisjoint(user_entry_lowercase)
        if self.has_user_indecency_status:
            display_behavior.display_grandpy_status_code_to_disrespectful(chat_session)
            self.number_of_user_indecency = self.number_of_user_indecency + 1

    def calculate_the_incomprehension_status(self, chat_session) -> None:
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
        self.has_user_incomprehension_status = incomprehension_status
        if self.has_user_incomprehension_status:
            display_behavior.display_grandpy_status_code_to_incomprehension(chat_session)
            self.number_of_user_incomprehension += 1

    # def get_behavior_value(self, name_behavior_data) -> str:
    #     """returns a value in behavior_data dictionary
    #     with name_behavior_data which takes one of the following values:
    #     has_fatigue_quotas_of_grandpy, grandpy_status_code, number_of_user_entries"""
    #     behavior_data = {
    #         'has_fatigue_quotas_of_grandpy': self.has_fatigue_quotas_of_grandpy,
    #         'grandpy_status_code': self.grandpy_status_code,
    #         'number_of_user_entries': self.number_of_user_entries}
    #     behavior_status = behavior_data[name_behavior_data]
    #     return behavior_status

    # # 2) DONE Create class method to read grandpy answer
    # def read_grandpy_answer(self, grandpy_status) -> str:
    #     """method to read grandpy answer
    #     with grandpy_status which takes one of the following values:
    #     home, benevolent, response, tired, incomprehension, mannerless, disrespectful,
    #     incivility_limit, indecency_limit, incomprehension_limit  and exhausted"""
    #     response = self.get_grandpy_status[grandpy_status]
    #     return response

    def set_attributes_from_database(self) -> None:
        """initialization of attributes from the redis database"""
        bool_filter = byte_to_boolean_conversion
        int_filter = byte_to_int_conversion
        str_filter = value_to_string_conversion
        self.level = read_access_conversation_data('leval', int_filter, self.db_number)
        self.has_user_incivility_status = \
            read_access_conversation_data('has_user_incivility_status', bool_filter, self.db_number)
        self.has_user_indecency_status = \
            read_access_conversation_data('has_user_indecency_status', bool_filter, self.db_number)
        self.has_user_incomprehension_status = \
            read_access_conversation_data(
                'has_user_incomprehension_status', bool_filter, self.db_number)
        self.number_of_user_incivility = \
            read_access_conversation_data('number_of_user_incivility', int_filter, self.db_number)
        self.number_of_user_indecency = \
            read_access_conversation_data('number_of_user_indecency', int_filter, self.db_number)
        self.number_of_user_incomprehension = \
            read_access_conversation_data(
                'number_of_user_incomprehension', int_filter, self.db_number)
        self.number_of_user_entries = \
            read_access_conversation_data('number_of_user_entries', int_filter, self.db_number)
        self.has_fatigue_quotas_of_grandpy =\
            read_access_conversation_data(
                'has_fatigue_quotas_of_grandpy', bool_filter, self.db_number)
        self.grandpy_status_code = \
            read_access_conversation_data('grandpy_status_code', str_filter, self.db_number)
        print('lecture number_incivility dans redis [set_attribut] '
              f"{read_access_conversation_data('number_of_user_incivility', int_filter, self.db_number)}")
        print(f'number_incivility[set_attribute_from_database]= {self.number_of_user_incivility}')
        # if self.has_fatigue_quotas_of_grandpy is None:
        #     print(f"number_incivility -> if dans init = {self.number_of_user_incivility}")
        #     #  deletion of data from database 1 ==> database for Test
        #     erasing_data(1)
        #     # deletion of data from database 0 ==> database for prod
        #     erasing_data(0)
        #     for name, value in self.get_user_behavior().items():
        #         write_access_conversation_data(name, value, self.db_number)
        # elif self.number_of_user_incivility == 0:
        #     print(f"number incivility -> else dans init = {self.number_of_user_incivility}")
        #     for name in self.get_user_behavior():
        #         self.set_user_behavior(name, read_access_conversation_data(name, self.db_number))
        # else:
        #     self.number_of_user_incivility += 1

    def database_init_ordered(self) -> dict:
        """initialization of redis database
        with a key, its value and the ID of the redis database
        example :
        redis_utilities.write_access_conversation_data ('grandpy_status_code', 'home', 0)"""
        print("Initialisation REDIS [Conversation]")
        list_attributs_names, list_attributs_values = [], []
        user_behavior = self.get_user_behavior()
        for (name, value) in user_behavior.items():
            list_attributs_names.append(name)
            list_attributs_values.append(value)
        behavioral_data = dict(zip(list_attributs_names, list_attributs_values))

        for (name, value) in behavioral_data.items():
            write_access_conversation_data(name, value, self.db_number)
        return behavioral_data

    def lower_and_split_user_entry(self) -> list:
        """management of the user_entry attribute"""
        user_entry_lowercase = self.user_entry.lower()
        return user_entry_lowercase.split()

    def update_database(self) -> None:
        """after all data processing update redis database with local attributes"""
        chat_session_attribut_value = {
            # has_user_incivility_status
            'has_user_incivility_status': self.has_user_incivility_status,
            # has_user_indecency_status
            'has_user_indecency_status': self.has_user_indecency_status,
            # has_user_incomprehension_status
            'has_user_incomprehension_status': self.has_user_incomprehension_status,
            # has_fatigue_quotas_of_grandpy
            'has_fatigue_quotas_of_grandpy': self.has_fatigue_quotas_of_grandpy,
            # grandpy_status_code
            'grandpy_status_code': self.grandpy_status_code,
            # level
            'level': self.level,
            # number_of_user_incivility
            'number_of_user_incivility': self.number_of_user_incivility,
            # number_of_user_indecency
            'number_of_user_indecency': self.number_of_user_indecency,
            # number_of_user_incomprehension
            'number_of_user_incomprehension': self.number_of_user_incomprehension,
            # number_of_user_entries
            'number_of_user_entries': self.number_of_user_entries}
        print(f"[update_database] nombre_incivility ="
              f" {chat_session_attribut_value['number_of_user_incivility']}")
        # (in database redis) writing all
        for (name_attribut, value_attribut) in chat_session_attribut_value.items():
            write_access_conversation_data(name_attribut, value_attribut, self.db_number)

    def get_user_request_parser(self) -> None:
        """recover the keywords of the user request
        by abolishing word contained in UNNECESSARY_SET_DATA set"""
        list_of_word_request_user = self.user_entry.split()
        list_of_keyword = [
            w for w in list_of_word_request_user
            if w.lower() not in self.__class__.UNNECESSARY_SET_DATA
        ]
        # keyword = ' '.join(list_of_keyword)
        self.user_entry = ' '.join(list_of_keyword)


if __name__ == '__main__':
    pass
