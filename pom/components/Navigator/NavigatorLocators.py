from selenium.webdriver.common.by import By

from pom.components.Component.Locators import Locators


class NavigatorLocators(Locators):
    def __init__(self):
        self.element = (By.ID, "main_menu")
        self.nav_tab = (By.CSS_SELECTOR, "#main_menu>.menu-item>a")
