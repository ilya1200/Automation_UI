from selenium.webdriver.common.by import By
from pom.components.Component.Locators import Locators


class CareerItemLocators(Locators):
    def __init__(self, index: int):
        self.element = (By.XPATH, f'(//*[contains(@class,"career-item")])[{index+1}]')
        self.link = (By.XPATH, ".//*[contains(@class, 'fw-link')]")
        self.title = (By.CSS_SELECTOR, ".row a")
        self.subtitle = (By.CSS_SELECTOR, ".row .small")
        self.city = (By.CLASS_NAME, 'city')
        self.tags = (By.CSS_SELECTOR, ".tags .capsule")
