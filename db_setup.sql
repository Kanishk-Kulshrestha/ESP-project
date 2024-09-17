create database USERS;
use USERS;

create table if not exists CREDS (
	id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(72) NOT NULL 
);