from Page.Page import Page
from components.RegisterForm.RegisterForm import RegisterForm
from infrastructure.SeleniumInfra import SeleniumInfra
from pages.RegisterPage.RegisterPageLocators import RegisterPageLocators


class RegisterPage(Page):
    def __init__(self, infra: SeleniumInfra, locators: RegisterPageLocators, url: str, register_form: RegisterForm, **kwargs):
        super().__init__(infra, locators, url, **kwargs)
        self.register_form = register_form
