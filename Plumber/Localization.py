import csv 
import Settings

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


    def _load_localization(self):
        with open('localization.csv', mode = 'r', encoding = 'utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            langs = list(reader.fieldnames)[1:]
            self._dictionaries = dict((lang, dict()) for lang in langs)
            for row in reader:
                for lang in langs:
                    self._dictionaries[lang][row['key']] = row[lang]


instance = __Localization()


def get_text(key):
    return instance.get_text(key)