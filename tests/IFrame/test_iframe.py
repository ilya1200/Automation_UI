import allure
from assertpy import assert_that
from selenium.webdriver.common.by import By

from infrastructure.SeleniumInfra import SeleniumInfra, FRAMES_PAGE_URL


class TestIFrames:

    def setup_class(self):
        self.selenium_infra = SeleniumInfra()
        self.data = {
            "input": "I am inside an iFrame"
        }

    def test_iframes(self):
        with allure.step(f"When user goes Frames Page"):
            self.selenium_infra.get(FRAMES_PAGE_URL)
            self.selenium_infra.screenshot_for_allure()

        with allure.step(f"And enter {self.data['input']} into the input field"):
            self.selenium_infra.driver.switch_to.frame('SingleFrame')
            self.input = self.selenium_infra.find_element_by(By.TAG_NAME, 'input')
            self.selenium_infra.write_into_element("I am inside an iFrame", element=self.input)
            self.selenium_infra.screenshot_for_allure()

        with allure.step(f"Then input field value should be: {self.data['input']}"):
            assert_that(self.selenium_infra.get_attribute_from_element("value", element=self.input)).is_equal_to(self.data['input'])
            self.selenium_infra.screenshot_for_allure()

    def teardown_class(self):
        self.selenium_infra.screenshot_for_allure()
        self.selenium_infra.close()
        self.selenium_infra.quit()
