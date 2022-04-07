#!/usr/bin/env python
"""conversation management module between grandpyRobot and a user"""
from frozenordereddict import FrozenOrderedDict
from collections import OrderedDict
from google_api import get_placeid_from_address, get_address_api_from_placeid
from redis_utilities import write_access_conversation_data, read_access_conversation_data
from redis_utilities import erasing_data, value_to_string_conversion, data_expiration
from counting_behaviour import user_incivility_count, user_indecency_count
from counting_behaviour import user_incomprehension_count


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
        'number_of_user_entries': 0
    })
    USER_BEHAVIOR_DEFAULT_DATA_KEYS = tuple(USER_BEHAVIOR_DEFAULT_DATA.keys())

    # data grandpy satus values
    GRANDPY_STATUS_DATA = FrozenOrderedDict({
        'home': "Bonjour Mon petit, en quoi puis-je t'aider ?",
        'user_question': 'As-tu une nouvelle question à me demander ?',
        'response': 'Voici Ta Réponse à la question !',
        'tired': 'houla, maintenant ma memoire commence à fatiguée !',
        'incomprehension': "Ha, je ne comprends pas, essaye d'être plus précis ... !",
        'mannerless': "s'il te plait, reformule ta question en étant plus polis ... !",
        'disrespectful': "Hola, sois plus RESPECTUEUX ENVERS TES AINES 'MON PETIT' ... !",
        'incivility_limit': 'cette impolitesse me FATIGUE ... !',
        'indecency_limit': 'cette grossièreté me FATIGUE ... !',
        'incomprehension_limit': 'cette incomprehension me FATIGUE ... !',
        'exhausted': 'je suis fatigué reviens me voir demain !'
    })
    GRANDPY_STATUS_DATA_KEYS = tuple(GRANDPY_STATUS_DATA.keys())

    # Data for check incivility
    INCIVILITY_SET_DATA = frozenset({'bonjour', 'bonsoir', 'salut', 'hello', 'hi'})
    # Data for check decency
    INDECENCY_SET_DATA = frozenset({
        'vieux', 'con', 'ancetre', 'poussierieux', 'vieillard', 'demoder', 'dinosaure',
        'senille', 'arrierer', 'decrepit', 'centenaire', 'rococo', 'antiquite', 'senille',
        'gateux', 'archaique', 'croulant', 'vieille', 'baderne', 'fossile', 'foutu', 'bjr',
        'bsr', 'slt'
    })
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
        'donner', "l'adresse", 'du', 'connais', 'donnez', 'connaissez'
    })

    def __init__(self, user_entry, db_number=0):
        self.user_entry = user_entry
        self.user_behavior = self.user_behavior_init_ordered(db_number=db_number)

    @classmethod
    def get_user_behavior_key(cls, key_position) -> str:
        """returns a key in USER_BEHAVIOR_DEFAULT_DATA dictionary"""
        behavior_key = cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[key_position]
        return behavior_key

    # 1) DONE Create class method to read grandpy status
    @classmethod
    def get_grandpy_status_key(cls, key_position) -> str:
        """returns a key in GRANDPY_STATUS_DATA dictionary"""
        status_key = cls.GRANDPY_STATUS_DATA_KEYS[key_position]
        return status_key

    # 2) DONE Create class method to read grandpy answer
    @classmethod
    def read_grandpy_answer(cls, grandpy_status_key) -> str:
        """method to read grandpy answer"""
        response = cls.GRANDPY_STATUS_DATA_KEYS[grandpy_status_key]
        return response

    @classmethod
    def database_init_ordered(cls, db_number) -> dict:
        """initialization of redis database
        example :
        redis_utilities.write_access_conversation_data ('user_incivility', 'False', db_number)
        """
        list_data_keys, list_data_values = list(), list()
        for (key, value) in cls.USER_BEHAVIOR_DEFAULT_DATA.items():
            list_data_keys.append(key)
            list_data_values.append(value)
        behavioral_data = OrderedDict(zip(list_data_keys, list_data_values))

        for (key, value) in behavioral_data.items():
            write_access_conversation_data(
                key, value, db_number
            )
        return behavioral_data

    def user_behavior_init_ordered(self, db_number) -> dict:
        """user behavior initialization parameter"""
        list_data_keys, list_data_values = list(), list()
        for value in self.__class__.USER_BEHAVIOR_DEFAULT_DATA_KEYS:
            list_data_keys.append(value)
            list_data_values.append(read_access_conversation_data(value, db_number))
        behavioral_data = OrderedDict(zip(list_data_keys, list_data_values))
        try:
            # fatigue_quotas_of_grandpy
            behavioral_data[self.__class__.get_user_behavior_key(3)]
        except AttributeError:
            #  deletion of data from database 1 ==> database for Test
            erasing_data(1)
            #  deletion of data from database 0 ==> database for prod
            erasing_data(0)
            behavioral_data = self.__class__.database_init_ordered(db_number)
        return behavioral_data

    def set_has_user_incivility_status(self, incivility_value) -> None:
        """determine user incivility status in the conversation"""
        self.user_behavior[self.__class__.get_user_behavior_key(0)] = incivility_value

    def set_has_user_indecency_status(self, indecency_value) -> None:
        """determine user incivility status in the conversation"""
        self.user_behavior[self.__class__.get_user_behavior_key(1)] = indecency_value

    def set_has_user_incomprehension_status(self, incomprehension_value) -> None:
        """determine user incivility status in the conversation"""
        self.user_behavior[self.__class__.get_user_behavior_key(2)] = incomprehension_value

    def set_has_fatigue_quotas_of_grandpy(self, quotas_value) -> None:
        """determine fatigue quotas in the conversation"""
        self.user_behavior[self.__class__.get_user_behavior_key(3)] = quotas_value

    def lower_and_split_user_entry(self) -> list:
        """management of the user_entry attribute"""
        user_entry_lowercase = self.user_entry.lower()
        return user_entry_lowercase.split()

    def update_database(self, db_number) -> None:
        """after all data processing update redis database with local attributes
        example :
        write_access_conversation_data(
            'user_incivility', str(self.user_behavior['user_incivility']), db_number)"""
        behavior_data = self.__class__.USER_BEHAVIOR_DEFAULT_DATA_KEYS
        db_data = {
            # has_user_incivility_status
            behavior_data[0]: self.user_behavior[self.__class__.get_user_behavior_key(0)],
            # has_user_indecency_status
            behavior_data[1]: self.user_behavior[self.__class__.get_user_behavior_key(1)],
            # has_user_incomprehension_status
            behavior_data[2]: self.user_behavior[self.__class__.get_user_behavior_key(2)],
            # has_fatigue_quotas_of_grandpy
            behavior_data[3]: self.user_behavior[self.__class__.get_user_behavior_key(3)],
            # grandpy_status_code
            behavior_data[4]: self.user_behavior[self.__class__.get_user_behavior_key(4)],
            # number_of_user_incivility
            behavior_data[5]: self.user_behavior[self.__class__.get_user_behavior_key(5)],
            # number_of_user_indecency
            behavior_data[6]: self.user_behavior[self.__class__.get_user_behavior_key(6)],
            # number_of_user_incomprehension
            behavior_data[7]: self.user_behavior[self.__class__.get_user_behavior_key(7)],
            # number_of_user_entries
            behavior_data[8]: self.user_behavior[self.__class__.get_user_behavior_key(8)]
        }
        # (in database redis) writing all
        for (data, value) in db_data.items():
            write_access_conversation_data(data, value_to_string_conversion(value), db_number)

    def calculate_the_incivility(self, db_number) -> None:
        """update the attribut has_user_incivility_status since INCIVILITY_SET_DATA set"""
        user_entry_lowercase = self.lower_and_split_user_entry()
        incivility_set_data = self.__class__.INCIVILITY_SET_DATA
        self.set_has_user_incivility_status(incivility_set_data.isdisjoint(user_entry_lowercase))
        user_incivility_count(self, data_expiration, db_number)

    def calculate_the_indecency(self, db_number) -> None:
        """update the attribut has_user_indecency_status since INDECENCY_SET_DATA set"""
        user_entry_lowercase = self.lower_and_split_user_entry()
        indecency_set_data = self.__class__.INDECENCY_SET_DATA
        self.set_has_user_indecency_status(not indecency_set_data.isdisjoint(user_entry_lowercase))
        user_indecency_count(self, data_expiration, db_number)

    def calculate_the_incomprehension(self, db_number) -> None:
        """update the attribut has_user_indecency_status since GoogleMap API"""
        result_api = get_placeid_from_address(self.user_entry)
        if result_api in (
                {'candidates': [], 'status': 'ZERO_RESULTS'},
                {'candidates': [], 'status': 'INVALID_REQUEST'}
        ):
            self.set_has_user_incomprehension_status(True)
        else:
            self.set_has_user_incomprehension_status(False)
        user_incomprehension_count(self, data_expiration, db_number)
    # def calculate_the_user_entries(self) -> None:
    #     """update the attribute number_of_user_entries
    #     example:
    #     if self.lower_and_split_user_entry is 'openClassrooms ...' X 10 times
    #     after self.lower_and_split_user_entry = 'bonjour' then number_of_the_user_entries += 1"""
    #     if not self.user_behavior['user_indecency'] or \
    #             not self.user_behavior['user_incomprehension']:
    #         if self.user_behavior['number_of_user_entries'] >= 10:
    #             self.user_behavior['number_of_user_entries'] = 10
    #             self.user_behavior['fatigue_quotas'] = True
    #             # display response value in grandpy_code
    #             self.user_behavior['grandpy_code'] = \
    #                 self.__class__.grandpy_status_search_key('Voici Ta Réponse à la question !')
    #             # print(
    #             #     'Grandpy_response : '
    #             #     f"{self.get_grandpy_status(self.user_behavior['grandpy_code'])}"
    #             # )
    #             # display exhausted value in grandpy_code
    #             self.user_behavior['grandpy_code'] = \
    #                 self.__class__.grandpy_status_search_key(
    #                     'je suis fatigué reviens me voir demain !'
    #                 )
    #             # print(f"{self.get_grandpy_status(self.user_behavior['grandpy_code'])}")
    #         elif self.user_behavior['number_of_user_entries'] == 5:
    #             self.user_behavior['number_of_user_entries'] += 1
    #             self.user_behavior['fatigue_quotas'] = False
    #             # display tired value in grandpy_code
    #             self.user_behavior['grandpy_code'] = \
    #                 self.__class__.grandpy_status_search_key(
    #                     'houla, maintenant ma memoire commence a fatiguée" !'
    #                 )
    #             # print(
    #             #     'Grandpy_response : '
    #             #     f"{self.get_grandpy_status(self.user_behavior['grandpy_code'])}"
    #             # )
    #         else:
    #             self.user_behavior['number_of_user_entries'] += 1
    #             self.user_behavior['fatigue_quotas'] = False
    #             # display home value in grandpy_code
    #             self.user_behavior['grandpy_code'] = \
    #                 self.__class__.grandpy_status_search_key(
    #                     "Bonjour Mon petit, en quoi puis-je t'aider ?"
    #                 )
    #             # print(
    #             #     'Grandpy_response[number_of_user_entries<10] : '
    #             #     f"{self.get_grandpy_status(self.user_behavior['grandpy_code'])}"
    #             # )

    def get_request_parser(self) -> str:
        """recover the key words of the user request
        by abolishing word contained in UNNECESSARY_SET_DATA set"""
        list_of_word_request_user = self.user_entry.split()
        list_of_key_word = [
            w for w in list_of_word_request_user
            if w.lower() not in self.__class__.UNNECESSARY_SET_DATA
        ]
        key_word = ' '.join(list_of_key_word)
        return key_word


if __name__ == '__main__':
    pass
