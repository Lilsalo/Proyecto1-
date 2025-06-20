import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


from classes.alumno import Alumno
from classes.boleta import BoletaCalificaciones

if __name__ == "__main__":
    # Crea y guarda alumno
    alumno = Alumno("Salome Rosales", "20211021503", "Ingeniería en sistemas", "salome.rosales@unah.hn")
    alumno_id = alumno.save()

    # Paso 2: Crea y guarda boleta con el alumno_id
    boleta = BoletaCalificaciones(89.3, 2024, 6, 2, alumno_id)
    boleta_id = boleta.save()

    # Paso 3: Actualiza el alumno con el boleta_id
    alumno.update_boleta_id(alumno_id, boleta_id)

    # Paso 4: Actualiza el promedio de la boleta
    boleta.update_promedio(boleta_id, 95.7)

    print("Relación 1:1 guardada y actualizada con éxito.")
