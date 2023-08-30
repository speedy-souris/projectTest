"""conversation management module between grandpyRobot and a user"""
from . import google_api
from . import RedisDataManagement

class Conversation:
    """conversation setting class"""
    # Default value of grandpy status attributes
    grandpy_status_code_value = {
        'home': "Bonjour Mon petit, en quoi puis-je t'aider ?",
        'benevolent': "Ok, c'est tres bien mon petit !",
        'response': "Voici la reponse à t'as questions !",
        'tired': 'Houla, maintenant ma memoire commence à fatiguée !',
        'incomprehension': "Ha, je ne comprends pas, essaye d'être plus précis ... !",
        'mannerless': "S'il te plait, reformule ta question en étant plus polis ... !",
        'disrespectful': "Hola, sois plus RESPECTUEUX ENVERS TES AINES 'MON PETIT' ... !",
        'incivility_limit': 'Cette impolitesse me FATIGUE ... !',
        'indecency_limit': 'Cette grossièreté me FATIGUE ... !',
        'incomprehension_limit': 'Cette incomprehension me FATIGUE ... !',
        'response_limit': 'HEY ! CA SUFFIT mon petit, ma mémoire est saturé ... !',
        'exhausted': 'Je suis fatigué reviens me voir demain !'}
    # -------------------------------
    # Data for check incivility user behavior
    INCIVILITY_SET_DATA = frozenset({'bonjour', 'bonsoir', 'salut', 'hello', 'hi'})
    # Data for check indecency user behavior
    INDECENCY_SET_DATA = frozenset({
        'vieux', 'con', 'ancetre', 'poussierieux', 'vieillard', 'demoder', 'dinosaure',
        'senile', 'arrierer', 'decrepit', 'centenaire', 'rococo', 'antiquite', 'gateux',
        'archaique', 'croulant', 'vieille', 'baderne', 'fossile', 'foutu', 'bjr', 'bsr', 'slt'})
    # Data for check incomprehension user behavior
    # ~ INCOMPREHENSION_SET_DATA = frozenset({'~', '#', '|', '\\', '€', '/', '&'})
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

    def __init__(self, user_entry, database_redis_number=0, **args):
        self.user_entry = user_entry
        self.parsed_user_entry = ''
        self.db_session = RedisDataManagement(database_redis_number=database_redis_number)
        self.level = args.get('level', 1)
        # Leve1 1 --> Presentation
        self.has_user_incivility_status = args.get('has_user_incivility_status', False)
        self.number_of_user_incivility = args.get('number_of_user_incivility', 0)
        # Level 1 --> Presentation and Level 2 --> chat_object_connect
        self.has_user_indecency_status = args.get('has_user_indecency_status', False)
        self.has_user_incomprehension_status = \
            args.get('has_user_incomprehension_status', False)
        self.number_of_user_indecency = args.get('number_of_user_indecency', 0)
        self.number_of_user_incomprehension = args.get('number_of_user_incomprehension', 0)
        self.number_of_user_entries = args.get('number_of_user_entries', 0)
        self.has_fatigue_quotas_of_grandpy = args.get('has_fatigue_quotas_of_grandpy', False)
        self.previous_has_fatigue_quotas_of_grandpy = self.has_fatigue_quotas_of_grandpy
        self.grandpy_status_code =\
            args.get('grandpy_status_code', self.__class__.grandpy_status_code_value['home'])
        self.previous_grandpy_status_code = self.grandpy_status_code
        

    def __str__(self):
        text = ''
        if self.level == 1:
            text = \
                f"Niveau : {self.level}, incivility / indecency / incomprehension"
        elif self.level == 2:
            text = f"Niveau : {self.level}, indecency / incomprehension"
        return text

    def from_level1_to_level2(self):
        """transition method from level 1 (Presentation) to level 2 (chat_object_connect)"""
        self.level = 2
        self.has_user_incivility_status = False
        self.number_of_user_incivility = 0
        self.has_user_indecency_status = False
        self.number_of_user_indecency = 0
        self.has_user_incomprehension_status = False
        self.number_of_user_incomprehension = 0
        self.grandpy_status_code = 'benevolent'

    def calculate_the_incivility_status(self) -> None:
        """update the attribut has_user_incivility_status since INCIVILITY_SET_DATA set"""
        user_entry_lowercase = self.lower_and_split_user_entry()
        incivility_set_data = self.__class__.INCIVILITY_SET_DATA
        self.has_user_incivility_status =\
            incivility_set_data.isdisjoint(user_entry_lowercase)

    def calculate_the_indecency_status(self) -> None:
        """update the attribut has_user_indecency_status since INDECENCY_SET_DATA set"""
        user_entry_lowercase = self.lower_and_split_user_entry()
        indecency_set_data = self.__class__.INDECENCY_SET_DATA
        self.has_user_indecency_status =\
            not indecency_set_data.isdisjoint(user_entry_lowercase)

    def calculate_the_incomprehension_status(self) -> dict:
        """update the attribut has_user_indecency_status since GoogleMap API"""
        # ~ import pdb; pdb.set_trace()
        # ~ incomprehension_status = False
        incomprehension_status = True
        result_api = google_api.search_address_to_gMap(self.parsed_user_entry)
        if bool(self.parsed_user_entry):
            print(f'[in conversation_as_incomprehension1] = {result_api}')
            print (f'[in conversation_as_incomprehension2]  = {self.user_entry}')
            if type(result_api) is dict and 'result' in result_api:
                if bool(result_api['result']):
                    incomprehension_status = False
        self.has_user_incomprehension_status = incomprehension_status
        coordinates_googleMap_API = ' '
        if bool(self.parsed_user_entry):
            try:
            # ~ if type(result_api) is dict and 'result' in result_api:
                coordinates_googleMap_API = result_api#['result']['geometry']['location']
            except (KeyError, TypeError):
                coordinates_googleMap_API = {}
            else:
                print(f'[calculate_incomprehension] = {coordinates_googleMap_API}')
                return coordinates_googleMap_API

    def lower_and_split_user_entry(self) -> list:
        """management of the user_entry attribute"""
        user_entry_lowercase = self.user_entry.lower()
        return user_entry_lowercase.split()

    def get_user_request_parser(self) -> None:
        """recover the keywords of the user request
        by abolishing word contained in UNNECESSARY_SET_DATA set"""
        list_of_word_request_user = self.user_entry.split()
        list_of_keyword = [
            w for w in list_of_word_request_user
            if w.lower() not in self.__class__.UNNECESSARY_SET_DATA]
        # ~ list_of_keyword = list_of_word_request_user
        if list_of_keyword != []:
            self.parsed_user_entry = ' '.join(list_of_keyword)


if __name__ == '__main__':
    pass
