import allure
from assertpy import assert_that

from infrastructure.SeleniumInfra import SeleniumInfra
from pom.InitPOM.InitPOM import InitPOM
from pom.components.CareersList.CareersList import CareersList
from pom.pages.CareersPage.CareersPage import CareersPage


class TestCareers:

    def setup_class(self):
        self.selenium_infra: SeleniumInfra = SeleniumInfra()
        self.pom: InitPOM = InitPOM(self.selenium_infra)
        self.pages = self.pom.pages
        self.careers_page: CareersPage = self.pages.careers_page
        self.careers_list: CareersList = self.careers_page.careers_list
        self.careers_number: int = 0
        self.careers_number_counted: int = 0

    @allure.title("test_careers")
    def test_careers(self):
        with allure.step(f"When user goes to Careers Israel Page"):
            self.careers_page.move_to_page()
            self.selenium_infra.screenshot_for_allure()

        with allure.step(f"And view the number of Open Positions"):
            self.careers_number = self.careers_list.open_positions
            self.selenium_infra.screenshot_for_allure()

        with allure.step(f"When user count Open Position"):
            self.careers_list.expand_all_positions()
            self.careers_number_counted = self.careers_list.count_open_positions()
            self.selenium_infra.screenshot_for_allure()

        with allure.step(f"Then should see the same amount"):
            assert_that(self.careers_number).is_equal_to(self.careers_number_counted)
            self.selenium_infra.screenshot_for_allure()

    def teardown_class(self):
        self.selenium_infra.screenshot_for_allure()
        self.selenium_infra.close()
        self.selenium_infra.quit()
