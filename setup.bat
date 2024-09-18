@echo off

curl -L "https://github.com/Kanishk-Kulshrestha/ESP-project/archive/refs/heads/master.zip" -o project.zip
if %errorlevel% equ 0 (
	echo Repository downloaded successfully.
) else (
	echo Failed to download the repository.
	exit /b 1
)

powershell -Command "Expand-Archive -Path project.zip"

if %errorlevel% equ 0 (
	echo Repository extracted successfully.
) else (
	echo Failed to extract.
	exit /b 1
)

del project.zip

pip install "mysql-connector-python"

if %errorlevel% equ 0 (
	echo Library downloaded successfully.
) else (
	echo Unable to download library.
	exit /b 1
)

pip install flask

if %errorlevel% equ 0 (
	echo Library downloaded successfully.
) else (
	echo Unable to download library.
	exit /b 1
)

pip install flask-cors

if %errorlevel% equ 0 (
	echo Library downloaded successfully.
) else (
	echo Unable to download library.
	exit /b 1
)

pip install bcrypt

if %errorlevel% equ 0 (
	echo Library downloaded successfully.
) else (
	echo Unable to download library.
	exit /b 1
)

cd project
cd ESP-project-main

setx HASH_SALT $2b$12$LZCJc8g4SwyqTvBVbfldjO

python db-setup.py
del db-setup.py
python logger.py
del setup.bat
