from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAlerts:
    ALERTS_URL = "http://demo.automationtesting.in/Alerts.html"
    LOAD_WAIT = 7

    def setup_class(self):
        self.driver = webdriver.Chrome(r"C:\\Users\\user\\Desktop\\Automation_UI\\drivers\\chromedriver.exe")
        self.driver.implicitly_wait(self.LOAD_WAIT)
        self.driver.maximize_window()

    def test_alerts(self):
        self.driver.get(self.ALERTS_URL)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'alert box')]").click()
        alert = self.driver.switch_to.alert

        assert_that(alert.text) .is_equal_to("I am an alert box!")
        alert.accept()

    def teardown_class(self):
        self.driver.close()
        self.driver.quit()
