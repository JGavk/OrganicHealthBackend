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
    try:
        pipeline = [{"$sample": {"size": limit}}]
        questions = await database["questions"].aggregate(pipeline).to_list(length=limit)
        for q in questions:
            q["_id"] = str(q["_id"])
        return questions
    except Exception as e:
        print("Error al obtener preguntas:", e)
        raise HTTPException(status_code=500, detail="Error interno al obtener preguntas")


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


@router.get("/leaderboard", tags=["Quiz"])
async def get_leaderboard(limit: int = 10):
    try:
        pipeline = [
            {
                "$group": {
                    "_id": "$user_id",
                    "correct_answers": {
                        "$sum": {
                            "$cond": [{"$eq": ["$is_correct", True]}, 1, 0]
                        }
                    },
                    "total_answers": {"$sum": 1},
                }
            },
            {
                "$addFields": {
                    "accuracy": {
                        "$cond": [
                            {"$eq": ["$total_answers", 0]},
                            0,
                            {
                                "$multiply": [
                                    {"$divide": ["$correct_answers", "$total_answers"]},
                                    100,
                                ]
                            }
                        ]
                    }
                }
            },
            {"$sort": {"correct_answers": -1, "accuracy": -1}},
            {"$limit": limit}
        ]
        leaderboard = await database["answers"].aggregate(pipeline).to_list(length=limit)
        return leaderboard
    except Exception as e:
        print("Error obteniendo leaderboard:", e)
        raise HTTPException(status_code=500, detail="Error interno al obtener el ranking")
