from assertpy import assert_that
from selenium.webdriver.common.by import By

from infrastructure.SeleniumInfra import SeleniumInfra


class TestIFrames:
    FRAMES_URL = "http://demo.automationtesting.in/Frames.html"
    LOAD_WAIT = 7

    def setup_class(self):
        self.selenium_infra = SeleniumInfra(r"C:\\Users\\user\\Desktop\\Automation_UI\\drivers\\chromedriver.exe")

    def test_iframes(self):
        self.selenium_infra.get(self.FRAMES_URL)
        self.selenium_infra.driver.switch_to.frame('SingleFrame')
        input = self.selenium_infra.find_element_by(By.TAG_NAME, 'input')
        self.selenium_infra.write_into_element("I am inside an iFrame", element=input)
        assert_that(self.selenium_infra.get_attribute_from_element("value", element=input)).is_equal_to("I am inside an iFrame")

    def teardown_class(self):
        self.selenium_infra.close()
        self.selenium_infra.quit()
