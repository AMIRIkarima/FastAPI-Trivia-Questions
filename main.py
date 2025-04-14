from fastapi import FastAPI
import  json
from models import TriviaResponse,Answer
from typing import List


app = FastAPI()
scoreboard={}

#fetch data from json

with open("questions.json") as f:
    questions =json.load(f)


#print(questions[:2])


@app.get("/trivia")
def get_trivia()-> List[TriviaResponse]:
    trivia_list =[]

    for ques in questions :
        trivia = TriviaResponse(
            id = ques["id"],
            question = ques["question"],
            points = ques["points"]
        )
        
        trivia_list.append(trivia)
    return trivia_list


@app.post("/trivia/answer/{question_id}")
def answer_question(question_id :int ,answer :Answer):
    question = None 

    for q in questions :
        if q["id"] == question_id:
            question = q
            break

    if answer.answer.lower().strip() == question["answer"].lower().strip():
        is_correct=True
        points = questions["points"]
        scoreboard[answer.username] =scoreboard.get(answer.username,0)+points

    else:
        is_correct=False
        scoreboard.setdefault(answer.username,0)


    return{
        "correct" : is_correct,
        "score" :scoreboard
    }