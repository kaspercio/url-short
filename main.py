from url import UrlManager
#from json_object import JsonManager
from pathlib import Path
import json

def main():
        # find and designate file path for json file
        json_directory = Path.home() / "urls.json" 
        
        n = 1000204
        url = UrlManager(n)
        url.encode()
        
        # create json file if not already exists
        if not json_directory.is_file():
                with open(json_directory, "w") as f:
                        json.dump([], f, indent=4)
                        print(f"urls.json initialised at {json_directory}")

        # write json to python dict
        with open(json_directory, "r") as f:
                json_dict = json.load(f)
                #manager = JsonManager(json_dict)
        print(json_dict)
        

if __name__ == "__main__":
    main()
