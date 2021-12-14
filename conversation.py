#!/usr/bin/env python
"""conversation management module between grandpyRobot and a user"""
from frozendict import frozendict
import redis_utilities
from google_api import get_placeid_from_address


class Conversation:
    """conversation setting class"""
    def __init__(self, user_entry, db_number=0):
        self.user_entry = user_entry
        self.db_number = db_number
        self.is_fatigue_quotas_in_conversation = redis_utilities.string_to_boolean_conversion(
            redis_utilities.read_access_conversation_data('quotas', self.db_number)
        )
        self.is_user_incivility = redis_utilities.string_to_boolean_conversion(
            redis_utilities.read_access_conversation_data('incivility', self.db_number)
        )
        self.is_user_indecency = redis_utilities.string_to_boolean_conversion(
            redis_utilities.read_access_conversation_data('indecency', self.db_number)
        )
        self.is_user_incomprehension = redis_utilities.string_to_boolean_conversion(
            redis_utilities.read_access_conversation_data('incomprehension', self.db_number)
        )
        self.number_of_incivility = int(redis_utilities.read_access_conversation_data(
            'number_of_incivility', self.db_number
        )
        )
        self.number_of_indecency = int(redis_utilities.read_access_conversation_data(
            'number_of_indecency', self.db_number
        )
        )
        self.number_of_incomprehension = int(redis_utilities.read_access_conversation_data(
            'number_of_incomprehension', self.db_number
        )
        )
        # self.number_of_user_entries = int(redis_utilities.read_access_conversation_data(
        #     'number_of_user_entries', self.db_number
        # )
        # )

    def lower_and_split_user_entry(self) -> list:
        """management of the user_entry attribute"""
        user_entry_lowercase = self.user_entry.lower()
        return user_entry_lowercase.split()

    @classmethod
    def compare_this_set(cls) -> tuple:
        """management of sets to parse it"""
        # Data for check civility
        cls.incivility_set_data = {'bonjour', 'bonsoir', 'salut', 'hello', 'hi'}
        # Data for check decency
        cls.indecency_set_data = {
            'vieux', 'con', 'ancetre', 'poussierieux', 'vieillard', 'demoder', 'dinosaure',
            'senille', 'arrierer', 'decrepit', 'centenaire', 'rococo', 'antiquite', 'senille',
            'gateux', 'archaique', 'croulant', 'vieille', 'baderne', 'fossile', 'foutu', 'bjr',
            'bsr', 'slt'
        }
        # Data for parser (deleted for research)
        cls.unnecessary_set_data = {
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
                'chaque', 'cher', 'chers', 'chez', 'chiche', 'chut', 'chère', 'chères', 'ci','cinq',
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
           }
        data_behavior_sets = (
            cls.incivility_set_data,
            cls.indecency_set_data
        )
        return data_behavior_sets

    @classmethod
    def get_grandpy_status(cls, status_value='home'):
        """Generation of grandpy response according to user entry and Conversation attributes"""
        grandpy_code = frozendict({
            'home': "Bonjour Mon petit, en quoi puis-je t'aider ?",
            'user_question': 'As tu une nouvelle question a me demander ?',
            'response': 'Voici Ta Réponse à la question !',
            'tired': 'houla, maintenant ma memoire commence a fatiguer !',
            'incomprehension': "Ha, Je ne comprends pas, essaye d'être plus précis ... !",
            'mannerless': "s'il te plait, reformule ta question en étant plus polis ... !",
            'disrespectful': "Hola, sois plus RESPECTUEUX ENVERS TES AINES 'MON PETIT' ... !",
            'incivility_limit': 'cette impolitesse me FATIGUE ... !',
            'indecency_limit': 'cette grossierete me FATIGUE ... !',
            'incomprehension_limit': 'cette incomprehension me FATIGUE ... !',
            'exhausted': 'je suis fatigué reviens me voir demain !'
        })
        cls.grandpy_code = status_value
        cls.grandpy_response = grandpy_code[status_value]

    @staticmethod
    def database_init(db_number) -> None:
        """initialization of redis database
        example :
        redis_utilities.write_access_conversation_data ('user_incivility', 'False', self.db_number)
        """
        user_behavior = ['user_incivility', 'user_indecency', 'user_incomprehension', 'quotas']
        behavioral_data_counting = [
            'number_of_incivility', 'number_of_indecency',
            'number_of_incomprehension', 'number_of_user_entries'
        ]
        for behavior in user_behavior:
            redis_utilities.write_access_conversation_data(
                behavior, 'False', db_number
            )
        for counting in behavioral_data_counting:
            redis_utilities.write_access_conversation_data(counting, 0, db_number)

    #
    # def update_database(self) -> None:
    #     """after all data processing update redis database with local attributes
    #     example :
    #     redis_utilities.write_access_conversation_data(
    #         'user_incivility', str(self.is_user_incivility), self.db_number)"""
    #     db_data = [
    #         {'user_incivility': self.is_user_incivility},
    #         {'user_indecency': self.is_user_indecency},
    #         {'user_incomprehension': self.is_user_incomprehension},
    #         {'number_of_incivility': self.number_of_indecency},
    #         {'number_of_indecency': self.number_of_indecency},
    #         {'number_of_incomprehension': self.number_of_indecency},
    #         {'number_of_user_entries': self.number_of_user_entries}
    #     ]
    #     for counting in db_data:
    #         for (data, value) in counting.items():
    #             redis_utilities.write_access_conversation_data(data, str(value), self.db_number)

    def calculate_the_incivility(self) -> tuple:
        """update the attributes is_user_incivility and number_of_incivilities
        example :
        if self.user_entry_data_split is 'Blablabla...'
        then is_user_incivility = True and number_of_incivilities += 1"""
        user_entry_lowercase = self.lower_and_split_user_entry()
        compare = Conversation.compare_this_set()
        civility_set_data = compare[0]
        self.is_user_incivility = civility_set_data.isdisjoint(user_entry_lowercase)
        if self.is_user_incivility:
            if self.number_of_incivility >= 3:
                self.number_of_incivility = 3
                self.is_fatigue_quotas_in_conversation = True
            else:
                self.number_of_incivility += 1
        status_incivility = (
            self.is_user_incivility,
            self.number_of_incivility,
            self.is_fatigue_quotas_in_conversation
        )
        return status_incivility

    def calculate_the_indecency(self) -> tuple:
        """update the attributes is_user_indecency and number_of_indecencies
        example :
        if self.user_entry_data_split is 'vieux...'
        then is_user_indecency = True and number_of_indecencies += 1"""
        user_entry_lowercase = self.lower_and_split_user_entry()
        compare = Conversation.compare_this_set()
        indecency_set_data = compare[1]
        self.is_user_indecency = not indecency_set_data.isdisjoint(user_entry_lowercase)
        if self.is_user_indecency:
            if self.number_of_indecency >= 3:
                self.number_of_indecency = 3
                self.is_fatigue_quotas_in_conversation = True
            else:
                self.number_of_indecency += 1
        status_indecency = (
            self.is_user_indecency,
            self.number_of_indecency,
            self.is_fatigue_quotas_in_conversation
        )
        return status_indecency

    def calculate_the_incomprehension(self) -> tuple:
        """update the attributes is_user_incomprehension and number_of_incomprehension
        if self.user_entry_data_split is 'gjegruiotuygtugyt ...'
        then is_user_incomprehension = True and number_of_incomprehension += 1"""
        result_api = get_placeid_from_address(self.user_entry)
        if result_api in (
                {'candidates': [], 'status': 'ZERO_RESULTS'},
                {'candidates': [], 'status': 'INVALID_REQUEST'}
        ):
            self.is_user_incomprehension = True
            if self.number_of_incomprehension >= 3:
                self.number_of_incomprehension = 3
                self.is_fatigue_quotas_in_conversation = True
            else:
                self.number_of_incomprehension += 1
        else:
            self.is_user_incomprehension = False
        status_incomprehension = (
            self.is_user_incomprehension,
            self.number_of_incomprehension,
            self.is_fatigue_quotas_in_conversation
        )
        return status_incomprehension
    #
    # def calculate_the_user_entries(self) -> int:
    #     """update the attribute number_of_user_entries
    #     if self.user_entry_data_split is 'openClassrooms ...' X 10 times
    #     after self.user_entry_data_split = 'bonjour' then number_of_the_user_entries += 1"""
    #     user_entry_lowercase = self.do_this_from_attribut()
    #     compare = Conversation.compare_this_set()
    #     civility_set_data, indecency_set_data, unnecessary_set_data = [
    #         compare[0], compare[1], compare[2]
    #     ]
    #     if civility_set_data.isdisjoint(user_entry_lowercase) and \
    #             not indecency_set_data.isdisjoint(user_entry_lowercase) and \
    #             not unnecessary_set_data.isdisjoint(user_entry_lowercase):
    #         if self.number_of_user_entries >= 10:
    #             self.number_of_user_entries = 10
    #         else:
    #             self.number_of_user_entries += 1
    #     return self.number_of_user_entries

    def get_request_parser(self):
        """function which cuts the character string
        of the user request with the words present in the unnecessary set
        to keep only the keywords for the search
        example
        user_request = 'where is the Eiffel Tower' ==> get_request_parser = 'eiffel tower'"""
        user_question = self.user_entry.split()
        result = [w for w in user_question if w.lower() not in self.unnecessary_set_data]
        modified_message = ' '.join(result)
        return modified_message


if __name__ == '__main__':
    # chat_session = Conversation('bonjour')
    # chat_session.database_init()
    pass
