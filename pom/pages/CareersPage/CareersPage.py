from infrastructure.SeleniumInfra import SeleniumInfra
from pom.components.CareersList.CareersList import CareersList
from pom.pages.Page.Page import Page
from pom.pages.CareersPage.CareersPageLocators import CareersPageLocators


class CareersPage(Page):
    def __init__(self, selenium_infra: SeleniumInfra, locators: CareersPageLocators, url: str, careers_list: CareersList, **kwargs):
        super().__init__(selenium_infra, locators, url, **kwargs)
        self.careers_list = careers_list