import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.readproperties import  ReadConfig
from utilities.customlogger import  LogGen

from pageObjects.LoginPage  import  LoginPage
from utilities import excel_utility

class  Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    # baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    # useremail = "admin@yourstore.com"
    # password = "admin"

    logger = LogGen.loggen()

    path = r"C:\Users\Priyanka_Pothamsetty\PycharmProjects\nopcommerceAPP\TestData\login_data_driven.xlsx"
    status_list = []

    def test_login_datadriven(self,setup):
        self.logger.info("************************ Verifying Login Test data driven*************************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = excel_utility.getRowCount(self.path , "Sheet1")
        print("Now of Rows :", self.rows)

        for r in range(2, self.rows+1):
            self.user_name = excel_utility.readData(self.path , "Sheet1",r,1)
            self.password = excel_utility.readData(self.path, "Sheet1", r, 2)
            self.exp_login = excel_utility.readData(self.path, "Sheet1", r, 3)
            self.lp.setUserName(self.user_name)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp_login == "yes":
                    self.logger.info("test data is passed")
                    self.status_list.append("Pass")
                    self.lp.clickLogout()
                elif self.exp_login == "no":
                    self.logger.info("test data is failed")
                    self.status_list.append("Fail")
                    self.lp.clickLogout()
            elif  act_title != exp_title:
                if  self.exp_login == "yes":
                    self.logger.info("test data is failed")
                    self.status_list.append("Fail")
                elif  self.exp_login == "no":
                    self.logger.info("test data is passed")
                    self.status_list.append("Passed")

        print("status list is :",self.status_list)
        if "Fail" in self.status_list:
            self.logger.info("Test login data driven test is failed")
            assert  False
        else:
            self.logger.info("Test login data driven test is passed")
            assert  True


