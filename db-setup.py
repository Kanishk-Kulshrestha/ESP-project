import mysql.connector
import sys

if len(sys.argv) <= 2:
	usr = input("Enter your mysql username: ")
	pw = input("Enter the password: ")
else:
	usr= sys.argv[1]
	pw = sys.argv[2]

db = mysql.connector.connect(
	host = "localhost",
	user = usr,
	passwd = pw,
	)

cursor = db.cursor()

cursor.execute("create database ESP_8266_DOOR")
cursor.execute("use ESP_8266_DOOR")
cursor.execute("create table if not exists CREDS (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50) NOT NULL UNIQUE, password VARCHAR(72) NOT NULL )")

db.commit()
db.close()