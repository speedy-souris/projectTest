"""conversation management module between grandpyRobot and a user"""
from collections import OrderedDict
from frozenordereddict import FrozenOrderedDict
from . import google_api
from . import redis_utilities
# from counting_behaviour import user_incivility_count, user_indecency_count
# from counting_behaviour import user_incomprehension_count


class Conversation:
    """conversation setting class"""
    # database initialization behavior parameter
    USER_BEHAVIOR_DEFAULT_DATA = FrozenOrderedDict({
        'has_user_incivility_status': False,
        'has_user_indecency_status': False,
        'has_user_incomprehension_status': False,
        'has_fatigue_quotas_of_grandpy': False,
        'grandpy_status_code': 'home',
        'number_of_user_incivility': 0,
        'number_of_user_indecency': 0,
        'number_of_user_incomprehension': 0,
        'number_of_user_entries': 0})
    USER_BEHAVIOR_DEFAULT_DATA_KEYS = tuple(USER_BEHAVIOR_DEFAULT_DATA.keys())

    # data grandpy satus values
    GRANDPY_STATUS_DATA = FrozenOrderedDict({
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
        'exhausted': 'Je suis fatigué reviens me voir demain !'})
    GRANDPY_STATUS_DATA_KEYS = tuple(GRANDPY_STATUS_DATA.keys())

    # Data for check incivility
    INCIVILITY_SET_DATA = frozenset({'bonjour', 'bonsoir', 'salut', 'hello', 'hi'})
    # Data for check decency
    INDECENCY_SET_DATA = frozenset({
        'vieux', 'con', 'ancetre', 'poussierieux', 'vieillard', 'demoder', 'dinosaure',
        'senile', 'arrierer', 'decrepit', 'centenaire', 'rococo', 'antiquite', 'gateux',
        'archaique', 'croulant', 'vieille', 'baderne', 'fossile', 'foutu', 'bjr', 'bsr', 'slt'})
    # Data for parser (deleted for research)
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

    def __init__(self, user_entry, db_number):
        self.user_entry = user_entry
        self.db_number = db_number
        self.user_behavior = self.user_behavior_init_ordered()

    @classmethod
    def get_user_behavior_key(cls, name_position) -> str:
        """returns a key in USER_BEHAVIOR_DEFAULT_DATA dictionary
        with name_position which takes one of the following values:
        has_user_incivility_status, has_user_indecency_status, has_user_incomprehension_status,
        has_fatigue_quotas_of_grandpy, grandpy_status_code, number_of_user_incivility,
        number_of_user_indecency, number_of_user_incomprehension and number_of_user_entries"""
        behavior_key = {
            'has_user_incivility_status': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[0],
            'has_user_indecency_status': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[1],
            'has_user_incomprehension_status': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[2],
            'has_fatigue_quotas_of_grandpy': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[3],
            'grandpy_status_code': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[4],
            'number_of_user_incivility': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[5],
            'number_of_user_indecency': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[6],
            'number_of_user_incomprehension': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[7],
            'number_of_user_entries': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[8]
        }
        return behavior_key.get(name_position)

    # 1) DONE Create class method to read grandpy status
    @classmethod
    def get_grandpy_status_key(cls, name_position) -> str:
        """returns a key in GRANDPY_STATUS_DATA dictionary
        with name_position which takes one of the following values:
        home, benevolent, response, tired, incomprehension, mannerless, disrespectful,
        incivility_limit, indecency_limit, incomprehension_limit , response_limit and exhausted"""
        status_key = {
            'home': cls.GRANDPY_STATUS_DATA_KEYS[0],
            'benevolent': cls.GRANDPY_STATUS_DATA_KEYS[1],
            'response': cls.GRANDPY_STATUS_DATA_KEYS[2],
            'tired': cls.GRANDPY_STATUS_DATA_KEYS[3],
            'incomprehension': cls.GRANDPY_STATUS_DATA_KEYS[4],
            'mannerless': cls.GRANDPY_STATUS_DATA_KEYS[5],
            'disrespectful': cls.GRANDPY_STATUS_DATA_KEYS[6],
            'incivility_limit': cls.GRANDPY_STATUS_DATA_KEYS[7],
            'indecency_limit': cls.GRANDPY_STATUS_DATA_KEYS[8],
            'incomprehension_limit': cls.GRANDPY_STATUS_DATA_KEYS[9],
            'response_limit': cls.GRANDPY_STATUS_DATA_KEYS[10],
            'exhausted': cls.GRANDPY_STATUS_DATA_KEYS[11]
        }
        return status_key.get(name_position)

    # 2) DONE Create class method to read grandpy answer
    @classmethod
    def read_grandpy_answer(cls, grandpy_status) -> str:
        """method to read grandpy answer
        with grandpy_status which takes one of the following values:
        home, benevolent, response, tired, incomprehension, mannerless, disrespectful,
        incivility_limit, indecency_limit, incomprehension_limit  and exhausted"""
        response = cls.GRANDPY_STATUS_DATA[cls.get_grandpy_status_key(grandpy_status)]
        return response

    def database_init_ordered(self) -> dict:
        """initialization of redis database
        with a key, its value and the ID of the redis database
        example :
        redis_utilities.write_access_conversation_data ('grandpy_status_code', 'home', 0)"""
        list_attributs_names, list_attributs_values = list(), list()
        for (name, value) in self.__class__.USER_BEHAVIOR_DEFAULT_DATA.items():
            list_attributs_names.append(name)
            list_attributs_values.append(value)
        behavioral_data = OrderedDict(zip(list_attributs_names, list_attributs_values))

        for (name, value) in behavioral_data.items():
            redis_utilities.write_access_conversation_data(
                name, value, self.db_number
            )
        return behavioral_data

    def user_behavior_init_ordered(self) -> dict:
        """user behavior initialization parameter"""
        if not redis_utilities.read_access_conversation_data(self.__class__.get_user_behavior_key(
                'has_fatigue_quotas_of_grandpy'), self.db_number):
            list_attributs_names, list_attributs_values = list(), list()
            for name in self.__class__.USER_BEHAVIOR_DEFAULT_DATA_KEYS:
                list_attributs_names.append(name)
                list_attributs_values.append(redis_utilities.read_access_conversation_data(name, self.db_number))
            behavioral_data = OrderedDict(zip(list_attributs_names, list_attributs_values))
        else:
            #  deletion of data from database 1 ==> database for Test
            redis_utilities.erasing_data(1)
            # deletion of data from database 0 ==> database for prod
            redis_utilities.erasing_data(0)
            behavioral_data = self.database_init_ordered()
        return behavioral_data

    def set_has_user_incivility_status(self, incivility_value) -> None:
        """determine user incivility status in the conversation"""
        self.user_behavior[
            self.__class__.get_user_behavior_key('has_user_incivility_status')] = incivility_value

    def set_has_user_indecency_status(self, indecency_value) -> None:
        """determine user incivility status in the conversation"""
        self.user_behavior[
            self.__class__.get_user_behavior_key('has_user_indecency_status')] = indecency_value

    def set_has_user_incomprehension_status(self, incomprehension_value) -> None:
        """determine user incivility status in the conversation"""
        self.user_behavior[
            self.__class__.get_user_behavior_key('has_user_incomprehension_status')]\
            = incomprehension_value

    def set_has_fatigue_quotas_of_grandpy(self, quotas_value) -> None:
        """determine fatigue quotas in the conversation"""
        self.user_behavior[
            self.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')] = quotas_value

    def lower_and_split_user_entry(self) -> list:
        """management of the user_entry attribute"""
        user_entry_lowercase = self.user_entry.lower()
        return user_entry_lowercase.split()

    def update_database(self) -> None:
        """after all data processing update redis database with local attributes
        example :
        write_access_conversation_data(
            'user_incivility', str(self.user_behavior['user_incivility']), db_number)"""
        chat_session_attribut_value = {
            # has_user_incivility_status
            self.__class__.get_user_behavior_key('has_user_incivility_status'):
                self.user_behavior[
                self.__class__.get_user_behavior_key('has_user_incivility_status')],
            # has_user_indecency_status
            self.__class__.get_user_behavior_key('has_user_indecency_status'):
                self.user_behavior[
                self.__class__.get_user_behavior_key('has_user_indecency_status')],
            # has_user_incomprehension_status
            self.__class__.get_user_behavior_key('has_user_incomprehension_status'):
                self.user_behavior[
                self.__class__.get_user_behavior_key('has_user_incomprehension_status')],
            # has_fatigue_quotas_of_grandpy
            self.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy'):
                self.user_behavior[
                self.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')],
            # grandpy_status_code
            self.__class__.get_user_behavior_key('grandpy_status_code'):
                self.user_behavior[self.__class__.get_user_behavior_key('grandpy_status_code')],
            # number_of_user_incivility
            self.__class__.get_user_behavior_key('number_of_user_incivility'):
                self.user_behavior[
                self.__class__.get_user_behavior_key('number_of_user_incivility')],
            # number_of_user_indecency
            self.__class__.get_user_behavior_key('number_of_user_indecency'):
                self.user_behavior[self.__class__.get_user_behavior_key('number_of_user_indecency')],
            # number_of_user_incomprehension
            self.__class__.get_user_behavior_key('number_of_user_incomprehension'):
                self.user_behavior[
                self.__class__.get_user_behavior_key('number_of_user_incomprehension')],
            # number_of_user_entries
            self.__class__.get_user_behavior_key('number_of_user_entries'):
                self.user_behavior[self.__class__.get_user_behavior_key('number_of_user_entries')]
        }
        # (in database redis) writing all
        for (name_attribut, value_attribut) in chat_session_attribut_value.items():
            redis_utilities.write_access_conversation_data(
                name_attribut, redis_utilities.value_to_string_conversion(value_attribut), self.db_number)

    def calculate_the_incivility_status(self) -> None:
        """update the attribut has_user_incivility_status since INCIVILITY_SET_DATA set"""
        user_entry_lowercase = self.lower_and_split_user_entry()
        incivility_set_data = self.__class__.INCIVILITY_SET_DATA
        self.set_has_user_incivility_status(incivility_set_data.isdisjoint(user_entry_lowercase))

    def calculate_the_indecency_status(self) -> None:
        """update the attribut has_user_indecency_status since INDECENCY_SET_DATA set"""
        user_entry_lowercase = self.lower_and_split_user_entry()
        indecency_set_data = self.__class__.INDECENCY_SET_DATA
        self.set_has_user_indecency_status(not indecency_set_data.isdisjoint(user_entry_lowercase))

    # DONE create a behaviour incomprehension for the user
    def calculate_the_incomprehension_status(self) -> None:
        """update the attribut has_user_indecency_status since GoogleMap API"""
        result_api = google_api.get_placeid_from_address(self.user_entry)
        if result_api in (
                {'candidates': [], 'status': 'ZERO_RESULTS'},
                {'candidates': [], 'status': 'INVALID_REQUEST'}):
            self.set_has_user_incomprehension_status(True)
        elif result_api not in (
                {'candidates': [], 'status': 'ZERO_RESULTS'},
                {'candidates': [], 'status': 'INVALID_REQUEST'}):
            self.set_has_user_incomprehension_status(False)

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
