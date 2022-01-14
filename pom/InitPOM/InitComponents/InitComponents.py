from infrastructure.SeleniumInfra import SeleniumInfra
from pom.components.CareersList.CareersList import CareersList
from pom.components.CareersList.CareersListLocators import CareersListLocators
from pom.components.CookiesBanner.CookiesBanner import CookiesBanner
from pom.components.CookiesBanner.CookiesBannerLocators import CookiesBannerLocators


class InitComponents:

    def __init__(self, selenium_infra: SeleniumInfra):
        self.careers_list = CareersList(selenium_infra, CareersListLocators())
        self.cookies_banner = CookiesBanner(selenium_infra, CookiesBannerLocators())

