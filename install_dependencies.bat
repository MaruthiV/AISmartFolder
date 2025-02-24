@echo off
cd C:\Temp\file\AISmartFolder

REM Use embedded Python if no global Python is found
if not exist "C:\Temp\file\AISmartFolder\python-embed\python.exe" (
    echo Installing Portable Python...
    curl -o python-embed.zip https://www.python.org/ftp/python/3.11/python-3.11-embed-amd64.zip
    tar -xf python-embed.zip -C python-embed
)

REM Install Python Dependencies
python-embed\python.exe -m pip install -r requirements.txt
