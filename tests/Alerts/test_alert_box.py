from assertpy import assert_that
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from infrastructure.SeleniumInfra import SeleniumInfra


class TestAlerts:
    ALERTS_URL = "http://demo.automationtesting.in/Alerts.html"

    def setup_class(self):
        self.selenium_infra = SeleniumInfra(r"C:\\Users\\user\\Desktop\\Automation_UI\\drivers\\chromedriver.exe")

    def test_alerts(self):
        self.selenium_infra.get(self.ALERTS_URL)
        self.selenium_infra.find_element_by(By.XPATH, "//button[contains(text(), 'alert box')]").click()
        alert = self.selenium_infra.driver.switch_to.alert

        assert_that(alert.text) .is_equal_to("I am an alert box!")
        alert.accept()

        try:
            alert = self.selenium_infra.driver.switch_to.alert
            is_alert = True
        except NoAlertPresentException as e:
            is_alert = False
        assert_that(is_alert, "Expected the alert to disappear").is_false()

    def teardown_class(self):
        self.selenium_infra.close()
        self.selenium_infra.quit()
