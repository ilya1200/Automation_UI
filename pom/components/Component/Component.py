from abc import ABC, abstractmethod

from pom.components.Component import Locators
from infrastructure.SeleniumInfra import SeleniumInfra


class Component(ABC):
    def __init__(self, selenium_infra: SeleniumInfra, locators: Locators, **kwargs):
        self.selenium_infra = selenium_infra
        self.locators = locators
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    @abstractmethod
    def is_visible(self) -> bool:
        pass
