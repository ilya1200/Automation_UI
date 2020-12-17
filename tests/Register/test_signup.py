from assertpy import assert_that

from infrastructure.SeleniumInfra import SeleniumInfra
from pom.InitPOM.InitPOM import InitPOM


class TestSignUp:

    def setup_class(self):
        self.pom = InitPOM(SeleniumInfra())
        self.pages = self.pom.pages

        self.register_page = self.pages.register_page
        self.register_form = self.register_page.register_form
        self.web_table_page = self.pages.web_table_page
        self.register_page.move_to_page()

        self.data = {
            "first_name": "Nissim",
            "last_name": "David",
            "email_address": "nissim.david@Fmail.com",
            "phone": "0739118927",
            "gender": "male",
            "country": "United States",
            "date_of_birth": (12, "November", 2000),
            "password": "Aa102030",
            "confirm_password": "Aa102030"
        }
        self.invalid_phone = 10203040506070

    def test_sign_up(self):
        self.register_form.first_name = self.data["first_name"]
        self.register_form.last_name = self.data["last_name"]
        self.register_form.phone = self.invalid_phone
        self.register_form.email_address = self.data["email_address"]
        self.register_form.gender = self.data["gender"]
        self.register_form.set_date_of_birth(*self.data["date_of_birth"])
        self.register_form.password = self.data["password"]
        self.register_form.confirm_password = self.data["confirm_password"]

        assert_that(self.register_form.first_name).is_equal_to(self.data["first_name"])
        assert_that(self.register_form.last_name).is_equal_to(self.data["last_name"])
        assert_that(self.register_form.email_address).is_equal_to(self.data["email_address"])
        assert_that(self.register_form.gender).is_equal_to(self.data["gender"])
        assert_that(self.register_form.date_of_birth).is_equal_to(self.data["date_of_birth"])

        # Submit with Invalid password
        self.register_form.submit()
        assert_that(self.register_page.is_visible).is_true()
        self.register_form.phone = self.data["phone"]
        assert_that(self.register_form.phone).is_equal_to(self.data["phone"])

        # Submit without Country - mandatory field
        self.register_form.submit()
        assert_that(self.register_page.is_visible).is_true()

        # Submit valid form
        self.register_form.country = self.data["country"]
        assert_that(self.register_form.country).is_equal_to(self.data["country"])
        self.register_form.submit()
        assert_that(self.web_table_page.is_visible).is_true()

    def teardown_class(self):
        self.pom.selenium_infra.close()
        self.pom.selenium_infra.quit()
