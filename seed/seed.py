import asyncio
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database_mongo import database
from models.question import Question
from models.option import Option

questions = [
    Question(
        text="¿Cuál es el síntoma más común en pacientes con estenosis aórtica severa?",
        options=[
            Option(text="Disnea de esfuerzo", is_correct=True),
            Option(text="Dolor abdominal", is_correct=False),
            Option(text="Hepatomegalia", is_correct=False),
            Option(text="Poliuria", is_correct=False),
        ]
    ),
    Question(
        text="¿Cuál es el hallazgo auscultatorio clásico en la estenosis aórtica?",
        options=[
            Option(text="Soplo sistólico en foco aórtico que irradia al cuello", is_correct=True),
            Option(text="Soplo diastólico en foco mitral", is_correct=False),
            Option(text="Soplo continuo en foco pulmonar", is_correct=False),
            Option(text="Soplo holosistólico en foco tricuspídeo", is_correct=False),
        ]
    ),
    Question(
        text="¿Cuál es la causa principal de la cardiopatía isquémica?",
        options=[
            Option(text="Hipertensión arterial", is_correct=False),
            Option(text="Tabaquismo", is_correct=False),
            Option(text="Aterosclerosis de las arterias coronarias", is_correct=True),
            Option(text="Fibrilación auricular", is_correct=False),
        ]
    ),
    Question(
        text="¿Qué medida preventiva es más eficaz para reducir el riesgo de cardiopatía isquémica?",
        options=[
            Option(text="Consumir suplementos vitamínicos", is_correct=False),
            Option(text="Mantener un estilo de vida saludable con dieta y ejercicio", is_correct=True),
            Option(text="Dormir 8 horas diarias", is_correct=False),
            Option(text="Beber café moderadamente", is_correct=False),
        ]
    ),
    Question(
        text="¿Cuál de los siguientes fármacos NO se utiliza de forma rutinaria en el manejo de la cardiopatía isquémica?",
        options=[
            Option(text="Betabloqueadores", is_correct=False),
            Option(text="Estatinas", is_correct=False),
            Option(text="Anticoagulantes", is_correct=False),
            Option(text="Antibióticos", is_correct=True),
        ]
    ),
    Question(
        text="¿Qué es el infarto agudo del miocardio?",
        options=[
            Option(text="Una infección viral del corazón", is_correct=False),
            Option(text="Un tipo de insuficiencia cardíaca congénita", is_correct=False),
            Option(text="La interrupción del flujo sanguíneo al corazón por obstrucción coronaria", is_correct=True),
            Option(text="Un latido irregular sin riesgo vital", is_correct=False),
        ]
    ),

    Question(
        text="¿Cuál es la causa más común del infarto agudo del miocardio?",
        options=[
            Option(text="Hipertensión arterial", is_correct=False),
            Option(text="Tabaquismo", is_correct=False),
            Option(text="Aterosclerosis de las arterias coronarias", is_correct=True),
            Option(text="Fibrilación auricular", is_correct=False),
        ]
    ),

    Question(
        text="¿Cuál de los siguientes es un síntoma típico del infarto agudo del miocardio?",
        options=[
            Option(text="Dolor en el pecho tipo opresivo", is_correct=True),
            Option(text="Fiebre alta", is_correct=False),
            Option(text="Pérdida de la visión", is_correct=False),
            Option(text="Dolor lumbar agudo", is_correct=False),
        ]
    ),

    Question(
        text="¿Cuál es la medida preventiva más eficaz para reducir el riesgo de infarto agudo del miocardio?",
        options=[
            Option(text="Consumir suplementos vitamínicos", is_correct=False),
            Option(text="Mantener un estilo de vida saludable con dieta y ejercicio", is_correct=True),
            Option(text="Dormir 8 horas diarias", is_correct=False),
            Option(text="Beber café moderadamente", is_correct=False),
        ]
    ),

    Question(
        text="¿Cuál de los siguientes fármacos NO se utiliza de forma rutinaria en el manejo del infarto agudo del miocardio?",
        options=[
            Option(text="Betabloqueadores", is_correct=False),
            Option(text="Estatinas", is_correct=False),
            Option(text="Anticoagulantes", is_correct=False),
            Option(text="Antibióticos", is_correct=True),
        ]
    ),
]

async def seed_data():
    for q in questions:
        exists = await database["questions"].find_one({"text": q.text})
        if not exists:
            await database["questions"].insert_one(q.dict())
    print("Preguntas insertadas sin duplicados")

if __name__ == "__main__":
    asyncio.run(seed_data())
