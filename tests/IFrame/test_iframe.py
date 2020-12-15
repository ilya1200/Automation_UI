from assertpy import assert_that
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By


class TestIFrames:
    FRAMES_URL = "http://demo.automationtesting.in/Frames.html"
    LOAD_WAIT = 7

    def setup_class(self):
        self.driver = webdriver.Chrome(r"C:\\Users\\user\\Desktop\\Automation_UI\\drivers\\chromedriver.exe")
        self.driver.implicitly_wait(self.LOAD_WAIT)
        self.driver.maximize_window()

    def test_iframes(self):
        self.driver.get(self.FRAMES_URL)
        self.driver.switch_to.frame('SingleFrame')
        input = self.driver.find_element_by_tag_name('input')
        input.send_keys("I am inside an iFrame")
        assert_that(input.get_attribute("value")).is_equal_to("I am inside an iFrame")

    def teardown_class(self):
        self.driver.close()
        self.driver.quit()
