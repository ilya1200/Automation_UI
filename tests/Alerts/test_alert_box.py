from assertpy import assert_that
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
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

        try:
            alert = self.driver.switch_to.alert
            is_alert = True
        except NoAlertPresentException as e:
            is_alert = False
        assert_that(is_alert, "Expected the alert to disappear").is_false()

    def teardown_class(self):
        self.driver.close()
        self.driver.quit()
