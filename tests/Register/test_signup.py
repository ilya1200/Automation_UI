from assertpy import assert_that
from selenium import webdriver

from components.Register.Register import Register


class TestSignUp:
    def setup_class(self):
        self.driver = webdriver.Chrome(r"C:\\Users\\user\\Desktop\\Automation_UI\\drivers\\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.register = Register(self.driver)
        self.data = {
            "first_name": "Nissim",
            "last_name": "David",
            "email_address": "nissim.david@Fmail.com",
            "phone": "0739118927",
            "gender": "male",
            "country": "United States",
            "date_of_birth": (12, "November", 2000)
        }

    def test_sign_up(self):
        self.driver.get("http://demo.automationtesting.in/Register.html")

        self.register.first_name = self.data["first_name"]
        self.register.last_name = self.data["last_name"]
        self.register.phone = self.data["phone"]
        self.register.email_address = self.data["email_address"]
        self.register.gender = self.data["gender"]
        self.register.country = self.data["country"]
        self.register.set_date_of_birth(*self.data["date_of_birth"])

        assert_that(self.register.first_name).is_equal_to(self.data["first_name"])
        assert_that(self.register.last_name).is_equal_to(self.data["last_name"])
        assert_that(self.register.phone).is_equal_to(self.data["phone"])
        assert_that(self.register.email_address).is_equal_to(self.data["email_address"])
        assert_that(self.register.gender).is_equal_to(self.data["gender"])
        assert_that(self.register.country).is_equal_to(self.data["country"])
        assert_that(self.register.date_of_birth).is_equal_to(self.data["date_of_birth"])

        self.register.submit()

    def teardown_class(self):
        self.driver.close()
        self.driver.quit()
