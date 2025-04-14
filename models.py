from pydantic import BaseModel

class TriviaResponse(BaseModel):
    id : int
    question : str
    points : int

class Answer(BaseModel):
    username:str
    answer:str