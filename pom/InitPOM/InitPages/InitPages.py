from config import CAREERS_ISRAEL_PAGE_URL
from infrastructure.SeleniumInfra import SeleniumInfra
from pom.InitPOM.InitComponents import InitComponents
from pom.pages.CareersPage.CareersPage import CareersPage
from pom.pages.CareersPage.CareersPageLocators import CareersPageLocators


class InitPages:
    def __init__(self, selenium_infra: SeleniumInfra, components: InitComponents):
        self.careers_page = CareersPage(selenium_infra, CareersPageLocators(), CAREERS_ISRAEL_PAGE_URL, components.careers_list)
