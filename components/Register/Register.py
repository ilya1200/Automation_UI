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
        return self.element.find_element(*self.locators.first_name).get_attribute('value')

    @first_name.setter
    def first_name(self, f_name: str):
        self.element.find_element(*self.locators.first_name).send_keys(f_name)

    @property
    def last_name(self) -> str:
        return self.element.find_element(*self.locators.last_name).get_attribute('value')

    @last_name.setter
    def last_name(self, l_name: str):
        self.element.find_element(*self.locators.last_name).send_keys(l_name)

    @property
    def email_address(self) -> str:
        return self.element.find_element(*self.locators.email_address).get_attribute('value')

    @email_address.setter
    def email_address(self, email_address: str):
        self.element.find_element(*self.locators.email_address).send_keys(email_address)

    @property
    def phone(self) -> str:
        return self.element.find_element(*self.locators.phone).get_attribute('value')

    @phone.setter
    def phone(self, phone: str):
        self.element.find_element(*self.locators.phone).clear()
        self.element.find_element(*self.locators.phone).send_keys(phone)

    @property
    def gender(self) -> str:
        male = self.element.find_element(*self.locators.gender_male)
        female = self.element.find_element(*self.locators.gender_female)
        if male.is_selected():
            return male.get_attribute('value').lower()
        if female.is_selected():
            return female.get_attribute('value').lower()

    @gender.setter
    def gender(self, gender: str):
        if gender == "male":
            self.element.find_element(*self.locators.gender_male).click()
        elif gender == "female":
            self.element.find_element(*self.locators.gender_female).click()
        else:
            raise ValueError(f"Unexpected gender value:{gender}")

    @property
    def country(self) -> str:
        country_dropdown = Select(self.element.find_element(*self.locators.country_dropdown))
        return country_dropdown.first_selected_option.get_attribute('value')

    @country.setter
    def country(self, country: str):
        country_dropdown = Select(self.element.find_element(*self.locators.country_dropdown))
        country_dropdown.select_by_visible_text(country)

    @property
    def date_of_birth(self) -> tuple:
        day_dropdown = Select(self.element.find_element(*self.locators.date_of_birth_day))
        month_dropdown = Select(self.element.find_element(*self.locators.date_of_birth_month))
        year_dropdown = Select(self.element.find_element(*self.locators.date_of_birth_year))

        selected_day = int(day_dropdown.first_selected_option.get_attribute('value'))
        selected_month = month_dropdown.first_selected_option.get_attribute('value')
        selected_year = int(year_dropdown.first_selected_option.get_attribute('value'))
        return selected_day, selected_month, selected_year

    def set_date_of_birth(self, day: int, month: str, year: int):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        if day not in range(1, 32):
            raise ValueError(f"Expected day to be between 1 to 31, but actual {day}")
        if month not in months:
            raise ValueError(f"Unexpected month: {month}, should be in {months}")
        day_dropdown = Select(self.element.find_element(*self.locators.date_of_birth_day))
        month_dropdown = Select(self.element.find_element(*self.locators.date_of_birth_month))
        year_dropdown = Select(self.element.find_element(*self.locators.date_of_birth_year))

        day_dropdown.select_by_visible_text(str(day))
        month_dropdown.select_by_visible_text(month)
        year_dropdown.select_by_visible_text(str(year))

    @property
    def password(self) -> str:
        return self.element.find_element(*self.locators.password).get_attribute('value')

    @password.setter
    def password(self, password: str):
        self.element.find_element(*self.locators.password).send_keys(password)

    @property
    def confirm_password(self) -> str:
        return self.element.find_element(*self.locators.confirm_password).get_attribute('value')

    @confirm_password.setter
    def confirm_password(self, confirm_password: str):
        self.element.find_element(*self.locators.confirm_password).send_keys(confirm_password)

    def photo(self, path: str):
        choose_file = self.driver.find_element(*self.locators.choose_file_btn)
        choose_file.send_keys(path)

    def submit(self):
        self.element.find_element(*self.locators.submit_btn).click()

    def refresh(self):
        self.element.find_element(*self.locators.refresh_btn).click()
