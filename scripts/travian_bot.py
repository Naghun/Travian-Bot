import selenium
from seleniumbase import Driver
import random, time, datetime, requests
from .constants import Login, Base
from bs4 import BeautifulSoup
import mysql.connector


class TravianBot:
    def __init__(self, uc=True):
        self.driver = Driver(uc=uc)
        self.db_config = {
                'host' : 'localhost',
                'user' : 'root',
                'password' : 'sifraboliglava97',
                'database' : 'travian',
            }
        self.timer = None

    def quit(self):
        self.driver.quit()

    def wait(self):
        random_num = random.randint(1,4)
        self.driver.sleep(random_num)

    #####################################################################
    #########################       LOGIN       #########################
    #####################################################################


    def open_login_page(self):
        print("Opening login page!!!")
        self.driver.open(Login.login_page_link)

    def enter_login_data(self):
        print("Entering login data!!!")
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

    #####################################################################
    ################       GET BASIC INFORMATIONS       #################
    #####################################################################

    def get_villages_data(self):
        # get tribes

        # get data
        self.driver.click(Base.village_statistic)
        row = self.driver.find_elements(Base(village_number=1).village_statistic_table_rows)
        for item in row:
            print(item.text)
        
    #####################################################################
    #####################       BASIC ACTIONS       #####################
    #####################################################################
            

    def change_village(self, village_number):

        def get_resources_for_current_village():
            wood = self.driver.find_element(Base.current_wood)
            clay = self.driver.find_element(Base.current_clay)
            iron = self.driver.find_element(Base.current_iron)
            wheat = self.driver.find_element(Base.current_wheat)

            print(f"Wood: {wood.text}, Clay: {clay.text}, Iron: {iron.text}, Wheat: {wheat.text}")


        self.driver.click(Base(village_number).village)
        get_resources_for_current_village()

    def check_construction(self):
        construction = "#contentOuterContainer > div > div.villageInfoWrapper > div.buildingList > ul > li"
        queue = self.driver.find_elements(construction)
        if len(queue) == 2:
            print("Building avalible")
        else:
            print("Building under construction")


    #####################################################################
    #####################       GAME FUNCTIONS       ####################
    #####################################################################
            
    def upgrade_resource_field(self, variable):
        print(f"task variable is: {variable}")

    def upgrade_building(self):
        #def click_building_slot(driver, slot_number, tribe='egyptian'):
        selector_template = f"#villageContent > div.buildingSlot.a{slot_number}.aid{slot_number}.{tribe} > svg > path"
        selector_without_g0 = selector_template.replace('.g0', '').replace(' > svg > path', '')

        # Provjeri postoji li element bez .g0
        try:
            self.driver.click(selector_without_g0)
        except:
            self.driver.click(selector_template)

    def construct_new_building(self):
        pass

    def send_raids():
        pass

    def send_farm_lists():
        pass

    def do_npc():
        pass

    def train_troops(self):
        pass

    def upgrade_troops():
        pass


    #####################################################################
    #######################       ABOUT TASKS       #####################
    #####################################################################
        

    def get_tasks_for_current_timer(self, refresh_id):
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = f"SELECT * FROM tasks WHERE timer_id = %s;"
            cursor.execute(query, (refresh_id,))
            timer = cursor.fetchall()
            self.timer = list(timer)
            # treba jos data da se uzme da se moze koristiti

        except Exception as e:
            print(f"Error getting specified tasks from 'tasks' database, {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


    def execute_tasks(self):

        ### OPENING WINDOW AND TRAVIAN ###
        print("Setting bot...")
        self.open_login_page()
        self.enter_login_data()
        self.change_village(village_number = 1)

        ### EXECUTING TASKS ###
        print("Starting tasks...")
        print("-"*30)
        tasks = self.timer
        print("timer id is:", tasks)



        







