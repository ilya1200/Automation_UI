from typing import List, Dict, Any
from selenium.webdriver.remote.webelement import WebElement
from infrastructure.SeleniumInfra import SeleniumInfra
from pom.components.CareerItem.CareerItemLocators import CareerItemLocators
from pom.components.Component.Component import Component


class CareerItem(Component):
    def __init__(self, selenium_infra: SeleniumInfra, locators: CareerItemLocators, element: WebElement = None,
                 **kwargs):
        super().__init__(selenium_infra, locators, **kwargs)
        self.locators: CareerItemLocators = locators
        self._element: WebElement = element

    @property
    def element(self) -> WebElement:
        return self._element if self._element else self.selenium_infra.find_element_by(*self.locators.element)

    @element.setter
    def element(self, element: WebElement):
        self._element = element

    @property
    def is_visible(self) -> bool:
        if self._element:
            return self.selenium_infra.is_element_exist(element=self._element)
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
        tags_elements: List[WebElement] = self.selenium_infra.find_element_list_by(*self.locators.tags,
                                                                                   from_element=self.element)
        return list(map(lambda tags_element: tags_element.text, tags_elements))

    def explore_position(self):
        self.selenium_infra.click_element(*self.locators.link, from_element=self.element)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "link": self.link,
            "title": self.title,
            "subtitle": self.subtitle,
            "city": self.city,
            "tags": self.tags
        }

    def __str__(self):
        return str(self.to_dict())
