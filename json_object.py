import json

class JsonManager:

        def __init__(self, list, p_dict: dict):
                self.list = list
                self.p_dict = p_dict    
                

        def write_json(self, cd):
                self.list.append(self.p_dict)
                with open(cd, "w") as f:
                        json.dump(self.list, f, indent=4)

