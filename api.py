from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import bcrypt

ENV_VAR = b'$2b$12$LZCJc8g4SwyqTvBVbfldjO'

app = Flask(__name__)
CORS(app)


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

def check_cred(username, password):
	cipher = hash_func(password)
	cursor.execute(f"select * from creds where username='{username}' and password='{cipher}'")
	result = cursor.fetchall()
	if result:
		print("[SUCCESS] Logged in successfully.")
		return True
	print("[ERROR] Wrong username or password.")
	return False


@app.route('/get-user/<user_id>')
def get_user(user_id):
	pswd = request.args.get("pw")
	# print(type(user_id), pswd)
	if check_cred(user_id, pswd):
		return jsonify({"login": 1}), 200
	return jsonify({"login": 0}), 200

@app.route("/create-user", methods=["POST"])
def create_user():
	data = request.get_json()
	return jsonify(data), 201

@app.route("/")
def root():
	return "WELCOME, API works great."


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")