@echo off

REM Name of the program
set PROGRAM_NAME=AFE Learning log Timmer

REM Path to the program's executable
set EXECUTABLE_PATH="%~dp0afe_log_do_not_open.exe"

REM Add the program to the user's startup folder
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v %PROGRAM_NAME% /t REG_SZ /d %EXECUTABLE_PATH% /f

REM Relative path to the program's executable
set EXECUTABLE_PATH=%~dp0afe_log_do_not_open.exe

REM Start the program
start "" "%EXECUTABLE_PATH%"

echo %PROGRAM_NAME% has been installed and will run on startup!
