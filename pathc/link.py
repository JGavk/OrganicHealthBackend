import random
from bson import ObjectId
from fastapi import APIRouter, HTTPException
from typing import List
from models.question import QuestionInDB
from models.answer import UserAnswer
from database_mongo import database

router = APIRouter()


@router.get("/questions", tags=["Quiz"])
async def get_random_questions(limit: int = 5):
    pipeline = [{"$sample": {"size": limit}}]
    questions_cursor = database["questions"].aggregate(pipeline)
    questions = []
    async for q in questions_cursor:
        q["_id"] = str(q["_id"])
        questions.append(q)

    return questions


@router.post("/submit-answer", tags=["Quiz"])
async def submit_answer(answer: UserAnswer):
    question = await database["questions"].find_one({"_id": ObjectId(answer.question_id)})
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    correct_option = next((opt["text"] for opt in question["options"] if opt.get("is_correct")), None)

    if correct_option is None:
        raise HTTPException(status_code=500, detail="Pregunta sin opción correcta")
    is_correct = answer.selected_option == correct_option
    result = {
        "user_id": answer.user_id,
        "question_id": answer.question_id,
        "selected_option": answer.selected_option,
        "is_correct": is_correct,
    }
    await database["answers"].insert_one(result)

    return {"message": "Answer submitted", "is_correct": is_correct}
