from pydantic import BaseModel, Field


class Option(BaseModel):
    text: str
    is_correct: bool

