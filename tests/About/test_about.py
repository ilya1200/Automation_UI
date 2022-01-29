import allure

from infrastructure.SeleniumInfra import SeleniumInfra
from pom.InitPOM.InitPOM import InitPOM


class TestCareers:

    def setup_class(self):
        self.selenium_infra: SeleniumInfra = SeleniumInfra()
        self.pom: InitPOM = InitPOM(self.selenium_infra)
        self.pages = self.pom.pages
        self.components = self.pom.components

    @allure.title("test_about")
    def test_about(self):
        with allure.step(f"Given the user is on home page"):
            self.selenium_infra.screenshot_for_allure()

        with allure.step(f"When goes to the about page"):
            self.selenium_infra.screenshot_for_allure()

        with allure.step(f"Then user should see the sections"):
            self.selenium_infra.screenshot_for_allure()

    def teardown_class(self):
        self.selenium_infra.screenshot_for_allure()
        self.selenium_infra.close()
        self.selenium_infra.quit()
