@echo off
cd C:\Temp\file\AISmartFolder

REM Activate Portable Python (if needed)
set PYTHONPATH=C:\Temp\file\AISmartFolder\python-embed

REM Install Dependencies (Only the First Time)
call install_dependencies.bat

REM Start AI Smart Folder (GUI + AI Sorting)
start "" python src/ui/tray_app.py
