from Page.Page import Page
from infrastructure.SeleniumInfra import SeleniumInfra
from pages.WebTablePage.WebTablePageLocators import WebTablePageLocators


class WebTablePage(Page):
    def __init__(self, infra: SeleniumInfra, locators: WebTablePageLocators, url: str, **kwargs):
        super().__init__(infra, locators, url, **kwargs)

