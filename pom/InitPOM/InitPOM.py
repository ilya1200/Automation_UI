from infrastructure.SeleniumInfra import SeleniumInfra
from pom.InitPOM.InitComponents.InitComponents import InitComponents
from pom.InitPOM.InitPages.InitPages import InitPages


class InitPOM:

    def __init__(self, selenium_infra: SeleniumInfra):
        self.components = InitComponents(selenium_infra)
        self.pages = InitPages(selenium_infra, self.components)
