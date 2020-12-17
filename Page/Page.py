from Component import Locators
from Component.Component import Component
from infrastructure.SeleniumInfra import SeleniumInfra


class Page(Component):
    def __init__(self, infra: SeleniumInfra, locators: Locators, url: str, **kwargs):
        super().__init__(infra, locators, **kwargs)
        self.url = url

    @property
    def is_visible(self) -> bool:
        return self.infra.current_url == self.url

    def move_to_page(self):
        self.infra.get(self.url)


