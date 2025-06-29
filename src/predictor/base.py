from abc import ABC, abstractmethod


class IPredictor(ABC):
    @abstractmethod
    def run():
        pass
