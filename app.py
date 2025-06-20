from classes.alumno import Alumno
from classes.boleta import BoletaCalificaciones

if __name__ == "__main__":
    alumno = Alumno("Salome Rosales", "20211021503", "Ingeniería en sistemas", "salome.rosales@unah.hn")
    alumno_id = alumno.save()

    if alumno_id is not None:
        boleta = BoletaCalificaciones(91.0, 2024, 7, 1, alumno_id)
        boleta_id = boleta.save()

        alumno.update_boleta_id(alumno_id, boleta_id)
        boleta.update_promedio(boleta_id, 95.7)

        print("Relación 1:1 guardada y actualizada con éxito.")
    else:
        print("No se creó boleta ni se actualizó nada porque el alumno ya existía.")
