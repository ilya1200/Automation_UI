from infrastructure.SeleniumInfra import SeleniumInfra
from pom.components.InitComponents.InitComponents import InitComponents
from pom.pages.RegisterPage.RegisterPage import RegisterPage
from pom.pages.RegisterPage.RegisterPageLocators import RegisterPageLocators
from pom.pages.WebTablePage.WebTablePage import WebTablePage
from pom.pages.WebTablePage.WebTablePageLocators import WebTablePageLocators


class InitPages:
    REGISTER_URL = "http://demo.automationtesting.in/Register.html"
    WEB_TABLE_URL = 'http://demo.automationtesting.in/WebTable.html'

    def __init__(self, selenium_infra: SeleniumInfra, components: InitComponents):
        self.register_page = RegisterPage(selenium_infra, RegisterPageLocators(), self.REGISTER_URL, components.register_form)
        self.web_table_page = WebTablePage(selenium_infra, WebTablePageLocators(), self.WEB_TABLE_URL)
