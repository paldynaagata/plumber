import csv 
import Settings
import Constants

from Singleton import Singleton

class __Localization(metaclass = Singleton):
    """
    Class providing localization services
    """

    def __init__(self):
        self._dictionaries = None
        self._load_localization()


    def get_text(self, key):
        return self._dictionaries[Settings.get_language()][f"{key}"]


    def get_available_languages(self):
        return list(self._dictionaries.keys())


    def _load_localization(self):
        with open('localization.csv', mode = 'r', encoding = Constants.encoding) as file:
            reader = csv.DictReader(file)
            langs = list(reader.fieldnames)[1:]
            self._dictionaries = dict((lang, dict()) for lang in langs)
            for row in reader:
                for lang in langs:
                    self._dictionaries[lang][row['key']] = row[lang]


instance = __Localization()


def get_text(key):
    return instance.get_text(key)


def get_available_languages():
    return instance.get_available_languages()