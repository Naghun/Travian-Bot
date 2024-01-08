import mysql.connector
from datetime import datetime, timedelta
import random, time

class TaskCreator:
    def __init__(self):
        self.db_config = {
                'host' : 'localhost',
                'user' : 'root',
                'password' : 'sifraboliglava97',
                'database' : 'travian',
            }
        self.time = time

    def show_timers(self, count=10):
        cnt = count
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = "SELECT * FROM timers;"
            cursor.execute(query)
            timers = cursor.fetchall()
            for id, time in timers:
                print(f"ID: {id}, Time: {time.strftime('%H:%M:%S')}")
                cnt-=1
                if cnt==0:
                    break

        except Exception as e:
            print(f"Error Listing timers from 'timers' database, {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def create_task(self, id=1, task_name_index=1, village_index=1, tribe_index=1, building_slot_index=1, resource_field_slot_index = 1, 
                    contract_building_numbers_index = 1):
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = f"SELECT * FROM timers WHERE ID = {id};"
            cursor.execute(query)
            timers = cursor.fetchall()
            print("time for task is: ", timers[0][1])
            print("id for task is: ", timers[0][0])

        except Exception as e:
            print(f"Error getting specified time from 'timers' database, {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        print("Timer for tasks retrieved successfully!!!")

        names =  ['upgrade_resource_field', 'upgrade_building', 'construct_building', 'send_farm_lists', 'do_npc', 'raid_oasis', 'train_troops']

        villages = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]  
        tribes = ['none', 'egyptian', 'roman', 'spartan', 'hun', 'gaul', 'teuton']
        building_slots = [0,26,30,32,35,39,31,29,34,37,38,36,33,25,23,22,21,20,19,24,28,27,40,41,42,43] # fali luka
        resource_field_slots = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        contract_building_numbers = [0, 23, 10, 11, 18, 25, 44, 26, 17, 27, 24, 28, 39, 38, 15, 16, 42, 19, 27, 22, 13, 20, 21, 46, 14, 29, 30, 8, 5, 6, 7, 9,
                                    45, 41, 36, 48, 35, 47, 31, 32, 33, 43, 49, 34]

        if resource_field_slot_index:
            resource_field_slot = resource_field_slots[resource_field_slot_index]
        else:
            resource_field_slot = None

        if building_slot_index:
            building_slot = building_slots[building_slot_index]
        else:
            building_slot = None

        if contract_building_numbers_index:
            contract_building_number = contract_building_numbers[contract_building_numbers_index]
        else:
            contract_building_number = None

        task_data = {
            'name': names[task_name_index],
            'village': villages[village_index],
            'tribe': tribes[tribe_index],
            'timer_id': id,
            'building_slot': building_slot,
            'resource_field_slot': resource_field_slot,
            'contract_building_numbers': contract_building_number
        }

        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = f"INSERT INTO TASKS (name, village, tribe, building_slot, resource_field_slot, timer_id, contract_building_numbers) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (task_data['name'], task_data['village'], task_data['tribe'], task_data['building_slot'], task_data['resource_field_slot'], task_data['timer_id'], task_data['contract_building_numbers'])
            cursor.execute(query, values)
            conn.commit()

            print(f"Task added successfully at refresh time: {timers[0][1].strftime('%H:%M:%S')}")

        except Exception as e:
            print(f"Error setting tasks at specified timer! {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def create_task2(self):
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = f"SELECT * FROM timers WHERE ID = {id};"
            cursor.execute(query)
            timers = cursor.fetchall()
            print("time for task is: ", timers[0][1])
            print("id for task is: ", timers[0][0])

        except Exception as e:
            print(f"Error getting specified time from 'timers' database, {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        print("Timer for tasks retrieved successfully!!!")



if __name__ == '__main__':
    task = TaskCreator()
    task.create_task(id=1, task_name_index=5, village_index=1, tribe_index=0,
                      building_slot_index=None, resource_field_slot_index=None, contract_building_numbers_index = None)
    #task.show_timers(5)
"""
    names =  ['upgrade_resource_field', 'upgrade_building', 'construct_building', 'send_farm_lists', 'raid_oasis', 'do_npc',]
    #               0                           1                   2                   3                  4           5

    villages = [,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]    # -1 for indexes

    tribes = ['none','egyptian', 'roman', 'spartan', 'hun', 'gaul', 'teuton']
    #           0         1         2         3        4      5         6

    #                   0       1          2       3           4           5           6           7           8         9         10          11           12      13
    building_slots = ['none',  main', 'trade', 'market', 'residence', 'rallypoint', 'warehouse', 'silos', 'stable', 'barracks', 'hospital', 'town hall', 'hero', 'bakery', 
                        'mill', 'res1', 'res2', 'res3', 'workshop', 'arena', 'academy', 'smithy', 'wall', 'waterwork', 'treasury', 'great', 'harbor']
    #                    14      15      16        17      18          19      20          21       22          23          24       25         26

    resource_field_slots = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]       # -1 for indexes

    mine_villages = ['None, 1- Ghun Town, 2- Ghun Egypt, 3-Ghun Spartan, 4-Ghun Teuton, 5- Ghun Gaul, 6- Ghun Roman, 7-Ghun Hun]

                                    1          2        3       4           5           6             7       8       9       10        11          12          13                  
    contract_building_numbers = [skloniste, skladiste, silos, ambasada, rezidencija, komandni cen, dvorac, pijaca, riznica, opstina, trgovacki, veliki sil, veliko sklad,
                14          15          16            17          18          19          20      21      22         23      24          25          26
            glavna, mjesto okupljanja, zid-egipat, kasarna, dvorac heroja, akademija, kovacnica, stala, radionica, bolnica, arena, velika kas, velika stal, 
             27     28      29         30      31       32      33          34              35      36      37      38      39          40      41     42     43
            mlin, pilana, ciglana, livnica, pekara, vodovod, pojilo, postavljac zamki, asklepion, pivara, zid-sp, zid-rim, zid-teu, zid-gal, zid-hun, luka, klesar]


"""