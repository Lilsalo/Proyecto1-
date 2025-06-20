from pymongo import MongoClient

uri = "mongodb+srv://Lilsalo:salomongodb@cluster0.nqlvxee.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

db = client["escuela"]
alumnos_collection = db["alumnos"]
boletas_collection = db["boletas"]
