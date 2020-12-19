from infrastructure.SeleniumInfra import SeleniumInfra
from pom.components.RegisterForm.RegisterForm import RegisterForm
from pom.components.RegisterForm.RegisterFormLocators import RegisterFormLocators


class InitComponents:

    def __init__(self, selenium_infra: SeleniumInfra):
        self.register_form = RegisterForm(selenium_infra, RegisterFormLocators())

