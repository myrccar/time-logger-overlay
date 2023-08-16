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
        # elif "." in value:
        #     return float(value)
        elif value.isdigit():
            return int(value)
        elif value[0] == "[" and value[len(value)-1] == "]":
            return value.replace("[","").replace("]","").replace('"',"").split(",")
        else:
            return value

    def get_value(self, key):
        return self.config_dict.get(key, None)
