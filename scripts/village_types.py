import mysql.connector

class Villages:
    def __init__(self):
        self.db_config = {
        'host' : 'localhost',
        'user' : 'root',
        'password' : 'sifraboliglava97',
        'database' : 'travian',
        }

    def fill_db_manually(self, name, type, resource_type):
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = f"INSERT INTO villages (name, type) VALUES (%s, %s, %s);"
            values = (name, type, resource_type)
            cursor.execute(query, values)
            conn.commit()
            print("Village inserted successfully!")
        except Exception as e:
            print(f"Error while trying to insert village in 'villages' database: {e}")
        
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def fill_db_automatically(self):
        pass

    def delete_villages_from_db(self):
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = "DELETE FROM timers;"
            reset_query = f"ALTER TABLE timers AUTO_INCREMENT = 1;"
            cursor.execute(query)
            cursor.execute(reset_query)
            conn.commit()
            print("Villages deleted successfully!")
        except Exception as e:
            print(f"Error while trying to delete villages from 'villages' database: {e}")
        
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


if __name__ == '__main__':
    vill = Villages()
    vill.fill_db_manually(name='7. Ghun Huns', type='hun', resource_type=1)
    #vill.delete_villages_from_db()

    # resource_types = [1,1,1,15 - 6    3,3,3,9 - 1     4,4,4,6 - 3]