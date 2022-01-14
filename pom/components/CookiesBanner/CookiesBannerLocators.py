from selenium.webdriver.common.by import By

from pom.components.Component.Locators import Locators


class CookiesBannerLocators(Locators):
    def __init__(self):
        self.element = (By.XPATH, "//*[@id='onetrust-banner-sdk']")
        self.ok_btn = (By.XPATH, ".//*[@id='onetrust-accept-btn-handler']")
        self.close = (By.CLASS_NAME, 'banner-close-button')
