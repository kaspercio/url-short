from pathlib import Path
import json

class JsonManager:

        def __init__(self, list):
                self.list = list
                # find and designate file path for json file
                self.json_directory = Path.home() / "urls.json"     
                
                # create json file if not already exists
                if not self.json_directory.is_file():
                        with open(self.json_directory, "w") as f:
                                json.dump([], f, indent=4)
                                print(f"urls.json initialised at {self.json_directory}")
        

        def write_json(self, cd):
                with open(cd, "w") as f:
                        json.dump(self.list, f, indent=4)
