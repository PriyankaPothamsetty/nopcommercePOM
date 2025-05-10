from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class  Add_New_Customer_Page:
    Customer_Xpath = "//i[@class='nav-icon far fa-user']"
    Customer_button_Xpath = "//p[text()=' Customers']"
    customer_addnew_xpath = "//i[@class='fas fa-square-plus']"
    Customers_Email_id = "Email"
    Customer_password_Id = "Password"
    Customers_FirstName_id = "FirstName"
    Customers_LatestName_id = "LastName"
    customer_Gendermale_id = "Gender_Male"
    customer_genderFemale_id = "Gender_Female"
    Customers_IsActive_Xpath = "//select[@name='SearchIsActive']//option"
    Customer_Registerdate_from_Xpath = "//input[@id='SearchRegistrationDateFrom']"
    Customer_Registerdate_To_Xpath = "//input[@id='SearchRegistrationDateTo']"
    Customer_Last_Activity_From_Xpath = "//input[@id='SearchRegistrationDateTo']"
    Customer_Last_Activity_To_Xpath = "//input[@id='SearchLastActivityTo']"
    Customer_Company_Id = "Company"
    Customer_IsTaxExempt_ID = "IsTaxExempt"
    Customer_IPAddress_Id = "SearchIpAddress"
    Customer_Newsletter_Xpath = "(//label[text()='Newsletter']//following::input[@type='search'])[1]"
    Custmoer_newsletter_selection = "//li[text()='nopCommerce admin demo store']"
    Customer_customerrole_Xpath = "(//ul[@class='select2-selection__rendered'])[2]"
    Customer_role_Guest_Xpath = "//li[text()='Guests']"
    Customer_role_Administrator_Xpath = "//li[text()='Administrators']"
    Customer_role_ForumModerators_Xpath = "//li[text()='Forum Moderators']"
    Customer_role_Registered_Xpath = "//li[text()='Registered']"
    Customer_role_Vendors_Xpath = "//li[text()='Vendors']"
    Customer_vendor_Xpath = "//select[@id='VendorId']"
    Customer_admincomments = "AdminComment"
    save_xpth = "//button[@name='save']"



    def __init__(self,driver):
        self.driver = driver

    def click_customer(self):
        self.driver.find_element(By.XPATH,self.Customer_Xpath).click()

    def click_customer_from_menu_option(self):
        self.driver.find_element(By.XPATH,self.Customer_button_Xpath).click()

    def  click_newcustomer(self):
        self.driver.find_element(By.XPATH,self.customer_addnew_xpath).click()

    def  enter_email(self,email):
        self.driver.find_element(By.ID,self.Customers_Email_id).send_keys(email)

    def  enter_password(self,password):
        self.driver.find_element(By.ID,self.Customer_password_Id).send_keys(password)

    def  enter_FirstName(self,FirstName):
        self.driver.find_element(By.ID,self.Customers_FirstName_id).send_keys(FirstName)

    def  enter_LastName(self,LastName):
        self.driver.find_element(By.ID,self.Customers_LatestName_id).send_keys(LastName)

    def  Select_Gender(self,Gender):
        if  Gender == "Male":
            self.driver.find_element(By.ID, self.customer_Gendermale_id).click()
        elif  Gender == "Female":
            self.driver.find_element(By.ID, self. customer_genderFemale_id).click()
        else:
            self.driver.find_element(By.ID, self.customer_genderFemale_id).click()


    def  enter_companyname(self,companyname):
        self.driver.find_element(By.ID,self.Customer_Company_Id).send_keys(companyname)

    def select_tax_exempt(self):
        self.driver.find_element(By.ID,self.Customer_IsTaxExempt_ID).click()
        sleep(3)

    def select_news_letter(self):
        self.driver.find_element(By.ID, self.Customer_Newsletter_Xpath).click()
        sleep(2)
        self.driver.find_element(By.ID, self.Custmoer_newsletter_selection).click()

    def sellect_customer_role(self,role):
        self.driver.find_element(By.ID, self.Customer_customerrole_Xpath).click()
        sleep(2)
        if role  == 'Guests':
            self.driver.find_element(By.XPATH, self.Customer_role_Registered_Xpath).click()
            sleep(2)
            self.driver.find_element(By.ID, self.Customer_customerrole_Xpath).click()
            self.driver.find_element(By.XPATH,self.Customer_role_Guest_Xpath).click()
        elif role == 'Administrators':
            self.driver.find_element(By.XPATH, self.Customer_role_Administrator_Xpath).click()
        elif role == 'Forum Moderators':
            self.driver.find_element(By.XPATH, self.Customer_role_ForumModerators_Xpath).click()
        elif role == 'Registered':
            pass
        else:
            self.driver.find_element(By.XPATH, self.Customer_vendor_Xpath).click()

    def select_vendor(self,vendor):
        drp_down = Select(self.driver.find_element(By.XPATH,self.Customer_vendor_Xpath))
        drp_down.select_by_visible_text(vendor)

    def enter_admin_comments(self,admincomments):
        self.driver.find_element(By.ID,self.Customer_admincomments).send_keys("admincomments")

    def click_save(self):
        self.driver.find_element(By.ID,self.save_xpth).click()












