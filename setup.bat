@echo off

set repo = "https://github.com/Kanishk-Kulshrestha/ESP-project"

set zip = repo.zip

curl -L "%repo%/archive/refs/heads/main.zip" -o %zip%

if %errorlevel% equ 0 (
	echo Repository downloaded successfully.
) else (
	echo Failed to download the repository.
	exit /b 1
)

powershell -Command "Expand-Archive -Path %zip%"

if %errorlevel% equ 0 (
	echo Repository extracted successfully.
) else (
	echo Failed to extract.
	exit /b 1
)

del %zip%

echo Done.
pause