from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from components.Register.RegisterLocators import RegisterLocators


class Register:
    def __init__(self, driver):
        self.driver = driver
        self.locators = RegisterLocators()

    @property
    def element(self) -> WebElement:
        return self.driver.find_element(*self.locators.element)

    @property
    def first_name(self) -> str:
        return self.element.find_element(*self.locators.first_name).text

    @first_name.setter
    def first_name(self, f_name: str):
        self.element.find_element(*self.locators.first_name).send_keys(f_name)

    @property
    def last_name(self) -> str:
        return self.element.find_element(*self.locators.last_name).text

    @last_name.setter
    def last_name(self, l_name: str):
        self.element.find_element(*self.locators.last_name).send_keys(l_name)

    @property
    def email_address(self) -> str:
        return self.element.find_element(*self.locators.email_address).text

    @email_address.setter
    def email_address(self, email_address: str):
        self.element.find_element(*self.locators.email_address).send_keys(email_address)

    @property
    def phone(self) -> str:
        return self.element.find_element(*self.locators.phone).text

    @phone.setter
    def phone(self, phone: str):
        self.element.find_element(*self.locators.phone).send_keys(phone)

    @property
    def gender(self) -> str:
        male = self.element.find_element(*self.locators.gender_male)
        female = self.element.find_element(*self.locators.gender_female)
        if male.is_selected():
            return male.text
        if female.is_selected():
            return male.text

    @gender.setter
    def gender(self, gender: str):
        if gender == "male":
            self.element.find_element(*self.locators.gender_male).click()
        elif gender == "female":
            self.element.find_element(*self.locators.gender_male).click()
        raise ValueError(f"Unexpected gender value:{gender}")

    @property
    def country(self) -> str:
        country_dropdown = Select(self.element.find_element(*self.locators.country_dropdown))
        selected_options = country_dropdown.all_selected_options()
        selected_option = selected_options[0].text
        return selected_option

    @country.setter
    def country(self, country: str):
        country_dropdown = Select(self.element.find_element(*self.locators.country_dropdown))
        country_dropdown.select_by_visible_text(country)
