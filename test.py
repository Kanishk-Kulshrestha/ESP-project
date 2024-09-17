import mysql.connector
import bcrypt
import os

os.system('cls')

# ENV_VAR = bcrypt.gensalt()
ENV_VAR = b'$2b$12$LZCJc8g4SwyqTvBVbfldjO'


db = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "razk",
	database = "USERS"
	)

cursor = db.cursor()

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

while(1):
	x = int(input("1: Login\n2: Create account\n3: Exit\n"))
	if x==1:
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
			create_acc(username, password)
		else:
			print("[ERROR] Passwords dont match.")
	elif x==3:
		os.system('cls')
		l = input("enter 1 to save changes to database: ")
		if l=='1':
			db.commit()
			print("[SAVED CHANGES]")
		else:
			print("[NOT SAVING]")
		print("Shutting down...")
		exit()
	else:
		os.system('cls')
		print("[ERROR] No such option.")

db.close()