import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.readproperties import  ReadConfig
from utilities.customlogger import  LogGen

from pageObjects.LoginPage  import  LoginPage

class  Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    # baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    # useremail = "admin@yourstore.com"
    # password = "admin"

    logger = LogGen.loggen()

    def  test_homePageTitle(self,setup):
        self.logger.info("************** Test_001_Login ****************")
        self.logger.info("************************ Verifying Home Page Title *************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if  act_title == "nopCommerce demo store. Login":
            assert  True
        else:
            self.driver.save_screenshot("C:\\Users\\Priyanka_Pothamsetty\\PycharmProjects\\nopcommerceAPP\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            self.logger.info("************** Test_001_Login ****************")
            self.logger.info("************************ Home Page Title is failed *************************")
            assert False


    def test_login(self,setup):
        self.logger.info("************************ Verifying Login Test *************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if  act_title == "Dashboard / nopCommerce administration":
            assert   True
            self.logger.info("************************ Login Test is passed *************************")
            self.driver.close()
        else:
            self.driver.save_screenshot("C:\\Users\\Priyanka_Pothamsetty\\PycharmProjects\\nopcommerceAPP\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            self.logger.info("************************ Login Test is Failed   *************************")
            assert False
