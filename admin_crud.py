import csv
from storage import cargar_misiones, guardar_misiones

def ver_misiones_disponibles():
    misiones = cargar_misiones("misiones.csv")
    print("---------------------------------------------------------------")
    print("                  MISIONES DISPONIBLES                          ")
    print("---------------------------------------------------------------")    
    for mision in misiones:
        print(f"ID: {mision['id']}")
        print(f"Nombre: {mision['nombre']}")
        print(f"Dificultad: {mision['dificultad']}")
        print(f"Descripción: {mision['descripcion']}")
        print(f"Objetivo: {mision['objetivo']}")
        print(f"Recompensa: {mision['recompensa']}")
        print("---------------------------------------")

def agregar_mision(id):
    misiones = cargar_misiones("misiones.csv")
    if id in [mision["id"] for mision in misiones]:
        print("Ya existe una misión con ese ID.")
        return
    else:
        nueva_mision = {
            "id": id,
            "nombre": input("Ingrese el nombre de la misión: "),
            "dificultad": input("Ingrese la dificultad de la misión: "),
            "descripcion": input("Ingrese la descripción de la misión: "),
            "objetivo": input("Ingrese el objetivo de la misión: "),
            "recompensa": input("Ingrese la recompensa de la misión: ")
        }
        misiones.append(nueva_mision)
        guardar_misiones(misiones)
        print("Misión agregada exitosamente.")