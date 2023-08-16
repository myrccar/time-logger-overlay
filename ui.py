from datetime import datetime
import tkinter as tk
from config_manger import ConfigManager
from stopwatch import Stopwatch

class Ui:
    def __init__(self, categories: str, overlay, add_time_func) -> None:
        self.categories = categories
        self.overlay = overlay
        self.stopwatch = Stopwatch(1)
        self.config_manger = ConfigManager("D:/vs code stuff/time logger overlay/build/config.txt")
        self.add_time_func = add_time_func
        self.init_vars()
        self.page_1()

    def init_vars(self) -> None:
        # buttons
        self.start_btn = tk.Button(self.overlay.root, text="Start", command=self.start)
        self.stop_btn = tk.Button(self.overlay.root, text="Stop", command=self.stop)
        self.pause_btn = tk.Button(self.overlay.root, text="Pause", command=self.pause_resume)
        self.done_btn = tk.Button(self.overlay.root, text="Done", command=self.done)
        self.add_btn = tk.Button(self.overlay.root,text="Add Time",command=self.page_4)
        self.done_add_btn = tk.Button(self.overlay.root,text="Done",command=self.done_add)
        # other
        self.category = tk.StringVar()
        self.category_select_dropdown = tk.OptionMenu(self.overlay.root, self.category, *self.categories)
        self.description_input = tk.Entry(self.overlay.root)
        self.info_label = tk.Label(self.overlay.root, text="", wraplength=self.overlay.parse_percent(self.config_manger.get_value("size_x")))
        self.category_label = tk.Label(text="Select Category:")
        self.time_input = tk.Entry(self.overlay.root)
        self.time_label = tk.Label(self.overlay.root,text="time(Minutes)")

    def done(self):
        self.add_time_func(int(self.stopwatch.duration / 60), self.category.get(), self.description_input.get())
        self.page_1()
    
    def done_add(self):
        self.add_time_func(int(self.time_input.get()), self.category.get(), self.description_input.get())
        self.page_1()

    def start(self):
        self.stopwatch.stop()
        self.stopwatch.reset()
        self.stopwatch.start()
        self.page_2()

    def stop(self):
        self.stopwatch.stop()
        self.page_3()

    def pause_resume(self):
        if self.stopwatch.running:
            self.stopwatch.stop()
            self.pause_btn.config(text='Resume')
        else:
            self.stopwatch.start()
            self.pause_btn.config(text='Pause')

    def page_1(self):
        self.clear_widgets()
        self.category.set(self.categories[0])
        self.category_label.config(text="Select Category:")
        self.category_label.pack()
        self.category_select_dropdown.pack()
        self.start_btn.pack()
        self.add_btn.pack()

    def page_2(self):
        self.clear_widgets()
        self.stop_btn.pack()
        self.pause_btn.pack()
        self.info_label.config(text=f"Category: {self.category.get()}")
        self.info_label.pack()

    def page_3(self):
        self.clear_widgets()
        self.stop_btn.pack_forget()
        self.pause_btn.pack_forget()
        self.info_label.config(text=f"category: {self.category.get()}, date: {datetime.now().strftime('%Y-%m-%d')}, time: {int(self.stopwatch.duration / 60)} minutes")
        self.category_label.config(text="Enter Description:")
        self.category_label.pack()
        self.description_input.pack()
        self.done_btn.pack()
        self.info_label.pack()

    def page_4(self):
        self.clear_widgets()
        self.time_label.pack()
        self.time_input.pack()
        self.category_label.config(text="Enter Description:")
        self.category_label.pack()
        self.description_input.pack()
        self.done_add_btn.pack()


    def clear_widgets(self):
        self.category_label.pack_forget()
        self.info_label.pack_forget()
        self.done_btn.pack_forget()
        self.description_input.pack_forget()
        self.description_input.delete(0, tk.END)
        self.category_select_dropdown.pack_forget()
        self.start_btn.pack_forget()
        self.stop_btn.pack_forget()
        self.add_btn.pack_forget()
        self.time_input.pack_forget()
        self.time_label.pack_forget()
        self.done_add_btn.pack_forget()