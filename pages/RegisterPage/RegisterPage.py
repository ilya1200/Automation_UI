from Page.Page import Page
from infrastructure.SeleniumInfra import SeleniumInfra
from pages.RegisterPage.RegisterPageLocators import RegisterPageLocators


class RegisterPage(Page):
    def __init__(self, infra: SeleniumInfra, locators: RegisterPageLocators, url: str, **kwargs):
        super().__init__(infra, locators, url, **kwargs)
