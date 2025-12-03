import csv
from storage import cargar_misiones, guardar_misiones

def ver_misiones_disponibles():
    misiones = cargar_misiones("misiones.csv")
    print("""---------------------------------------------------------------
                        MISIONES DISPONIBLES
---------------------------------------------------------------""")
    for mision in misiones:
        print(f"""---------------------------------------------------------------
                        MISION {mision['id']}
---------------------------------------------------------------""")
        print(f"ID: {mision['id']}")
        print(f"Nombre: {mision['nombre']}")
        print(f"Dificultad: {mision['dificultad']}")
        print(f"Descripción: {mision['descripcion']}")
        print(f"Objetivo: {mision['objetivo']}")
        print(f"Recompensa: {mision['recompensa']}")
        print("---------------------------------------")

def agregar_mision(id):
    print("""---------------------------------------------------------------
                        AGREGAR MISIÓN                            
---------------------------------------------------------------""")
    misiones = cargar_misiones("misiones.csv")
    if id in [mision["id"] for mision in misiones]:
        print("Ya existe una misión con ese ID.")
        return False
    else:
        desicion = 0
        cont = 0
        while desicion != "n":
            cont += 1
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
            if cont >= 1:
                desicion = input("¿Desea agregar otra misión? (s/n): ").lower()
                if desicion not in ["s", "n"]:
                    print("Opción no válida")
                    desicion = 0

        return True

def eliminar_mision(id):
    misiones = cargar_misiones("misiones.csv")
    misiones_actualizadas = [mision for mision in misiones if mision["id"] != id]
    if len(misiones) == len(misiones_actualizadas):
        print("No se encontró una misión con ese ID.")
        return False
    else:
        guardar_misiones(misiones_actualizadas)
        print("Misión eliminada correctamente.")
        return True

def modificar_mision(id):
    print("""---------------------------------------------------------------
                        MODIFICAR MISIÓN                            
---------------------------------------------------------------""")
    misiones = cargar_misiones("misiones.csv")
    for mision in misiones:
        if mision["id"] == id:
            print("Ingrese los nuevos datos de la misión (deje en blanco para mantener el valor actual):")
            nombre = input(f"Nombre ({mision['nombre']}): ") or mision['nombre']
            dificultad = input(f"Dificultad ({mision['dificultad']}): ") or mision['dificultad']
            descripcion = input(f"Descripción ({mision['descripcion']}): ") or mision['descripcion']
            objetivo = input(f"Objetivo ({mision['objetivo']}): ") or mision['objetivo']
            recompensa = input(f"Recompensa ({mision['recompensa']}): ") or mision['recompensa']

            mision.update({
                "nombre": nombre,
                "dificultad": dificultad,
                "descripcion": descripcion,
                "objetivo": objetivo,
                "recompensa": recompensa
            })
            guardar_misiones(misiones)
            print("Misión modificada correctamente.")
            return True
    print("No se encontró una misión con ese ID.")
    return False

"""
A partir de aqui se le hará CRUD especificamente a la parte del objeto, tanto funciones para crearlo, leer los objetos existentes, actualizar información del objeto como tambien para eliminar algun objeto 
"""

def menu_objetos():

    print("""------------------------------------------------------
            PANEL ARTEFACTOS
------------------------------------------------------
            Bienvenido a la gestion de artefactos. ¿Que deseas hacer?
            1. Crear un nuevo objeto
            2. Buscar objeto
            3. Leer objetos encontrados
            4. Eliminar algun objeto
            5. Salir""")
    menu = input("Digita el numero de la opcion correspondiente: ")

    return menu



def crear_objeto(id):
    pass