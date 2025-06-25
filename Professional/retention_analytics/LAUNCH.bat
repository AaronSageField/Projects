@echo off
set "PROGRAM_DATA=%~dp0Program Data"
echo PROGRAM_DATA is set to: %PROGRAM_DATA% >> launch_log.txt
echo Checking if launcher.py exists... >> launch_log.txt
if exist "%PROGRAM_DATA%\launcher.py" (
    echo Found launcher.py >> launch_log.txt
) else (
    echo ERROR: launcher.py not found in %PROGRAM_DATA% >> launch_log.txt
    pause
    exit /b 1
)
echo Checking Python availability... >> launch_log.txt
where python >> launch_log.txt 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found in PATH >> launch_log.txt
    pause
    exit /b 1
)
echo Attempting to run launcher.py... >> launch_log.txt
python "%PROGRAM_DATA%\launcher.py" >> launch_log.txt 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Failed to run launcher.py, see above for details >> launch_log.txt
    pause
    exit /b 1
)
echo launcher.py executed successfully >> launch_log.txt
pause