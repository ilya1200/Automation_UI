from selenium.webdriver.common.by import By

from pom.components.Component.Locators import Locators


class RegisterFormLocators(Locators):
    def __init__(self):
        self.element = (By.XPATH, '//form[@id="basicBootstrapForm"]')
        self.first_name = (By.XPATH, '//input[@ng-model="FirstName"]')
        self.last_name = (By.XPATH, '//input[@ng-model="LastName"]')
        self.email_address = (By.XPATH, '//input[@ng-model="EmailAdress"]')
        self.phone = (By.XPATH, '//input[@ng-model="Phone"]')
        self.gender_male = (By.XPATH, '//input[@value="Male"]')
        self.gender_female = (By.XPATH, '//input[@value="FeMale"]')
        self.country_dropdown = (By.XPATH, '//select[@ng-model="country"]')
        self.required = (By.XPATH, "//label[contains(text(),'*')]")
        self.submit_btn = (By.XPATH, '//button[@id="submitbtn"]')
        self.refresh_btn = (By.XPATH, '//button[@value="Refresh"]')
        self.date_of_birth_year = (By.XPATH, '//*[@id="yearbox"]')
        self.date_of_birth_month = (By.XPATH, '//*[@ng-model="monthbox"]')
        self.date_of_birth_day = (By.XPATH, '//*[@id="daybox"]')
        self.password = (By.XPATH, '//input[@id="firstpassword"]')
        self.confirm_password = (By.XPATH, '//input[@id="secondpassword"]')
        self.choose_file_btn = (By.XPATH, '//*[@id="imagesrc"]')





