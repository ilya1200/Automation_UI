from selenium.webdriver.remote.webelement import WebElement

from infrastructure.SeleniumInfra import SeleniumInfra
from pom.components.Component.Component import Component
from pom.components.CookiesBanner.CookiesBannerLocators import CookiesBannerLocators


class CookiesBanner(Component):
    def __init__(self, selenium_infra: SeleniumInfra, locators: CookiesBannerLocators, **kwargs):
        super().__init__(selenium_infra, locators, **kwargs)
        self.locators: CookiesBannerLocators = locators

    @property
    def element(self) -> WebElement:
        return self.selenium_infra.find_element_by(*self.locators.element)

    @property
    def is_visible(self) -> bool:
        return self.selenium_infra.is_element_exist(*self.locators.element)

    def accept(self):
        self.selenium_infra.click_element(*self.locators.ok_btn, from_element=self.element)

    def dismiss(self):
        self.selenium_infra.click_element(*self.locators.close, from_element=self.element)
