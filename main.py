from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {"message": "Hello World!"}


@app.get('/hello')
def index():
    return {"message": "Hello Testing the routes !"}


@app.get("/answers")
async def getAnswer(question: str):
    return {"question": "Hello  " +   question}


