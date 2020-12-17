from assertpy import assert_that

from components.RegisterForm.RegisterForm import RegisterForm
from components.RegisterForm.RegisterFormLocators import RegisterFormLocators
from infrastructure.SeleniumInfra import SeleniumInfra
from pages.RegisterPage.RegisterPage import RegisterPage
from pages.RegisterPage.RegisterPageLocators import RegisterPageLocators


class TestSignUp:
    REGISTER_URL = "http://demo.automationtesting.in/Register.html"
    WEB_TABlE_URL = 'http://demo.automationtesting.in/WebTable.html'

    def setup_class(self):
        self.infra = SeleniumInfra(r"C:\\Users\\user\\Desktop\\Automation_UI\\drivers\\chromedriver.exe")
        self.register_page = RegisterPage(self.infra, RegisterPageLocators(), self.REGISTER_URL, RegisterForm(self.infra, RegisterFormLocators()))
        self.register_page.move_to_page()
        self.register = self.register_page.register_form
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

        self.register.first_name = self.data["first_name"]
        self.register.last_name = self.data["last_name"]
        self.register.phone = self.invalid_phone
        self.register.email_address = self.data["email_address"]
        self.register.gender = self.data["gender"]
        self.register.set_date_of_birth(*self.data["date_of_birth"])
        self.register.password = self.data["password"]
        self.register.confirm_password = self.data["confirm_password"]

        assert_that(self.register.first_name).is_equal_to(self.data["first_name"])
        assert_that(self.register.last_name).is_equal_to(self.data["last_name"])
        assert_that(self.register.email_address).is_equal_to(self.data["email_address"])
        assert_that(self.register.gender).is_equal_to(self.data["gender"])
        assert_that(self.register.date_of_birth).is_equal_to(self.data["date_of_birth"])

        # Submit with Invalid password
        self.register.submit()
        assert_that(self.infra.current_url).is_equal_to(self.register_page.url)
        self.register.phone = self.data["phone"]
        assert_that(self.register.phone).is_equal_to(self.data["phone"])

        # Submit without Country - mandatory field
        self.register.submit()
        assert_that(self.infra.current_url).is_equal_to(self.register_page.url)

        # Submit valid form
        self.register.country = self.data["country"]
        assert_that(self.register.country).is_equal_to(self.data["country"])
        self.register.submit()
        self.infra.wait_for_url_to_be(self.WEB_TABlE_URL)
        assert_that(self.infra.current_url).is_equal_to(self.WEB_TABlE_URL)

    def teardown_class(self):
        self.infra.close()
        self.infra.quit()
