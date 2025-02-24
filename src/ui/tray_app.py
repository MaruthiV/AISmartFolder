import pystray
from pystray import MenuItem as item, Icon
from PIL import Image
import subprocess
import os

# Path to smart_folder.py (no renaming needed!)
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "..", "smart_folder.py")

# Load Tray Icon
ICON_PATH = "icon.png"  # Ensure you have an icon file
icon_image = Image.open(ICON_PATH)

def start_ai_folder():
    subprocess.Popen(["python", SCRIPT_PATH], creationflags=subprocess.CREATE_NO_WINDOW)

def stop_ai_folder(icon, item):
    os.system("taskkill /f /im python.exe")  # Kills the AI sorting process
    icon.stop()

# Define Tray Menu
menu = (
    item("Start AI Sorting", start_ai_folder),
    item("Stop AI Sorting", stop_ai_folder),
    item("Quit", stop_ai_folder)
)

icon = Icon("AI Smart Folder", icon_image, menu=menu)
icon.run()
