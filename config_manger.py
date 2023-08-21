import re

class ConfigManager:
    def __init__(self, file):
        self.file = file
        self.config_dict = {}
        with open(self.file, "r") as f:
            lines = f.read().strip().split("\n")
            for line in lines:
                key, value = line.split("$")
                self.config_dict[key] = self._parse_value(value)

    def _parse_value(self, value):
        if value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        elif re.match("\d+\.\d+",str(value)) != None:
             return float(value)
        elif value.isdigit():
            return int(value)
        elif re.match("^\[.*\]$",value) != None:
            return value.replace("[","").replace("]","").replace('"',"").split(",")
        else:
            return value

    def get_value(self, key):
        return self.config_dict.get(key, None)
