import mysql.connector
import bcrypt
import os
from tabulate import tabulate

os.system('cls')
dirty = 0

ENV_VAR = (os.environ['HASH_SALT']).encode('utf-8')

db = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "razk",
	database = "esp_8266_door"
	)

cursor = db.cursor()

def print_db():
	cursor.execute("select * from creds")
	print(tabulate(cursor, headers = ["Sr_ID", "User_ID", "Hash"]))	
	input("\nPress Enter to continue..\n")

def hash_func(password):
	byte = password.encode("utf-8")
	return str(bcrypt.hashpw(byte, ENV_VAR))[2:-1]

def create_acc(username, password):
	cipher = hash_func(password)
	cursor.execute(f"select * from creds where username='{username}'")
	result = cursor.fetchall()
	if result:
		print("[ERROR] Username already exists.")
		return 0
	cursor.execute(f"insert into CREDS(username, password) values ('{username}', '{cipher}')")
	print("[SUCCESS] Account generated successfully.")
	return 1

def check_cred(username, password):
	cipher = hash_func(password)
	cursor.execute(f"select * from creds where username='{username}' and password='{cipher}'")
	result = cursor.fetchall()
	if result:
		print("[SUCCESS] Logged in successfully.")
		return True
	print("[ERROR] Wrong username or password.")
	return False

def del_acc(username, password):
	if check_cred(username, password):
		os.system("cls")
		cursor.execute(f"delete from creds where username='{username}'");
		print("[DELETED] successfully removed account.")

while(1):
	x = int(input("0: Show database\n1: Login\n2: Create account\n3: Remove account\n4: Exit\n\n>>> "))
	if x==0:
		os.system('cls')
		print_db()
		os.system('cls')
	elif x==1:
		os.system('cls')
		username = input("Enter username: ")
		password = input("Enter Password: ")
		os.system('cls')
		check_cred(username, password)
	elif x==2:
		os.system('cls')
		username = input("Enter username: ")
		password = input("Enter Password: ")
		re_passw = input("Re-enter Password: ")
		os.system('cls')
		if re_passw==password:
			dirty = 1
			create_acc(username, password)
		else:
			print("[ERROR] Passwords dont match.")
	elif x==3:
		os.system('cls')
		username = input("Enter username: ")
		password = input("Enter Password: ")
		os.system('cls')
		dirty = 1
		del_acc(username, password)
	elif x==4:
		os.system('cls')
		if dirty:
			l = input("There are unsaved changes\nPress 1 to save, anyother key to quit\n")
			if l=='1':
				db.commit()
				print("[SAVED CHANGES]")
			else:
				print("[NOT SAVING]")
			print("Shutting down...")
			exit()
		else:
			print("Shutting down...")
			exit()

	else:
		os.system('cls')
		print("[ERROR] No such option.")

db.close()
