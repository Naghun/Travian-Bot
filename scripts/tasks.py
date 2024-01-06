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

    def create_task(self, id=1, task_name_index=1, village_index=1, tribe_index=1, building_slot_index=1, resource_field_slot_index = None):
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

        names =  ['upgrade_resource_field', 'upgrade_building', 'construct_building', 'send_farms', 'do_npc', 'raid_oasis', 'train_troops']
        #               0                           1                   2                   3           4           5           6
        villages = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]    # -1 for indexes
        tribes = ['egyptian', 'roman', 'spartan', 'hun', 'gaul', 'teuton']
        #           0           1           2       3       4       5
        #                   0       1           2       3               4           5           6       7           8           9           10          11      12
        building_slots = ['main', 'trade', 'market', 'residence', 'rallypoint', 'warehouse', 'silos', 'stable', 'barracks', 'hospital', 'town hall', 'hero', 'bakery', 
                          'mill', 'res1', 'res2', 'res3', 'workshop', 'arena', 'academy', 'smithy', 'wall', 'waterwork', 'treasury', 'great',]
        #                   13      14      15      16          17      18          19      20          21      22          23          24
        resource_field_slots = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]       # -1 for indexes

        if resource_field_slot_index:
            resource_field_slot = resource_field_slots[resource_field_slot_index]
        else:
            resource_field_slot = None

        if building_slot_index:
            building_slot = building_slots[building_slot_index]
        else:
            building_slot = None

        task_data = {
            'name': names[task_name_index],
            'village': villages[village_index],
            'tribe': tribes[tribe_index],
            'timer_id': id,
            'building_slot': building_slot,
            'resource_field_slot': resource_field_slot
        }

        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = f"INSERT INTO TASKS (name, village, tribe, building_slot, resource_field_slot, timer_id) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (task_data['name'], task_data['village'], task_data['tribe'], task_data['building_slot'], task_data['resource_field_slot'], task_data['timer_id'])
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


if __name__ == '__main__':
    task = TaskCreator()
    task.create_task(id=1, task_name_index=3, village_index=3, tribe_index=3, building_slot_index=16)        #resource_slot_index
    #task.show_timers(5)


"""
    names =  ['upgrade_resource_field', 'upgrade_building', 'construct_building', 'send_farms', 'do_npc', 'raid_oasis', 'train_troops']
    #               0                           1                   2                   3           4           5           6

    villages = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]    # -1 for indexes

    tribes = ['egyptian', 'roman', 'spartan', 'hun', 'gaul', 'teuton']
    #           0           1           2       3       4       5

    #                   0       1           2       3               4           5           6       7           8           9           10          11      12
    building_slots = ['main', 'trade', 'market', 'residence', 'rallypoint', 'warehouse', 'silos', 'stable', 'barracks', 'hospital', 'town hall', 'hero', 'bakery', 
                        'mill', 'res1', 'res2', 'res3', 'workshop', 'arena', 'academy', 'smithy', 'wall', 'waterwork', 'treasury', 'great',]
    #                   13      14      15      16          17      18          19      20          21      22          23          24

    resource_field_slots = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]       # -1 for indexes

    mine_villages = [1-egypt, 2-egypt, 3-spartan, 4-teuton, 5-gaul, 6-roman, 7-hun]

"""