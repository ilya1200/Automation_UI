from infrastructure.SeleniumInfra import SeleniumInfra
from pom.components.CareersList.CareersList import CareersList
from pom.components.CareersList.CareersListLocators import CareersListLocators
from pom.components.RegisterForm.RegisterForm import RegisterForm
from pom.components.RegisterForm.RegisterFormLocators import RegisterFormLocators


class InitComponents:

    def __init__(self, selenium_infra: SeleniumInfra):
        self.register_form = RegisterForm(selenium_infra, RegisterFormLocators())
        self.carres_list = CareersList(selenium_infra, CareersListLocators())

