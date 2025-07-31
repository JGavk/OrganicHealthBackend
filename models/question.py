from pydantic import BaseModel, Field
from typing import List
from models.option import Option


class Question(BaseModel):
    text: str
    options: List[Option]


class QuestionInDB(Question):
    id: str = Field(default_factory=str, alias='_id')
