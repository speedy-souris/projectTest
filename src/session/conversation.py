"""conversation management module between grandpyRobot and a user"""
from collections import OrderedDict
from frozenordereddict import FrozenOrderedDict
from . import write_access_conversation_data, read_access_conversation_data
from . import erasing_data, value_to_string_conversion


class Conversation:
    """conversation setting class"""
    # database initialization behavior parameter
    USER_BEHAVIOR_DEFAULT_DATA = FrozenOrderedDict({
        'has_user_incivility_status': False,
        'has_user_indecency_status': False,
        'has_user_indecency_status2': False,
        'has_user_incomprehension_status': False,
        'has_user_incomprehension_status2': False,
        'has_fatigue_quotas_of_grandpy': False,
        'grandpy_status_code': 'home',
        'behavior_level': 'presentation',
        'number_of_user_incivility': 0,
        'number_of_user_indecency': 0,
        'number_of_user_indecency2': 0,
        'number_of_user_incomprehension': 0,
        'number_of_user_incomprehension2': 0,
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
            'has_user_indecency_status2': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[2],
            'has_user_incomprehension_status': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[3],
            'has_user_incomprehension_status2': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[4],
            'has_fatigue_quotas_of_grandpy': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[5],
            'grandpy_status_code': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[6],
            'behavior_level': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[7],
            'number_of_user_incivility': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[8],
            'number_of_user_indecency': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[9],
            'number_of_user_indecency2': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[10],
            'number_of_user_incomprehension': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[11],
            'number_of_user_incomprehension2': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[12],
            'number_of_user_entries': cls.USER_BEHAVIOR_DEFAULT_DATA_KEYS[13]
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
            'inconsistency': cls.GRANDPY_STATUS_DATA_KEYS[4],
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

    def user_behavior_init_ordered(self) -> dict:
        """user behavior initialization parameter"""
        if not read_access_conversation_data(self.__class__.get_user_behavior_key(
                'has_fatigue_quotas_of_grandpy'), self.db_number):
            list_attributs_names, list_attributs_values = [], []
            for name in self.__class__.USER_BEHAVIOR_DEFAULT_DATA_KEYS:
                list_attributs_names.append(name)
                list_attributs_values.append(
                    read_access_conversation_data(name, self.db_number))
            behavioral_data = OrderedDict(zip(list_attributs_names, list_attributs_values))
        else:
            #  deletion of data from database 1 ==> database for Test
            erasing_data(1)
            # deletion of data from database 0 ==> database for prod
            erasing_data(0)
            behavioral_data = self.database_init_ordered()
        return behavioral_data

    def database_init_ordered(self) -> dict:
        """initialization of redis database
        with a key, its value and the ID of the redis database
        example :
        redis_utilities.write_access_conversation_data ('grandpy_status_code', 'home', 0)"""
        list_attributs_names, list_attributs_values = [], []
        for (name, value) in self.__class__.USER_BEHAVIOR_DEFAULT_DATA.items():
            list_attributs_names.append(name)
            list_attributs_values.append(value)
        behavioral_data = OrderedDict(zip(list_attributs_names, list_attributs_values))

        for (name, value) in behavioral_data.items():
            write_access_conversation_data(
                name, value, self.db_number
            )
        return behavioral_data

    def lower_and_split_user_entry(self) -> list:
        """management of the user_entry attribute"""
        user_entry_lowercase = self.user_entry.lower()
        return user_entry_lowercase.split()

    def update_database(self) -> None:
        """after all data processing update redis database with local attributes
        example :
        write_access_conversation_data(
            'has_user_incivility_status', str(self.user_behavior['user_incivility']), db_number)"""
        chat_session_attribut_value = {
            # has_user_incivility_status
            self.__class__.get_user_behavior_key('has_user_incivility_status'):
                self.user_behavior[
                self.__class__.get_user_behavior_key('has_user_incivility_status')],
            # has_user_indecency_status
            self.__class__.get_user_behavior_key('has_user_indecency_status'):
                self.user_behavior[
                self.__class__.get_user_behavior_key('has_user_indecency_status')],
            # has_user_indecency_status2
            self.__class__.get_user_behavior_key('has_user_indecency_status2'):
                self.user_behavior[
                    self.__class__.get_user_behavior_key('has_user_indecency_status2')],
            # has_user_incomprehension_status
            self.__class__.get_user_behavior_key('has_user_incomprehension_status'):
                self.user_behavior[
                self.__class__.get_user_behavior_key('has_user_incomprehension_status')],
            # has_user_incomprehension_status2
            self.__class__.get_user_behavior_key('has_user_incomprehension_status2'):
                self.user_behavior[
                    self.__class__.get_user_behavior_key('has_user_incomprehension_status2')],
            # has_fatigue_quotas_of_grandpy
            self.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy'):
                self.user_behavior[
                self.__class__.get_user_behavior_key('has_fatigue_quotas_of_grandpy')],
            # grandpy_status_code
            self.__class__.get_user_behavior_key('grandpy_status_code'):
                self.user_behavior[self.__class__.get_user_behavior_key('grandpy_status_code')],
            # behavior_level
            self.__class__.get_user_behavior_key('behavior_level'):
                self.user_behavior[self.__class__.get_user_behavior_key('behavior_level')],
            # number_of_user_incivility
            self.__class__.get_user_behavior_key('number_of_user_incivility'):
                self.user_behavior[
                self.__class__.get_user_behavior_key('number_of_user_incivility')],
            # number_of_user_indecency
            self.__class__.get_user_behavior_key('number_of_user_indecency'):
                self.user_behavior[
                    self.__class__.get_user_behavior_key('number_of_user_indecency')],
            # number_of_user_indecency2
            self.__class__.get_user_behavior_key('number_of_user_indecency2'):
                self.user_behavior[
                    self.__class__.get_user_behavior_key('number_of_user_indecency2')],
            # number_of_user_incomprehension
            self.__class__.get_user_behavior_key('number_of_user_incomprehension'):
                self.user_behavior[
                self.__class__.get_user_behavior_key('number_of_user_incomprehension')],
            # number_of_user_incomprehension2
            self.__class__.get_user_behavior_key('number_of_user_incomprehension2'):
                self.user_behavior[
                    self.__class__.get_user_behavior_key('number_of_user_incomprehension2')],
            # number_of_user_entries
            self.__class__.get_user_behavior_key('number_of_user_entries'):
                self.user_behavior[self.__class__.get_user_behavior_key('number_of_user_entries')]
        }
        # (in database redis) writing all
        for (name_attribut, value_attribut) in chat_session_attribut_value.items():
            write_access_conversation_data(
                name_attribut, value_to_string_conversion(value_attribut),
                self.db_number)

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
