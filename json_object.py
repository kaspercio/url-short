import json

class JsonManager:

        def __init__(self, p_dict: dict):
                self.p_dict = p_dict    
                

        def write_json(self, cd):
                with open(cd, "w") as f:
                        json.dump(self.p_dict, f, indent=4)

