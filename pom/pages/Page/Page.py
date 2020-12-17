from selenium.common.exceptions import TimeoutException

from pom.components.Component import Locators
from pom.components.Component.Component import Component
from infrastructure.SeleniumInfra import SeleniumInfra


class Page(Component):
    def __init__(self, selenium_infra: SeleniumInfra, locators: Locators, url: str, **kwargs):
        super().__init__(selenium_infra, locators, **kwargs)
        self.url = url

    @property
    def is_visible(self) -> bool:
        try:
            self.selenium_infra.wait_for_url_to_be(self.url)
        except TimeoutException:
            return False
        return self.selenium_infra.current_url == self.url

    def move_to_page(self):
        self.selenium_infra.get(self.url)


