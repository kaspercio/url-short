from url import UrlManager
from json_object import JsonManager
from pathlib import Path
import json

def main():
        # find and designate file path for json file
        json_directory = Path.home() / "urls.json" 
        
        # create json file if not already exists
        if not json_directory.is_file():
                with open(json_directory, "w") as f:
                        json.dump([], f, indent = 4)
                        print(f"urls.json initialised at {json_directory}")

        # write json to python dict
        with open(json_directory, "r") as f:
                python_list = json.load(f)
        
        # test input
        n = 1876

        # instatiate url object for encoding
        url = UrlManager(n)
        url_dict = url.encode()

        # write the result to json
        jsobject = JsonManager(python_list, url_dict)
        jsobject.write_json(json_directory)
        

if __name__ == "__main__":
    main()
