from infrastructure.SeleniumInfra import SeleniumInfra
from pom.components.InitComponents.InitComponents import InitComponents
from pom.pages.InitPages.InitPages import InitPages


class InitPOM:

    def __init__(self, selenium_infra: SeleniumInfra):
        self.selenium_infra = selenium_infra
        self.components = InitComponents(selenium_infra)
        self.pages = InitPages(selenium_infra, self.components)
