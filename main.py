from pathlib import Path
import json
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware

class ShortenRequest(BaseModel):
        url: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
        return {"message": "Hello World"}

# find and designate file path for json file
json_directory = Path("urls.json")

# create json file if not already exists
if not json_directory.is_file():
        with open(json_directory, "w") as f:
                json.dump({}, f, indent = 4)
                print(f"urls.json initialised at {json_directory}")


@app.post("/shorten")
async def shorten(request: ShortenRequest):
        # read data
        with open(json_directory, "r") as f:
                python_dict = json.load(f)

        # calculate id
        if python_dict:
                new_id = max(int(k) for k in python_dict.keys()) + 1
        else:
                new_id = 1

        # encoding in base 62
        base62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        encoded_id = ""
        

        quotient = new_id
        while(quotient > 0):
                remainder = quotient % 62
                quotient = quotient // 62
                encoded_id = encoded_id + base62[remainder]
        encoded_id = encoded_id[::-1]
        encoded_id = str(encoded_id)
        print(encoded_id)

        if not encoded_id:
                encoded_id = "1"

        # store the mapping Pydantic
        python_dict[encoded_id] = request.url

        # write to json file
        with open(json_directory, "w") as f:
               json.dump(python_dict, f, indent=4)

        # return coded id and user's url
        return{"encoded_id": encoded_id, "original_url": request.url}

@app.get("/{encoded_id}")
async def redirect_to_url(encoded_id: str):
        
        # read JSON
        with open(json_directory, "r") as f:
                python_dict = json.load(f)

        if python_dict.get(encoded_id):
                return RedirectResponse(url=python_dict.get(encoded_id))
        else:
                raise HTTPException(status_code=404, detail="Short code not found")