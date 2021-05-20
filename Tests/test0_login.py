import unittest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from Pages import loginPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test0_login_valid(self):

        driver = self.driver
        driver.get("https://www.facebook.com/")

        login = loginPage.LoginPage(driver)
        login.enter_username("sa****.***@gmail.com")
        login.enter_password("***")
        login.click_login()

        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Passed")

    if __name__ == '__main__':
        unittest.main()
