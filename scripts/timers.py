import mysql.connector
from datetime import datetime, timedelta
import random, time
from .travian_bot import TravianBot


class TimeManager:
    def __init__(self):
        self.db_config = {
                'host' : 'localhost',
                'user' : 'root',
                'password' : 'sifraboliglava97',
                'database' : 'travian',
            }
        self.time = time

    #####################################################################
    #################    DELETING OLD TIMERS AND TASKS  #################
    ####################    ADDING NEW TIMERS IN DB   ###################
    #####################################################################
     
    def make_start_timers(self):

        ### REMOVING TIMERS AND TASKS DB ###

        print("Removing old Times from Timers db!")
        print("-"*30)
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = "DELETE FROM timers;"
            reset_query = f"ALTER TABLE timers AUTO_INCREMENT = 1;"
            cursor.execute(query)
            cursor.execute(reset_query)
            conn.commit()

        except Exception as e:
            print(f"Error deleting rows from 'timers' table: {e}")
        
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        print("Removing old Tasks from Tasks db!")
        print("-"*30)
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = "DELETE FROM tasks;"
            reset_query = f"ALTER TABLE tasks AUTO_INCREMENT = 1;"
            cursor.execute(query)
            cursor.execute(reset_query)
            conn.commit()

        except Exception as e:
            print(f"Error deleting rows from 'tasks' table: {e}")
        
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        ### CREATING NEW TIMERS IN DB ###
                
        print("Setting new Timers in db!")
        print("-"*30)

        try:

            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            current_time = datetime.now()
            timers_list = []

            for _ in range(96):
                interval = timedelta(minutes=random.randint(1, 2))
                new_time = current_time + interval
                timers_list.append(new_time)
                current_time = new_time

            for index, time in enumerate(timers_list):
                insert_query = f"INSERT INTO timers (time) VALUES ('{time.strftime('%Y-%m-%d %H:%M:%S')}')"
                cursor.execute(insert_query)
                conn.commit()
            print("Timers inserted successfully!")

        
        except Exception as e:
            print(f"Error inserting timers in database: {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    #####################################################################
    #########################    FIRST REFRESH   ########################
    #####################################################################

    def set_first_refresh(self):
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = "SELECT id, time FROM timers;"
            cursor.execute(query)
            
            timers_list = cursor.fetchall()

            if timers_list:
                refresh_time = timers_list[0][1]
                refresh_time.strftime('%Y-%m-%d %H:%M:%S')
                refresh_id = timers_list[0][0]

                with open("scripts/refresh.py", 'w') as file:
                    file.write("import datetime\n")
                    file.write(f"refresh_time = {repr(refresh_time)}\n")
                    file.write(f"refresh_id = {repr(refresh_id)}")

        except Exception as e:
            print(f"Error setting first refresh, {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    #####################################################################
    ###############      DELETE FIRST, ADD LAST      ####################
    #####################################################################

    def delete_first_timer_add_last_timer(self):
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = "SELECT id, time FROM timers;"
            cursor.execute(query)
            timers_list = cursor.fetchall()

            first_timer_id = timers_list[0][0]
            query_delete = f"DELETE FROM timers WHERE id = {first_timer_id};"
            cursor.execute(query_delete)

            if timers_list:
                last_timer_id = timers_list[-1][0]
                last_timer_time = timers_list[-1][1]
                print(f"Last timer id is: {last_timer_id}, time is: {last_timer_time}")
                interval = timedelta(minutes=random.randint(1,2))
                new_time = last_timer_time + interval
                query_add = f"INSERT INTO timers (time) VALUES ('{new_time}')"
                cursor.execute(query_add)

            conn.commit()
        except Exception as e:
            print(f"Error working with timers list from database: {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


    #####################################################################
    #################      OTHER REFRESH TIMERS      ####################
    #####################################################################

    def get_refresh_timer(self):
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = "SELECT id, time FROM timers;"
            cursor.execute(query)
            
            timers_list = cursor.fetchall()

            if timers_list:
                refresh_id = timers_list[1][0]
                refresh_time = timers_list[1][1]
                refresh_time.strftime('%Y-%m-%d %H:%M:%S')

                with open("scripts/refresh.py", 'w') as file:
                    file.write("import datetime\n")
                    file.write(f"refresh_time = {repr(refresh_time)}\n")
                    file.write(f"refresh_id = {repr(refresh_id)}")



        except Exception as e:
            print(f"Error working with timers list from database: {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()