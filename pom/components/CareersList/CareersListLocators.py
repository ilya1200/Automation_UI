from selenium.webdriver.common.by import By

from pom.components.Component.Locators import Locators


class CareersListLocators(Locators):
    def __init__(self):
        self.element = (By.ID, 'content')
        self.open_positions = (By.XPATH, "//*[contains(text(),'open positions')]")


