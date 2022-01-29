class NavNotFoundException(Exception):
    def __init__(self, not_found_page: str):
        super().__init__(f"Page {not_found_page} was not found in the main navigator")
        self.not_found_page: str = not_found_page