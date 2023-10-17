import requests

from typing import List
from fastapi import Depends, APIRouter
from app.schemas import Question, QuestionNumRequest, QuestionList
from sqlalchemy.orm import Session
from app.questions_repository import get_questions, bulk_create_questions
from app.database import get_db
from app.constants import QUESTION_RANDOM_COUNT_URL


router = APIRouter()



@router.post("/questions/", response_model=QuestionList)
def questions(req: QuestionNumRequest, db: Session = Depends(get_db)) -> List[Question]:
    retry: bool = True
    while retry:
        
        questions: QuestionList = QuestionList(list=requests.get(f"{QUESTION_RANDOM_COUNT_URL}{req.questions_num}").json())
        ids_questions: list[dict] = list(map(lambda item: item.id, questions.list))
        if not get_questions(db, ids_questions):
            bulk_create_questions(db, questions.list)
            retry = False
    return questions
