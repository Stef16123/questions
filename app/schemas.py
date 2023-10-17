from pydantic import BaseModel
from datetime import datetime

class QuestionNumRequest(BaseModel):
    questions_num: int


class Question(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime


class QuestionList(BaseModel):
    list: list[Question]