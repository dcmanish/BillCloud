import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
import pageObjects
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.custom_Logger import LogGen



class Test_001_Login:


    baseURL = Readconfig.getApplicationUrl()
    userid = Readconfig.getUserid()
    password = Readconfig.getPassword()

    logger=LogGen.loggen()


    def test_homePageTitle(self, setup):

        # self.logger.info("******** Test_001_Login ******")
        # self.logger.info("******** Verifying HomePage Title ******")

        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "BillRun Cloud":
            assert True
        else:
            assert False

    def test_Login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userid)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # act_url = self.driver.title
        # #self.driver.close()
        # if act_url == "https://mcdindia.billrun.cloud":
        #     self.driver.close()
        #     assert True
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "def test_Login.png")
        #     assert False
