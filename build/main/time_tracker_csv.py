import csv
from typing import Union
import os
from datetime import datetime

class TimeManagerCsv:
    def __init__(self,file_path:str,categories:Union[list,tuple]) -> None:
        self.categories = categories
        self.file_path = file_path

        #open/check file
        if not os.path.exists(self.file_path):
            with open(self.file_path,'w') as f:
                self.csv_writer = csv.writer(f)
                self.header = []
                for x in self.categories:
                    self.header.append(x+":")
                    self.header.append("Time")
                    self.header.append("Date")
                    self.header.append("Description")
                self.csv_writer.writerow(self.header)

    def add_time(self, category: str, minutes: int, description: str) -> None:
        if category not in self.categories:
            print(f"Category {category} not found in categories. Please use a valid category.")
            return

        # Get the current date in a formatted way (e.g., '2023-08-10')
        date = datetime.now().strftime('%Y-%m-%d')

        row = []
        for x in self.categories:
            if x == category:
                row.append(x + ":")
                row.append(minutes)
                row.append(date)
                row.append(description)
            else:
                row += ["", "", "", ""]

        with open(self.file_path, "a") as f: # Changed to 'a' to append to the file
            self.csv_writer = csv.writer(f)
            self.csv_writer.writerow(row)

        
                
    
