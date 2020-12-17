from components.InitComponents.InitComponents import InitComponents
from infrastructure.SeleniumInfra import SeleniumInfra
from pages.RegisterPage.RegisterPage import RegisterPage
from pages.RegisterPage.RegisterPageLocators import RegisterPageLocators
from pages.WebTablePage.WebTablePage import WebTablePage
from pages.WebTablePage.WebTablePageLocators import WebTablePageLocators


class InitPages:
    REGISTER_URL = "http://demo.automationtesting.in/Register.html"
    WEB_TABLE_URL = 'http://demo.automationtesting.in/WebTable.html'

    def __init__(self, infra: SeleniumInfra):
        self.components = InitComponents(infra)
        self.register_page = RegisterPage(infra, RegisterPageLocators(), self.REGISTER_URL, self.components.register_form)
        self.web_table_page = WebTablePage(infra, WebTablePageLocators(), self.WEB_TABLE_URL)
