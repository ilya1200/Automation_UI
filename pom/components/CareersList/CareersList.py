from typing import List

from selenium.webdriver.remote.webelement import WebElement
from infrastructure.SeleniumInfra import SeleniumInfra
from pom.components.CareerItem.CareerItem import CareerItem
from pom.components.CareerItem.CareerItemLocators import CareerItemLocators
from pom.components.Component.Component import Component
from pom.components.CareersList.CareersListLocators import CareersListLocators


class CareersList(Component):
    def __init__(self, selenium_infra: SeleniumInfra, locators: CareersListLocators, **kwargs):
        super().__init__(selenium_infra, locators, **kwargs)
        self.locators: CareersListLocators = locators

    @property
    def element(self) -> WebElement:
        return self.selenium_infra.find_element_by(*self.locators.element)

    @property
    def is_visible(self) -> bool:
        return self.selenium_infra.is_element_exist(*self.locators.element)

    @property
    def open_positions(self) -> int:
        positions_txt = self.selenium_infra.get_text(*self.locators.open_positions, from_element=self.element)
        return int(positions_txt.split()[0])

    @property
    def is_load_more_visible(self) -> bool:
        return self.selenium_infra.is_element_exist(*self.locators.load_more_btn, from_element=self.element)

    @property
    def items(self) -> List[CareerItem]:
        career_items: List[CareerItem] = list()

        index = 0
        while True:
            career_item: CareerItem = CareerItem(self.selenium_infra, CareerItemLocators(index))
            if not career_item.is_visible:
                break
            career_items.append(career_item)
            index += 1

        return career_items

    def load_more_positions(self):
        self.selenium_infra.click_element(*self.locators.load_more_btn, from_element=self.element)

    def expand_all_positions(self):
        while self.is_load_more_visible:
            self.load_more_positions()

    def count_open_positions(self) -> int:
        return len(self.items)
