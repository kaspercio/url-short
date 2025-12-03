# URL shortener
This is a URL shortener API made with FastAPI in Python. <br> The app takes the user's URL and generates an ID which is used
to create the shortened URL.

**Demo:** https://url-short-4bq6.onrender.com

## Features
- Stores user URL's in a JSON object.
- Generates sequential IDs' that are Base62 encoded.
- Redirects user to website given an ID associated with a stored URL.
- RESTful API design.

## Technologies used
- Python 3.10.12
- FastApi 0.123.5

## Local Installation
1. **Clone the repository:**
```bash
git clone https://github.com/kaspercio/url-short.git
cd url-short
```

2. **Create and activate virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the server:**
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## API endpoints
### Shorten a URL
**Endpoint:** `POST /shorten`

**Request body:**
```json
{
  "url": "https://www.example.com"
}
```

**Response:**
```json
{
  "encoded_id": "1",
  "original_url": "https://www.example.com"
}
```

**Example with curl:**
```bash
curl -X POST "http://127.0.0.1:8000/shorten" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://google.com"}'
```

### Redirect to Original URL
**Endpoint:** `GET /{encoded_id}`

Visit `http://127.0.0.1:8000/1` in your browser and you'll be redirected to the original URL.

## Future Improvements
- Frontend for using API
- Remote data storage
- URL Validation

## License
MIT
