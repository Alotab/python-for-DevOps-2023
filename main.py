from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wikilogic

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Wikipedia API.  Call/Search or /wiki"}


@app.get("/search/value}")
async def search(value: str):
    """Page to searcg in wikipedia"""

    result = search_wiki(value)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
