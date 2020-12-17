from typing import List

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service


class SeleniumInfra:
    TIME_TO_WAIT = 20
    DRIVER_DEFAULT_PATH = r"C:\\Users\\user\\Desktop\\Automation_UI\\drivers\\chromedriver.exe"

    def __init__(self, driver_path: str = DRIVER_DEFAULT_PATH):
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.driver.implicitly_wait(self.TIME_TO_WAIT)
        self.driver.maximize_window()

    def find_element_by(self, locator_type: By, locator_value: str, from_element: WebElement = None,
                        time_to_wait: int = TIME_TO_WAIT) -> WebElement:
        if not from_element:
            from_element = self.driver
        return WebDriverWait(from_element, time_to_wait).until(
            EC.visibility_of_element_located((locator_type, locator_value)))

    def is_element_exist(self, locator_type: By = None, locator_value: str = None, element: WebElement = None,
                         from_element: WebElement = None,
                         time_to_wait: int = TIME_TO_WAIT) -> bool:
        if not element:
            try:
                element = self.find_element_by(locator_type, locator_value, from_element, time_to_wait)
            except TimeoutException as e:
                return False
        return element.is_displayed()

    def find_element_list_by(self, locator_type: By, locator_value: str, from_element: WebElement = None,
                             time_to_wait: int = TIME_TO_WAIT) -> List[WebElement]:
        if not from_element:
            from_element = self.driver
        return WebDriverWait(from_element, time_to_wait).until(
            EC.visibility_of_all_elements_located((locator_type, locator_value)))

    def click_element(self, locator_type: By = None, locator_value: str = None,
                      element: WebElement = None,
                      from_element: WebElement = None,
                      time_to_wait: int = TIME_TO_WAIT):
        if not element:
            element = self.find_element_by(locator_type, locator_value, from_element, time_to_wait)

        element.click()

    def write_into_element(self, data: str, locator_type: By = None, locator_value: str = None,
                           element: WebElement = None,
                           from_element: WebElement = None,
                           time_to_wait: int = TIME_TO_WAIT, should_clear_element: bool = True):
        if not element:
            element = self.find_element_by(locator_type, locator_value, from_element, time_to_wait)
        if should_clear_element:
            self.clear_element(element=element)
        element.send_keys(data)

    def get_attribute_from_element(self, attribute_name: str, locator_type: By = None, locator_value: str = None,
                                   element: WebElement = None,
                                   from_element: WebElement = None,
                                   time_to_wait: int = TIME_TO_WAIT) -> str:
        if not element:
            element = self.find_element_by(locator_type, locator_value, from_element, time_to_wait)
        return element.get_attribute(attribute_name)

    def get_text(self, locator_type: By = None, locator_value: str = None, element: WebElement = None,
                 from_element: WebElement = None,
                 time_to_wait: int = TIME_TO_WAIT) -> str:
        if not element:
            element = self.find_element_by(locator_type, locator_value, from_element, time_to_wait)
        return element.text

    def clear_element(self, locator_type: By = None, locator_value: str = None, element: WebElement = None,
                      from_element: WebElement = None,
                      time_to_wait: int = TIME_TO_WAIT):
        if not element:
            element = self.find_element_by(locator_type, locator_value, from_element, time_to_wait)
        element.clear()

    def screenshot_for_allure(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def get(self, url: str, time_to_wait: int = TIME_TO_WAIT):
        self.driver.get(url)
        self.driver.set_page_load_timeout(time_to_wait)

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    def wait_for_url_to_be(self, url: str, time_to_wait: int = TIME_TO_WAIT):
        WebDriverWait(self.driver, time_to_wait).until(EC.url_to_be(url))

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
