import allure
from assertpy import assert_that

from infrastructure.SeleniumInfra import SeleniumInfra
from pom.InitPOM.InitPOM import InitPOM
from pom.components.Navigator.Navigator import Navigator
from pom.pages.AboutPage.AboutPage import AboutPage
from pom.pages.HomePage.HomePage import HomePage


class TestCareers:

    def setup_class(self):
        self.selenium_infra: SeleniumInfra = SeleniumInfra()
        self.pom: InitPOM = InitPOM(self.selenium_infra)
        self.pages = self.pom.pages
        self.home_page: HomePage = self.pages.home_page
        self.about_page: AboutPage = self.pages.about_page
        self.navigator: Navigator = self.home_page.navigator

    @allure.title("test_about")
    def test_about(self):
        with allure.step(f"Given the user is on home page"):
            self.home_page.move_to_page()
            assert_that(self.home_page.url).is_equal_to(self.selenium_infra.current_url)
            self.selenium_infra.screenshot_for_allure()

        with allure.step(f"When goes to the about page"):
            self.navigator.navigate_to("about us")
            assert_that(self.about_page.url).is_equal_to(self.selenium_infra.current_url)
            self.selenium_infra.screenshot_for_allure()

        with allure.step(f"Then user should see the sections"):
            self.selenium_infra.screenshot_for_allure()

    def teardown_class(self):
        self.selenium_infra.screenshot_for_allure()
        self.selenium_infra.close()
        self.selenium_infra.quit()
