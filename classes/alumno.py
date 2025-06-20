from conexion import alumnos_collection
from bson.objectid import ObjectId

class Alumno:
    def __init__(self, nombre, matricula, carrera, correo, boleta_id=None):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.correo = correo
        self.boleta_id = boleta_id

    def save(self):
        data = {
            "nombre": self.nombre,
            "matricula": self.matricula,
            "carrera": self.carrera,
            "correo": self.correo,
            "boleta_id": self.boleta_id
        }
        result = alumnos_collection.insert_one(data)
        return result.inserted_id

    def update_boleta_id(self, alumno_id, boleta_id):
        filtro = {"_id": ObjectId(alumno_id)}
        nuevos_valores = {"$set": {"boleta_id": ObjectId(boleta_id)}}

        resultado = alumnos_collection.update_one(filtro, nuevos_valores)

        if resultado.matched_count > 0:
            print("Documento encontrado y actualizado correctamente.")
        else:
            print("No se encontró ningún documento con ese ID.")
