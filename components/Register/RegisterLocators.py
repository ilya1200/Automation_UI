from selenium.webdriver.common.by import By


class RegisterLocators:
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



