from infrastructure.SeleniumInfra import SeleniumInfra
from pom.components.Navigator.Navigator import Navigator
from pom.pages.HomePage.HomePageLocators import HomePageLocators
from pom.pages.Page.Page import Page


class HomePage(Page):
    def __init__(self, selenium_infra: SeleniumInfra, locators: HomePageLocators, url: str, navigator: Navigator, **kwargs):
        super().__init__(selenium_infra, locators, url, **kwargs)
        self.navigator: Navigator = navigator