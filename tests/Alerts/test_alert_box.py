import allure
from assertpy import assert_that
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from infrastructure.SeleniumInfra import SeleniumInfra


class TestAlerts:
    ALERTS_URL = "http://demo.automationtesting.in/Alerts.html"

    def setup_class(self):
        self.selenium_infra = SeleniumInfra()

    @allure.title("test_alert_box")
    def test_alerts(self):
        with allure.step(f"When user goes Register Page"):
            self.selenium_infra.get(self.ALERTS_URL)
            self.selenium_infra.screenshot_for_allure()

        with allure.step(f"And click on the display alert button"):
            self.selenium_infra.find_element_by(By.XPATH, "//button[contains(text(), 'alert box')]").click()

        with allure.step(f"Then an alert should appear"):
            self.alert = self.selenium_infra.driver.switch_to.alert

        with allure.step(f"And should contain text - 'I am an alert box!' "):
            assert_that(self.alert.text) .is_equal_to("I am an alert box!")

        with allure.step(f"When user click ok"):
            self.alert.accept()
            self.selenium_infra.screenshot_for_allure()

        with allure.step(f"Then the alert should disappear"):
            try:
                self.alert = self.selenium_infra.driver.switch_to.alert
                is_alert = True
            except NoAlertPresentException as e:
                is_alert = False
            assert_that(is_alert, "Expected the alert to disappear").is_false()
            self.selenium_infra.screenshot_for_allure()

    def teardown_class(self):
        self.selenium_infra.screenshot_for_allure()
        self.selenium_infra.close()
        self.selenium_infra.quit()
