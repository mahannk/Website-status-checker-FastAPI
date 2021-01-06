from fastapi import FastAPI, Response, status
from pydantic import BaseModel 
from typing import List 
import markdown
from services import checking_url
import os

app = FastAPI()


class Input_Data(BaseModel):
    URL : str = "https://www.google.com"



@app.get("/")
def read_me():
    with open(os.path.dirname(app.root_path) + '/readme.md', 'r') as f:
        content = f.read()
        
        return markdown.markdown(content)


@app.post('/url_checker/')
def status_checker(input_data: List[Input_Data], response: Response):

    urls = [url.URL for url in input_data]
    results = checking_url.run(urls)
    
    return {'message' : 'success', 'data' : results}

