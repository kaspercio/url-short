import json

class JsonManager:

        def __init__(self, list):
                self.list = list    
                

        def write_json(self, cd):
                with open(cd, "w") as f:
                        json.dump(self.list, f, indent=4)

