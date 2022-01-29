from config import TECHDEMO_PAGE_URL
from infrastructure.SeleniumInfra import SeleniumInfra
from pom.InitPOM.InitComponents import InitComponents
from pom.pages.HomePage.HomePage import HomePage
from pom.pages.HomePage.HomePageLocators import HomePageLocators


class InitPages:
    def __init__(self, selenium_infra: SeleniumInfra, components: InitComponents):
        self.home_page = HomePage(selenium_infra, HomePageLocators(), TECHDEMO_PAGE_URL,
                                        components.navigator)
