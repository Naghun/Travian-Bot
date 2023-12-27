import selenium
from seleniumbase import Driver
import random, time, datetime, requests
from .constants import Login, Base
from bs4 import BeautifulSoup
import mysql.connector

class TravianBot:
    def __init__(self, uc=True):
        self.driver = Driver(uc=uc)

    def quit(self):
        self.driver.quit()


    def open_login_page(self):
        self.driver.open(Login.login_page_link)

    def enter_login_data(self):
        tries = 0
        while tries < 2:
            try:
                self.driver.send_keys(Login.login_name_field, Login.login_name)
                self.driver.send_keys(Login.login_password_field, Login.login_password)
                self.driver.click(Login.login_button_submit)
                self.driver.sleep(2)
                break
            except Exception as e:
                print(f"Error entering Login data: {e}")
                tries += 1
        else:
            print("LogIn Failed")

    def wait(self):
        random_num = random.randint(1,4)
        self.driver.sleep(random_num)


    ###############################################################################

    def get_villages_data(self):
        # get tribes

        # get data
        self.driver.click(Base.village_statistic)
        row = self.driver.find_elements(Base(village_number=1).village_statistic_table_rows)
        for item in row:
            print(item.text)
        """ tds = row.find_elements_by_tag_name("td")
            for td in tds:
                print(td.text)"""
        
    def change_village(self):

        def get_resources_for_current_village():
            wood = self.driver.find_element(Base.current_wood)
            clay = self.driver.find_element(Base.current_clay)
            iron = self.driver.find_element(Base.current_iron)
            wheat = self.driver.find_element(Base.current_wheat)

            print(f"Wood: {wood.text}, Clay: {clay.text}, Iron: {iron.text}, Wheat: {wheat.text}")


        self.driver.click(Base(village=2).village)
        get_resources_for_current_village()

    def upgrade_resource_field(self, variable):
        print(f"task variable is: {variable}")

    def upgrade_building(self):
        pass

    def execute_tasks(self, task, variable=None):
        if task == 'upgrade_resource':
            if variable:
                var = variable
                self.open_login_page()
                self.change_village()
                self.upgrade_resource_field(var)
        elif task == 'upgrade_building':
            var = variable








