from typing import List

from selenium.webdriver.remote.webelement import WebElement

from infrastructure.SeleniumInfra import SeleniumInfra
from pom.components.Component.Component import Component
from pom.components.Navigator.NavNotFoundException import NavNotFoundException
from pom.components.Navigator.NavigatorLocators import NavigatorLocators


class Navigator(Component):

    def __init__(self, selenium_infra: SeleniumInfra, locators: NavigatorLocators, **kwargs):
        super().__init__(selenium_infra, locators, **kwargs)
        self.locators: NavigatorLocators = locators

    @property
    def element(self) -> WebElement:
        return self.selenium_infra.find_element_by(*self.locators.element)

    @property
    def is_visible(self) -> bool:
        return self.selenium_infra.is_element_exist(*self.locators.element)

    def navigate_to(self, page_name: str):
        pages: List[WebElement] = self.selenium_infra.find_element_list_by(*self.locators.nav_tab)
        for page in pages:
            if page_name.upper() == page.text.upper():
                self.selenium_infra.click_element(element=page)
                return
        raise NavNotFoundException(page_name)
