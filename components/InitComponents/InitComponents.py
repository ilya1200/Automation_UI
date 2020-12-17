from components.RegisterForm.RegisterForm import RegisterForm
from components.RegisterForm.RegisterFormLocators import RegisterFormLocators
from infrastructure.SeleniumInfra import SeleniumInfra


class InitComponents:

    def __init__(self, infra: SeleniumInfra):
        self.register_form = RegisterForm(infra, RegisterFormLocators())

