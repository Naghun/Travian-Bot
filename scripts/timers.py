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
        
    def delete_timers(self):
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = "DELETE FROM timers;"
            cursor.execute(query)
            reset_query = f"ALTER TABLE timers AUTO_INCREMENT = 1;"
            cursor.execute(reset_query)
            conn.commit()
            print("All rows deleted from 'timers' table.")

        except Exception as e:
            print(f"Error deleting rows from 'timers' table: {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        
    def make_start_timers(self):
        try:

            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = "DELETE FROM timers;"
            cursor.execute(query)
            conn.commit()

            current_time = datetime.now()
            timers_list = []

            for _ in range(24):
                interval = timedelta(seconds=random.randint(55, 65))
                new_time = current_time + interval
                timers_list.append(new_time)
                current_time = new_time

            for index, time in enumerate(timers_list):
                insert_query = f"INSERT INTO timers (time) VALUES ('{time.strftime('%Y-%m-%d %H:%M:%S')}')"
                cursor.execute(insert_query)
                print(f"Timer {index+1}: {time.strftime("%H:%M:%S - %d, %m, %Y")}")
                conn.commit()
            print("Timers inserted successfully!")

        
        except Exception as e:
            print(f"Error inserting timers in database: {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


    def get_refresh_timer(self):
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = "SELECT id, time FROM timers;"
            cursor.execute(query)
            

            # Dobijanje rezultata iz upita
            timers_list = cursor.fetchall()
            print("List taken from database!")


            if timers_list:
                first_timer_id = timers_list[0][0]
                print("first timer id is: ", first_timer_id)
                query_delete = f"DELETE FROM timers WHERE id = {first_timer_id};"
                cursor.execute(query_delete)
                print("First timer deleted!")

            if timers_list:
                last_timer = timers_list[23][1]
                print(f"Last timer id is: {last_timer}")
                interval = timedelta(seconds=random.randint(55,65))
                new_time = last_timer + interval
                print(f"New time is: {new_time}" )
                query_add = f"INSERT INTO timers (time) VALUES ('{new_time}')"
                cursor.execute(query_add)
                print("New timer added successfully!")

            conn.commit()



        except Exception as e:
            print(f"Error working with timers list from database: {e}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


    def execute_tasks(self, task, variable):
        bot = TravianBot()
        bot.execute_tasks(task, variable)

    def make_task(self, task, variable):
        if task == '':
            pass






"""
kreirati vrijeme
u tom vremenu izvrsiti tasks
izbrisati vrijeme

sve ostale prebaciti ispod

"""
