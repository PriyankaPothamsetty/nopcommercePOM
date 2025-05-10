import  configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\Priyanka_Pothamsetty\PycharmProjects\nopcommerceAPP\Configurations\config.ini")


class  ReadConfig:
    @staticmethod
    def  getApplicationURL():
        url = config.get('admin_login_info','baseURL')
        return   url

    @staticmethod
    def  getUseremail():
        username = config.get('admin_login_info', 'useremail')
        return   username
    @staticmethod
    def  getPassword():
        password = config.get('admin_login_info','password')
        return   password

