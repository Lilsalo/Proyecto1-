import unittest
from classes.alumno import Alumno
from classes.boleta import BoletaCalificaciones

from conexion import alumnos_collection, boletas_collection

class TestRelacionUnoAUno(unittest.TestCase):

    def test_guardado_y_actualizacion(self):
        # Crear y guardar Alumno
        alumno = Alumno("Marlon Marineros", "20212031403", "Medicina", "MarlonMarineros@unah.")
        alumno_id = alumno.save()
        print(f"Alumno guardado con ID: {alumno_id}")

        # Crea y guardar Boleta con alumno_id
        boleta = BoletaCalificaciones(91.0, 2025, 7, 1, alumno_id)
        boleta_id = boleta.save()
        print(f"Boleta guardada con ID: {boleta_id}")

        # Actualiza Alumno con boleta_id
        alumno.update_boleta_id(alumno_id, boleta_id)
        print("Alumno actualizado con boleta_id.")

        # Verifica relación en base de datos
        alumno_db = alumnos_collection.find_one({"_id": alumno_id})
        boleta_db = boletas_collection.find_one({"_id": boleta_id})
        print(f"Relación en BD: alumno.boleta_id = {alumno_db.get('boleta_id')}, boleta.alumno_id = {boleta_db.get('alumno_id')}")

        self.assertEqual(boleta_db["alumno_id"], alumno_id)
        self.assertEqual(alumno_db["boleta_id"], boleta_id)

        # Actualiza promedio de la boleta
        boleta.update_promedio(boleta_id, 97.5)
        print("Promedio actualizado en la boleta.")

        # Verifica que se actualizó en la base de datos
        boleta_db_actualizada = boletas_collection.find_one({"_id": boleta_id})
        print(f"Nuevo promedio en BD: {boleta_db_actualizada['promedio_general']}")
        self.assertEqual(boleta_db_actualizada["promedio_general"], 97.5)

if __name__ == "__main__":
    unittest.main()
