import keyboard
import tkinter as tk
from config_manger import ConfigManager
from overlay import CustomOverlay
from time_tracker_csv import TimeManagerCsv
from ui import Ui
import os
import pystray
from PIL import Image, ImageDraw
import threading
import queue



config_manager = ConfigManager("D:/vs code stuff/time logger overlay/build/config.txt")
overlay = CustomOverlay(
    geometry_size=(
        config_manager.get_value("size_x"),
        config_manager.get_value("size_y")  # Assuming there's a size_y in the config
    ),
    hidden=config_manager.get_value("hidden_startup"),
    window_pos=(
        config_manager.get_value("pos_x"),
        config_manager.get_value("pos_y")
    )
)

window = overlay.get_window()
time_tracker_csv = TimeManagerCsv(config_manager.get_value("csv_path"), config_manager.get_value("categories"))

def add_time(time, category, description):
    time_tracker_csv.add_time(category, time, description)

ui = Ui(config_manager.get_value("categories"), overlay, add_time)
keyboard.add_hotkey(config_manager.get_value("hotkey"), overlay.show_hide)
#system tray

# ...

def start_icon():
    icon.run()

def on_select(icon, item):
    icon.stop()  # This will stop the icon and let the rest of the program continue

icon_image = Image.open(r"icon.png")
menu = (pystray.MenuItem('Show/Hide', on_select),)
icon = pystray.Icon("AFE Time Log", icon_image, "AFE Time Log", menu=menu)

icon_thread = threading.Thread(target=start_icon)
icon_thread.start()

# Pause the main thread until the icon is stopped
icon_thread.join()

# Now the icon is stopped, so we can toggle the overlay
overlay.show_hide()
