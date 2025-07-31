import os
from dotenv import load_dotenv
import motor.motor_asyncio


load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")

try:
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI, tls=True)
    database = client[MONGO_DB]
    print("Conectado a MongoDB correctamente")
except Exception as e:
    print("Error al conectar con MongoDB:", e)
    raise