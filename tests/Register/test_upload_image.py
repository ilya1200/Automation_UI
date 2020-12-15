from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from components.Register.Register import Register


class TestUploadImage:
    REGISTER_URL = "http://demo.automationtesting.in/Register.html"
    WEB_TABlE_URL = 'http://demo.automationtesting.in/WebTable.html'
    LOAD_WAIT = 7

    def setup_class(self):
        self.driver = webdriver.Chrome(r"C:\\Users\\user\\Desktop\\Automation_UI\\drivers\\chromedriver.exe")
        self.driver.implicitly_wait(self.LOAD_WAIT)
        self.driver.maximize_window()
        self.register = Register(self.driver)
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

    def test_upload_image(self):
        self.driver.get(self.REGISTER_URL)

        self.register.first_name = self.data["first_name"]
        self.register.last_name = self.data["last_name"]
        self.register.phone = self.data["phone"]
        self.register.email_address = self.data["email_address"]
        self.register.gender = self.data["gender"]
        self.register.set_date_of_birth(*self.data["date_of_birth"])
        self.register.country = self.data["country"]
        self.register.password = self.data["password"]
        self.register.confirm_password = self.data["confirm_password"]

        assert_that(self.register.first_name).is_equal_to(self.data["first_name"])
        assert_that(self.register.last_name).is_equal_to(self.data["last_name"])
        assert_that(self.register.email_address).is_equal_to(self.data["email_address"])
        assert_that(self.register.country).is_equal_to(self.data["country"])
        assert_that(self.register.gender).is_equal_to(self.data["gender"])
        assert_that(self.register.date_of_birth).is_equal_to(self.data["date_of_birth"])

        self.register.submit()
        WebDriverWait(self.driver, self.LOAD_WAIT).until(EC.url_to_be(self.WEB_TABlE_URL))
        assert_that(self.driver.current_url).is_equal_to(self.WEB_TABlE_URL)

    def teardown_class(self):
        self.driver.close()
        self.driver.quit()
