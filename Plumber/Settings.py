import Localization

from Singleton import Singleton

class __Settings(metaclass = Singleton):
    """
    Class responsible for change of settings
    """

    def __init__(self):
        self._languages = Localization.get_available_languages()

        self.language = self._languages[0]
        self.sound_enable = True
        self.scale_factor = 1


    def _get_next_value(self, collection, value):
        next_index = collection.index(value) + 1
        next_index = next_index % len(collection)
        new_value = collection[next_index]
        return new_value    


    def toggle_sound_enable(self):
        self.sound_enable = not self.sound_enable
        return self.sound_enable


    def set_to_next_language(self):
        self.language = self._get_next_value(self._languages, self.language)
        return self.language


instance = __Settings()


def toggle_sound_enable():
    return instance.toggle_sound_enable()


def set_to_next_language():
    return instance.set_to_next_language()


def get_language():
    return instance.language


def get_sound_enable():
    return instance.sound_enable


def set_scale_factor(factor):
    instance.scale_factor = factor


def get_scale_factor():
    return instance.scale_factor