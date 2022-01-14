from infrastructure.SeleniumInfra import SeleniumInfra
from pom.components.CareersList.CareersList import CareersList
from pom.components.CareersList.CareersListLocators import CareersListLocators


class InitComponents:

    def __init__(self, selenium_infra: SeleniumInfra):
        self.careers_list = CareersList(selenium_infra, CareersListLocators())

