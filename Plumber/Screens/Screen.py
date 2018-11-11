from abc import ABC, abstractmethod

class Screen(ABC):
    """
    Abstract class representing screen
    """

    @abstractmethod
    def show(self, window, events):
        return self