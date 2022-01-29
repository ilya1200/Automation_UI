from pom.components.Component.Locators import Locators
from selenium.webdriver.common.by import By


class AboutPageLocators(Locators):
    def __init__(self):
        self.section_header = (By.TAG_NAME, 'h2')

