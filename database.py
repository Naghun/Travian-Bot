import mysql.connector

db_config = {
    'host' : 'localhost',
    'user' : 'root',
    'passowrd' : 'sifraboliglava97',
    'database' : 'travian',
}

conn = mysql.connector.config(**db_config)

cursor = conn.cursor()