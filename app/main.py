import requests

from typing import List
from fastapi import FastAPI, Depends
from app.models import Base
from app.database import SessionLocal, engine
from app.schemas import Question, QuestionNumRequest, QuestionList
from sqlalchemy.orm import Session
from app.crud import get_questions, bulk_create_questions

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/questions/", response_model=QuestionList)
def questions(req: QuestionNumRequest, db: Session = Depends(get_db)) -> List[Question]:
    retry: bool = True
    while retry:
        questions: QuestionList = QuestionList(list=requests.get(f"https://jservice.io/api/random?count={req.questions_num}").json())
        ids_questions: list[dict] = list(map(lambda item: item.id, questions.list))
        if not get_questions(db, ids_questions):
            bulk_create_questions(db, questions.list)
            retry = False
    return questions
