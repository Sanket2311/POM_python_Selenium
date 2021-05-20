from selenium.webdriver.common.by import By
from Locators.locators import Locators


class LoginPage:

    def __init__(self, driver):

        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.email_id).clear()
        self.driver.find_element(By.ID, self.email_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.NAME, self.login_name).click()
