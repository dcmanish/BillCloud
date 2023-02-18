from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    Txt_id_cls = "//input[@placeholder='Email address']"
    textbox_password_xpath = "//input[@placeholder='Password']"
    button_login_xpath = "//button[normalize-space()='Login']"
    link_logout_xpath = "//a[normalize-space()='Logout']"
    

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, userid):
        self.driver.find_element(By.XPATH, self.Txt_id_cls).send_keys(userid)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()
