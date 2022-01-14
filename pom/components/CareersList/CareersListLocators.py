from selenium.webdriver.common.by import By

from pom.components.Component.Locators import Locators


class CareersListLocators(Locators):
    def __init__(self):
        self.element = (By.CLASS_NAME, 'app-container')
        self.open_positions = (By.XPATH, "//*[contains(text(),'open positions')]")
        self.load_more_btn = (By.CLASS_NAME, 'load-more')


