import keyboard
import tkinter as tk
from config_manger import ConfigManager
from overlay import CustomOverlay
from time_tracker_csv import TimeManagerCsv
from ui import Ui
import os

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
overlay.run()
