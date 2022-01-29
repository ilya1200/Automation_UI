from infrastructure.SeleniumInfra import SeleniumInfra
from pom.components.Navigator.Navigator import Navigator
from pom.components.Navigator.NavigatorLocators import NavigatorLocators


class InitComponents:

    def __init__(self, selenium_infra: SeleniumInfra):
        self.navigator = Navigator(selenium_infra, NavigatorLocators())
