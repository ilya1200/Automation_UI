from typing import List

from selenium.webdriver.remote.webelement import WebElement

from infrastructure.SeleniumInfra import SeleniumInfra
from pom.components.Navigator.Navigator import Navigator
from pom.pages.AboutPage.AboutPageLocators import AboutPageLocators
from pom.pages.Page.Page import Page


class AboutPage(Page):
    def __init__(self, selenium_infra: SeleniumInfra, locators: AboutPageLocators, url: str, navigator: Navigator,
                 **kwargs):
        super().__init__(selenium_infra, locators, url, **kwargs)
        self.navigator: Navigator = navigator
        self.locators: AboutPageLocators = locators

    @property
    def headers(self) -> List[str]:
        headers_elements: List[WebElement] = self.selenium_infra.find_element_list_by(*self.locators.section_header)
        return list(map(lambda header: header.text, headers_elements))
