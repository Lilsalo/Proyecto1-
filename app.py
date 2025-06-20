import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


from classes.alumno import Alumno
from classes.boleta import BoletaCalificaciones

if __name__ == "__main__":
    # Paso 1: Crear y guardar alumno
    alumno = Alumno("Salome Rosales", "20211021503", "Ingeniería en sistemas", "salome.rosales@unah.hn")
    alumno_id = alumno.save()

    # Paso 2: Crear y guardar boleta con el alumno_id
    boleta = BoletaCalificaciones(89.3, 2024, 6, 2, alumno_id)
    boleta_id = boleta.save()

    # Paso 3: Actualizar el alumno con el boleta_id
    alumno.update_boleta_id(alumno_id, boleta_id)

    # Paso 4: Actualizar el promedio de la boleta
    boleta.update_promedio(boleta_id, 95.7)

    print("Relación 1:1 guardada y actualizada con éxito.")
