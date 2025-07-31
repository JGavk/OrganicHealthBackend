from typing import Optional

from pydantic import BaseModel


class UserAnswer(BaseModel):
    user_id: str
    question_id: str
    selected_option: str
    is_correct: Optional[bool] = None
