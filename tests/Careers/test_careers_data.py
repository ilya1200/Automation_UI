from typing import List

import allure
from assertpy import assert_that

from infrastructure.SeleniumInfra import SeleniumInfra
from pom.InitPOM.InitPOM import InitPOM
from pom.components.CareerItem.CareerItem import CareerItem
from pom.components.CareersList.CareersList import CareersList
from pom.components.CookiesBanner.CookiesBanner import CookiesBanner
from pom.pages.CareersPage.CareersPage import CareersPage


class TestCareersData:

    def setup_class(self):
        self.selenium_infra: SeleniumInfra = SeleniumInfra()
        self.pom: InitPOM = InitPOM(self.selenium_infra)
        self.pages = self.pom.pages
        self.components = self.pom.components
        self.careers_page: CareersPage = self.pages.careers_page
        self.cookies_banner: CookiesBanner = self.components.cookies_banner
        self.careers_list: CareersList = self.careers_page.careers_list
        self.career_items: List[CareerItem] = list()

    @allure.title("test_careers_data")
    def test_careers_data(self):
        with allure.step(f"When user goes to Careers Israel Page"):
            self.careers_page.move_to_page()
            if self.cookies_banner.is_visible:
                self.cookies_banner.dismiss()
            self.selenium_infra.screenshot_for_allure()

        with allure.step(f"And expand to view all the positions"):
            self.careers_list.expand_all_positions()
            self.selenium_infra.screenshot_for_allure()

        with allure.step(f"When user look at each position"):
            self.career_items = self.careers_list.items
            self.selenium_infra.screenshot_for_allure()

        with allure.step(f"Then should see valid data"):
            for index, career_item in enumerate(self.career_items):
                assert_that(career_item.title, f"item at index:{index}, title is empty").is_not_empty()
                assert_that(career_item.city, f"item at index:{index} with {career_item.title}, city is empty").is_not_empty()
                assert_that(career_item.link, f"item at index:{index} with {career_item.title}, link prefix is wrong").starts_with("https://company.is.com/careers/")
            self.selenium_infra.screenshot_for_allure()

    def teardown_class(self):
        self.selenium_infra.screenshot_for_allure()
        self.selenium_infra.close()
        self.selenium_infra.quit()
