from sqlalchemy.orm import Session

from app import schemas
from app.models import Question

def get_questions(db: Session, question_ids: list[int]):
    return db.query(Question).filter(Question.id.in_(question_ids)).all()

def bulk_create_questions(db: Session, questions: list[schemas.Question]):
    db_questions = db.add_all(list(map(lambda quest: Question(**quest.dict()), questions)))
    db.commit()
    return db_questions
