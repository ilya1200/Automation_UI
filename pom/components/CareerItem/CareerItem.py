from typing import List

from selenium.webdriver.remote.webelement import WebElement

from infrastructure.SeleniumInfra import SeleniumInfra
from pom.components.CareerItem.CareerItemLocators import CareerItemLocators
from pom.components.Component.Component import Component


class CareerItem(Component):
    def __init__(self, selenium_infra: SeleniumInfra, locators: CareerItemLocators, **kwargs):
        super().__init__(selenium_infra, locators, **kwargs)
        self.locators: CareerItemLocators = locators

    @property
    def element(self) -> WebElement:
        return self.selenium_infra.find_element_by(*self.locators.element)

    @property
    def is_visible(self) -> bool:
        return self.selenium_infra.is_element_exist(*self.locators.element)

    @property
    def link(self) -> str:
        return self.selenium_infra.get_attribute_from_element("href", *self.locators.link, from_element=self.element)

    @property
    def title(self) -> str:
        return self.selenium_infra.get_text(*self.locators.title, from_element=self.element)

    @property
    def subtitle(self) -> str:
        return self.selenium_infra.get_text(*self.locators.subtitle, from_element=self.element)

    @property
    def city(self) -> str:
        return self.selenium_infra.get_text(*self.locators.city, from_element=self.element)

    @property
    def tags(self) -> List[str]:
        tags_elements: List[WebElement] = self.selenium_infra.find_element_list_by(*self.locators.tags, from_element=self.element)
        return list(map(lambda tags_element: tags_element.text(), tags_elements))

    def explore_position(self):
        self.selenium_infra.click_element(*self.locators.link, from_element=self.element)
