from fastapi import FastAPI, Response, status
from fastapi.params import Body
from database import Chapter_wise
from model import ChapterwiseBase, FullTestAPI
from random import randrange

app = FastAPI()

def findquestion(subject, chapter_name, set_no):
    for i in Chapter_wise:
        if i['subject'] == subject:
            for j in i:
                if j['chapter'] == chapter:
                    for k in j:
                        if k['set_no'] == set_no:
                            return k


@app.get("/chapterwise")
def get_posts():
    return {"data": Chapter_wise}


@app.get("/chapterwise/{subject}/{chapter_name}/{set_no}")
def get_questions():
    return findquestion(subject, chapter_name, set_no)