from infrastructure.SeleniumInfra import SeleniumInfra
from pom.Page.Page import Page
from pom.components.RegisterForm.RegisterForm import RegisterForm
from pom.pages.RegisterPage.RegisterPageLocators import RegisterPageLocators


class RegisterPage(Page):
    def __init__(self, selenium_infra: SeleniumInfra, locators: RegisterPageLocators, url: str, register_form: RegisterForm, **kwargs):
        super().__init__(selenium_infra, locators, url, **kwargs)
        self.register_form = register_form
