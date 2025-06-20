from conexion import boletas_collection
from bson.objectid import ObjectId

class BoletaCalificaciones:
    def __init__(self, promedio_general, anio_lectivo, materias_aprobadas, materias_reprobadas, alumno_id=None):
        self.promedio_general = promedio_general
        self.anio_lectivo = anio_lectivo
        self.materias_aprobadas = materias_aprobadas
        self.materias_reprobadas = materias_reprobadas
        self.alumno_id = alumno_id

    def save(self):
        data = {
            "promedio_general": self.promedio_general,
            "anio_lectivo": self.anio_lectivo,
            "materias_aprobadas": self.materias_aprobadas,
            "materias_reprobadas": self.materias_reprobadas,
            "alumno_id": self.alumno_id
        }
        result = boletas_collection.insert_one(data)
        return result.inserted_id

    def update_promedio(self, boleta_id, nuevo_promedio):
        filtro = {"_id": ObjectId(boleta_id)}
        nuevos_valores = {"$set": {"promedio_general": nuevo_promedio}}

        resultado = boletas_collection.update_one(filtro, nuevos_valores)

        if resultado.matched_count > 0:
            print("Boleta actualizada correctamente.")
        else:
            print("No se encontró ninguna boleta con ese ID.")
