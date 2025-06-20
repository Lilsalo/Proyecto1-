import unittest
from classes.alumno import Alumno
from classes.boleta import BoletaCalificaciones
from pymongo import MongoClient
from bson.objectid import ObjectId

# Conexión a MongoDB remota (asegúrate de que coincida con tu entorno)
client = MongoClient("mongodb+srv://Lilsalo:salomongodb@cluster0.nqlvxee.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["escuela"]
alumnos_collection = db["alumnos"]
boletas_collection = db["boletas"]

class TestRelacionUnoAUno(unittest.TestCase):

    def test_guardado_y_actualizacion(self):
        # Crear y guardar Alumno
        alumno = Alumno("Carlos Mejía", "20231234", "Derecho", "carlos@correo.com")
        alumno_id = alumno.save()
        print(f"Alumno guardado con ID: {alumno_id}")

        # Crear y guardar Boleta con alumno_id
        boleta = BoletaCalificaciones(91.0, 2024, 7, 1, alumno_id)
        boleta_id = boleta.save()
        print(f"Boleta guardada con ID: {boleta_id}")

        # Actualizar Alumno con boleta_id
        alumno.update_boleta_id(alumno_id, boleta_id)
        print("Alumno actualizado con boleta_id.")

        # Verificar relación en base de datos
        alumno_db = alumnos_collection.find_one({"_id": alumno_id})
        boleta_db = boletas_collection.find_one({"_id": boleta_id})
        print(f"Relación en BD: alumno.boleta_id = {alumno_db.get('boleta_id')}, boleta.alumno_id = {boleta_db.get('alumno_id')}")

        self.assertEqual(boleta_db["alumno_id"], alumno_id)
        self.assertEqual(alumno_db["boleta_id"], boleta_id)

        # Actualizar promedio de la boleta
        boleta.update_promedio(boleta_id, 97.5)
        print("Promedio actualizado en la boleta.")

        # Verificar que se actualizó en la base de datos
        boleta_db_actualizada = boletas_collection.find_one({"_id": boleta_id})
        print(f"Nuevo promedio en BD: {boleta_db_actualizada['promedio_general']}")
        self.assertEqual(boleta_db_actualizada["promedio_general"], 97.5)

if __name__ == "__main__":
    unittest.main()
