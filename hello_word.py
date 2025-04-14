from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MessageResponse(BaseModel):
    message:str

@app.get("/")
async def helloWord() -> MessageResponse:
    return {"message": "Hello World"}

@app.get("/{name}")
async def hello_word_with_name(name:str) -> MessageResponse:
    """
    HELLO WORD ,JUST PASS YOUR NAME

    """
    return{"message":"hello "+name+"!"}