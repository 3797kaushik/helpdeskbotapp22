
import pyowm
from config.config_reader import ConfigReader

class employeeInformation():
    def __init__(self):
        self.config_reader = ConfigReader()
        self.configuration = self.config_reader.read_config()

    def get_employee_info(self,name):
        self.name=name
        print('==============',type(name))
        id = 1234
        self.bot_says = "Entity is : " + str(name )
        return self.bot_says