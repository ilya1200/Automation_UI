from config import REGISTER_PAGE_URL, WEB_TABLE_PAGE_URL
from infrastructure.SeleniumInfra import SeleniumInfra
from pom.InitPOM.InitComponents import InitComponents
from pom.pages.RegisterPage.RegisterPage import RegisterPage
from pom.pages.RegisterPage.RegisterPageLocators import RegisterPageLocators
from pom.pages.WebTablePage.WebTablePage import WebTablePage
from pom.pages.WebTablePage.WebTablePageLocators import WebTablePageLocators


class InitPages:
    def __init__(self, selenium_infra: SeleniumInfra, components: InitComponents):
        self.register_page = RegisterPage(selenium_infra, RegisterPageLocators(), REGISTER_PAGE_URL, components.register_form)
        self.web_table_page = WebTablePage(selenium_infra, WebTablePageLocators(), WEB_TABLE_PAGE_URL)
