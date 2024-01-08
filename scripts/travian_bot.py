import selenium
from seleniumbase import Driver
import random, time, datetime, requests
from .constants import Login, Base, ResourceFieldSlots, VillageSlots, FarmsRaidsAttacks
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

        """def get_resources_for_current_village():
            wood = self.driver.find_element(Base.current_wood)
            clay = self.driver.find_element(Base.current_clay)
            iron = self.driver.find_element(Base.current_iron)
            wheat = self.driver.find_element(Base.current_wheat)

            print(f"Wood: {wood.text}, Clay: {clay.text}, Iron: {iron.text}, Wheat: {wheat.text}")"""

        try:
            self.driver.click(Base(village_number_statistic=None, village_number=village_number).village)
            #get_resources_for_current_village()
        except Exception as e:
            print("Error opening specified village!", e)

    def check_construction(self):
        free_queue = False
        construction = "#contentOuterContainer > div > div.villageInfoWrapper > div.buildingList > ul > li"
        queue = self.driver.find_elements(construction)
        if len(queue) != 1 or len(queue) != 2:
            free_queue = True
            return free_queue
        else:
            return free_queue


    #####################################################################
    #####################       GAME FUNCTIONS       ####################
    #####################################################################
        
    ########    RESOURCE FIELD UPGRADE      #######
            
    def upgrade_resource_field(self, res_field_slot):

        try:
            self.driver.click(ResourceFieldSlots(resource_field_slot=res_field_slot).resource_field)
        except Exception as e:
            print("Error getting resoruce field slot to upgrade!!!", e)
        self.driver.sleep(1)
        try:
            self.driver.click(ResourceFieldSlots.resource_field_button)
        except Exception as e:
            print("Error finding confirm button for upgrade!!!", e)


    ########    BUILDING UPGRADE      #######

    def upgrade_building(self, slot_number, tribe):

        try:
            self.driver.click(Base.village_Page)
            self.driver.sleep(1)
        except Exception as e:
            print("Error changing to village view!", e)
        try:
            self.driver.click(VillageSlots(slot_number=slot_number, tribe=tribe, new_building_number=None, build_type=None).building_slot)
            self.driver.sleep(1)
        except Exception as e:
            print("Error finding specified building slot!", e)
        try:
            self.driver.sleep(1)
            self.driver.click(VillageSlots(slot_number=slot_number, tribe=tribe, new_building_number=None, build_type=None).building_button)
        except Exception as e:
            print("Error confirming building!", e)


    ########    BUILDING CONSTRUCTION      #######

    def construct_new_building(self, slot_number, tribe, new_building_number, build_type):

        try:
            self.driver.click(Base.village_Page)
            self.driver.sleep(1)
        except Exception as e:
            print("Error changing to village view!", e)
        try:
                self.driver.click(VillageSlots(slot_number=slot_number, tribe=tribe, new_building_number=new_building_number, build_type=build_type).empty_building)
                self.driver.sleep(1)
        except Exception as e:
            print("Error finding specified empty slot for constructing new building!", e)

        try:
            if slot_number == 39:
                self.driver.click(VillageSlots.new_building_button_rallypoint)
            elif slot_number == 26:
                self.driver.click(VillageSlots.new_building_button_main_building)
            else:
                if build_type == 1:
                    self.driver.click(VillageSlots(slot_number=slot_number, tribe=tribe, new_building_number=new_building_number, build_type=build_type).new_building_button)
                elif build_type == 2:
                    self.driver.click(VillageSlots(slot_number=slot_number, tribe=tribe, new_building_number=new_building_number, build_type=build_type).change_build_types)
                    self.driver.sleep(1)
                    self.driver.click(VillageSlots(slot_number=slot_number, tribe=tribe, new_building_number=new_building_number, build_type=build_type).new_building_button)
                else:
                    self.driver.click(VillageSlots(slot_number=slot_number, tribe=tribe, new_building_number=new_building_number, build_type=build_type).change_build_types)
                    self.driver.sleep(1)
                    self.driver.click(VillageSlots(slot_number=slot_number, tribe=tribe, new_building_number=new_building_number, build_type=build_type).new_building_button)
        except Exception as e:
            print("Error confirming building!", e)

    def send_raids():
        pass

    def send_farm_lists(self):
        try:
            self.driver.click(Base.village_Page)
            self.driver.sleep(1)
        except Exception as e:
            print("Error while changing to village view!", e)
        try:
            self.driver.click(FarmsRaidsAttacks.rallypoint)
            self.driver.sleep(1)
            self.driver.click(FarmsRaidsAttacks.farm_list_tab)
            self.driver.sleep(1)
        except Exception as e:
            print("Error opening rallypoint and finding farms!", e)
        try:
            self.driver.click(FarmsRaidsAttacks.start_all_farms)
            self.driver.sleep(1)
        except Exception as e:
            print("Error while strting farms!", e)

    def do_npc(self):
        remain = self.driver.get_property('#npc > tbody > tr:nth-child(2) > td.sum > span#remain')
        print(remain)
        """try:
            self.driver.click(Base.village_Page)
            self.driver.sleep(1)
        except Exception as e:
            print("Error while changing to village view!", e)
        try:
            self.driver.click(FarmsRaidsAttacks.rallypoint)
            self.driver.sleep(1)
            self.driver.click(FarmsRaidsAttacks.farm_list_tab)
            self.driver.sleep(1)
        except Exception as e:
            print("Error opening rallypoint and finding farms!", e)"""



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
        try:
            print("Setting bot...")
            self.open_login_page()
            self.enter_login_data()
            self.change_village(1)
        except Exception as e:
            print("Error setting bot and logging in your account!", e)

        ### EXECUTING TASKS ###
        print("Starting tasks...")
        print("-"*30)
        self.driver.sleep(2)
        tasks = self.timer
        for task in tasks:
            task_name = task[1]
            task_village = task[3]
            task_tribe = task[4]
            task_building = task[5]
            task_resource = task[6]
            task_building_number = task[7]
            try:
                self.change_village(task_village)
            except Exception as e:
                print("Error with changin village", e)

            if task_name == 'upgrade_resource_field':
                try:
                    self.upgrade_resource_field(res_field_slot=task_resource)
                except:
                    print("Building resource field was not possible!")

            if task_name == 'upgrade_building':
                try:
                    self.upgrade_building(slot_number = task_building, tribe=task_tribe)
                except:
                    print("Upgrading building was not possible!")
                self.driver.sleep(1)

            if task_name == 'construct_building':
                building_infrastructure = [23, 10, 11, 18, 25, 44, 26, 17, 27, 24, 28, 39, 38, 15, 16, 45, 41, 35, 49, 34]
                building_army = [42, 19, 27, 22, 13, 20, 21, 46, 14, 29, 30, 36, 48, 47, 31, 32, 33, 43]
                building_resources = [8, 5, 6, 7, 9]

                if task_building_number in building_infrastructure:
                    build_type = 1
                elif task_building_number in building_army:
                    build_type = 3
                elif task_building_number in building_resources:
                    build_type = 5
                try:
                    self.construct_new_building(slot_number = task_building, tribe=task_tribe, new_building_number = task_building_number, build_type=build_type)
                except:
                    print("Building new building was not possible!")
                self.driver.sleep(1)
            
            if task_name == 'send_farm_lists':
                try:
                    self.send_farm_lists()
                except:
                    print("Building new building was not possible!")

        print("#"*50)
        print("All tasks finished!!!")
        print("#"*50)

        
        self.quit()



        







