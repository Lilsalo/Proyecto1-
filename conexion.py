import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Cargar variables del archivo .env
load_dotenv()

# Obtener URI desde el entorno
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["escuela"]

alumnos_collection = db["alumnos"]
boletas_collection = db["boletas"]
