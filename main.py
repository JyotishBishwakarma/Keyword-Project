from fastapi import FastAPI

import uvicorn
import json
from pagination import read_posts
from keywordSuggestion import keywordsuggest

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/search-keywords/")
def movies(search, page_num: int = 1, page_size: int = 10):
    keywordsuggest(search)
    with open("data/amazon.json",'r') as openfile:
        data = json.load(openfile)
    return read_posts(data,page_num,page_size)



