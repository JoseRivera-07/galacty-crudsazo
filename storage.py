#leer y escribir en el csv
import csv

def guardar_usuarios(users, archivo="usuarios.csv"):
    import csv
    with open(archivo, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Nombre", "Especie", "Usuario", "Contrasena", "Estado"])
        writer.writeheader()
        writer.writerows(users)
        
    print("Usuarios guardados correctamente en", archivo)    

def cargar_usuarios(path_csv):
    usuarios =[]
    try:
        with open(path_csv, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                usuarios.append({
                    "Nombre": fila["Nombre"],
                    "Especie": fila["Especie"],
                    "Usuario": fila["Usuario"],
                    "Contrasena": fila["Contrasena"],
                    "Estado": fila.get("Estado", "Activo")  
                })
    except FileNotFoundError:
        print("No se encontró el archivo")
    return usuarios

def cargar_admin(path_csv):
    try:
        with open(path_csv, newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            next(lector)
            for usuario, password in lector:
                return (usuario, password)
    except FileNotFoundError:
        print("No se encontró el archivo")
        return None, None

def mostrar_usuarios(path_csv):
    print("---------------------------------------------------------------")
    print("                     LISTA DE VISITANTES                       ")
    print("---------------------------------------------------------------")    
    try:
        with open(path_csv, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for i, fila in enumerate(lector, start=1):
                print(f"Usuario #{i}")
                print(f"  Nombre:     {fila['Nombre']}")
                print(f"  Especie:    {fila['Especie']}")
                print(f"  Usuario:    {fila['Usuario']}")
                print(f"  Contraseña: {fila['Contrasena']}")
                print(f"  Estado:     {fila['Estado']}")
                print("---------------------------------------")
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")

def buscar_usuario(path_csv, usuario):
    try:
        with open(path_csv, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for i, fila in enumerate(lector, start=1):
                print(f"Usuario #{i}")
                if fila["Usuario"] == usuario:
                    print(f"  Nombre:     {fila['Nombre']}")
                    print(f"  Especie:    {fila['Especie']}")
                    print(f"  Usuario:    {fila['Usuario']}")
                    print(f"  Contraseña: {fila['Contrasena']}")
                    print(f"  Estado:     {fila['Estado']}")
                    print("---------------------------------------")
                    return
            print("Usuario no encontrado.")
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
        
def cargar_misiones(path_csv):
    misiones =[]
    try:
        with open(path_csv, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                misiones.append({
                    "id": fila["id"],
                    "nombre": fila["nombre"],
                    "dificultad": fila["dificultad"],
                    "descripcion": fila["descripcion"],
                    "objetivo": fila["objetivo"],
                    "recompensa": fila["recompensa"]
                })
    except FileNotFoundError:
        print("No se encontró el archivo de misiones")
    return misiones

def guardar_misiones(misiones, archivo="misiones.csv"):
    import csv
    with open(archivo, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "nombre", "dificultad", "descripcion", "objetivo", "recompensa"])
        writer.writeheader()
        writer.writerows(misiones)
        
    print("Misiones guardadas correctamente en", archivo)