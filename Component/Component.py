from abc import ABC, abstractmethod

from Component.Locators import Locators
from infrastructure.SeleniumInfra import SeleniumInfra


class Component(ABC):
    def __init__(self, infra: SeleniumInfra, locators: Locators, **kwargs):
        self.infra = infra
        self.locators = locators
        for key, value in kwargs:
            self.__setattr__(key, value)

    @abstractmethod
    def is_visible(self) -> bool:
        pass
