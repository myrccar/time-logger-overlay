import tkinter as tk
from screeninfo import get_monitors

class CustomOverlay:
    def __init__(self, geometry_size: tuple, hidden: bool, window_pos: tuple):
        self.root = tk.Tk()
        self.root.title("Custom Overlay")
        self.root.overrideredirect(True)  # Hide window decorations
        self.root.wm_attributes("-topmost", True) # Stay on top
        self.screen_width = get_monitors()[0].width
        self.screen_height = get_monitors()[0].height
        self.root.geometry(self.parse_geometry(geometry_size, window_pos))
        self.hidden = hidden
        if self.hidden:
            self.hide()

    def parse_geometry(self, geometry_size: tuple, window_pos: tuple):
        width, height = geometry_size
        x_pos, y_pos = window_pos
        x_pos = self.parse_percent(x_pos)
        y_pos = self.parse_percent(y_pos)
        return f"{self.parse_percent(width)}x{self.parse_percent(height)}+{x_pos}+{y_pos}"

    def parse_percent(self, value) -> int:
        if isinstance(value, str):
            if value.endswith("%w"):
                percentage = float(value[:-2]) / 100
                return int(percentage * self.screen_width)
            elif value.endswith("%h"):
                percentage = float(value[:-2]) / 100
                return int(percentage * self.screen_height)
        return value


    def show(self) -> None:
        self.root.deiconify()
        self.hidden = False

    def hide(self) -> None:
        self.root.withdraw()
        self.hidden = True

    def close(self) -> None:
        self.root.destroy()

    def run(self) -> None:
        self.root.mainloop()

    def get_window(self) -> tk.Tk:
        return self.root
    
    def show_hide(self):
        if self.hidden:
            self.show()
        else:
            self.hide()
        
