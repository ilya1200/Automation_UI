from selenium import webdriver


class TestSignUp:
    def setup_class(self):
        self.driver = webdriver.Chrome(r"C:\\Users\\user\\Desktop\\Automation_UI\\drivers\\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_sign_up(self):
        self.driver.get("http://demo.automationtesting.in/Register.html")

    def teardown_class(self):
        self.driver.close()
        self.driver.quit()
