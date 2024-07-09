import mysql.connector
import os

MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=MYSQL_ROOT_PASSWORD
)

#print(database)

#cursor object
cursorObject= database.cursor()

#create db
cursorObject.execute("CREATE DATABASE crm")

print("All Done!")

