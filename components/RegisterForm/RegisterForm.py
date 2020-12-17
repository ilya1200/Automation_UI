from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

from Component.Component import Component
from components.RegisterForm.RegisterFormLocators import RegisterFormLocators
from infrastructure.SeleniumInfra import SeleniumInfra


class RegisterForm(Component):
    def __init__(self, infra: SeleniumInfra, locators: RegisterFormLocators, **kwargs):
        super().__init__(infra, locators, **kwargs)
        self.locators = locators

    @property
    def element(self) -> WebElement:
        return self.infra.find_element_by(*self.locators.element)

    @property
    def is_visible(self) -> bool:
        return self.infra.is_element_exist(*self.locators.element)

    @property
    def first_name(self) -> str:
        return self.infra.get_attribute_from_element('value',*self.locators.first_name, from_element=self.element)

    @first_name.setter
    def first_name(self, f_name: str):
        self.infra.write_into_element(f_name, *self.locators.first_name, from_element=self.element)

    @property
    def last_name(self) -> str:
        return self.infra.get_attribute_from_element('value', *self.locators.last_name, from_element=self.element)

    @last_name.setter
    def last_name(self, l_name: str):
        self.infra.write_into_element(l_name, *self.locators.last_name, from_element=self.element)

    @property
    def email_address(self) -> str:
        return self.infra.get_attribute_from_element('value', *self.locators.email_address, from_element=self.element)

    @email_address.setter
    def email_address(self, email_address: str):
        self.infra.write_into_element(email_address, *self.locators.email_address, from_element=self.element)

    @property
    def phone(self) -> str:
        return self.infra.get_attribute_from_element('value', *self.locators.phone, from_element=self.element)

    @phone.setter
    def phone(self, phone: str):
        self.infra.write_into_element(phone, *self.locators.phone, from_element=self.element)

    @property
    def gender(self) -> str:
        male = self.infra.find_element_by(*self.locators.gender_male, from_element=self.element)
        female = self.infra.find_element_by(*self.locators.gender_female, from_element=self.element)
        if male.is_selected():
            return self.infra.get_attribute_from_element('value', element=male).lower()
        if female.is_selected():
            return self.infra.get_attribute_from_element('value', element=female).lower()

    @gender.setter
    def gender(self, gender: str):
        if gender == "male":
            self.infra.click_element(*self.locators.gender_male, from_element=self.element)
        elif gender == "female":
            self.infra.click_element(*self.locators.gender_female, from_element=self.element)
        else:
            raise ValueError(f"Unexpected gender value:{gender}")

    @property
    def country(self) -> str:
        country_dropdown = Select(self.infra.find_element_by(*self.locators.country_dropdown, from_element=self.element))
        return country_dropdown.first_selected_option.get_attribute('value')

    @country.setter
    def country(self, country: str):
        country_dropdown = Select(self.infra.find_element_by(*self.locators.country_dropdown, from_element=self.element))
        country_dropdown.select_by_visible_text(country)

    @property
    def date_of_birth(self) -> tuple:
        day_dropdown = Select(self.infra.find_element_by(*self.locators.date_of_birth_day, from_element=self.element))
        month_dropdown = Select(self.infra.find_element_by(*self.locators.date_of_birth_month, from_element=self.element))
        year_dropdown = Select(self.infra.find_element_by(*self.locators.date_of_birth_year, from_element=self.element))

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
        day_dropdown = Select(self.infra.find_element_by(*self.locators.date_of_birth_day, from_element=self.element))
        month_dropdown = Select(self.infra.find_element_by(*self.locators.date_of_birth_month, from_element=self.element))
        year_dropdown = Select(self.infra.find_element_by(*self.locators.date_of_birth_year, from_element=self.element))

        day_dropdown.select_by_visible_text(str(day))
        month_dropdown.select_by_visible_text(month)
        year_dropdown.select_by_visible_text(str(year))

    @property
    def password(self) -> str:
        return self.infra.get_attribute_from_element('value', *self.locators.password, from_element=self.element)

    @password.setter
    def password(self, password: str):
        self.infra.write_into_element(password, *self.locators.password, from_element=self.element)

    @property
    def confirm_password(self) -> str:
        return self.infra.get_attribute_from_element('value', *self.locators.confirm_password, from_element=self.element)

    @confirm_password.setter
    def confirm_password(self, confirm_password: str):
        self.infra.write_into_element(confirm_password, *self.locators.confirm_password, from_element=self.element)

    @property
    def photo(self) -> str:
        return self.infra.get_attribute_from_element('value', *self.locators.choose_file_btn, from_element=self.element)

    @photo.setter
    def photo(self, path: str):
        self.infra.write_into_element(path, *self.locators.choose_file_btn, from_element=self.element)

    def submit(self):
        self.infra.click_element(*self.locators.submit_btn, from_element=self.element)

    def refresh(self):
        self.infra.click_element(*self.locators.refresh_btn, from_element=self.element)
