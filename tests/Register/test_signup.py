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
            "phone": "0739118927",
            "gender": "male",
            "country": "United States"
        }

    def test_sign_up(self):
        self.driver.get("http://demo.automationtesting.in/Register.html")

        self.register.first_name = self.data["first_name"]
        self.register.last_name = self.data["last_name"]
        self.register.phone = self.data["phone"]
        self.register.gender = self.data["gender"]
        self.register.country = self.data["country"]

        assert_that(self.register.first_name).is_equal_to(self.data["first_name"])
        assert_that(self.register.last_name).is_equal_to(self.data["last_name"])
        assert_that(self.register.phone).is_equal_to(self.data["phone"])
        assert_that(self.register.gender).is_equal_to(self.data["gender"])
        assert_that(self.register.country).is_equal_to(self.data["country"])

    def teardown_class(self):
        self.driver.close()
        self.driver.quit()
