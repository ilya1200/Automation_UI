from infrastructure.SeleniumInfra import SeleniumInfra
from pom.pages.Page.Page import Page
from pom.pages.WebTablePage.WebTablePageLocators import WebTablePageLocators


class WebTablePage(Page):
    def __init__(self, selenium_infra: SeleniumInfra, locators: WebTablePageLocators, url: str, **kwargs):
        super().__init__(selenium_infra, locators, url, **kwargs)

