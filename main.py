import csv
from storage import *
from auth import login, registrar


users = cargar_usuarios("usuarios.csv")
cred_admin = cargar_admin("admin_access.csv")
menu = 0
while menu != "5":
    print("""--------------------------------------------------------------
Bienvenido a galáctic library. ¿Que deseas hacer el dia de hoy
--------------------------------------------------------------""")
    menu = input("1. Iniciar sesion \n2. Registrarse \n3. Ver vitrina de artefáctos encontrados \n4. Misiones disponibles \n5. Salir: ")
    match menu:
        case "1":
            print("""---------------------------------------------------------------
                        INICIO DE SESION                       
---------------------------------------------------------------""")
            intentos = 0        

            while intentos < 3:
                username = input("Usuario: ")
                password = input("Contraseña: ")
                valid_ingreso = login(username, password, users, cred_admin)
                if valid_ingreso == None:
                    print("Nombre de usuario o contraseña incorrectos.")
                    intentos += 1
                else:
                    intentos = 3
    
        case "2":
            user, psw = registrar(users)
            valid_ingreso = (user, psw, cred_admin, users)
        case _:
            print("""Opción no válida, por favor intente de nuevo....
                  
            -----------------------------------------------
                  Retornando al menú principal.""")

"""
3. Para la vitrina de artefactos encontrados pienso listarlo como listé en el trabajo de los libros

4. Con las misiones disponibles las haré como ranking de objetos a encontrar, y los categorizaré como comun, raro, epico, legendario
    cada mision solo podrá ser tomada por un usuario que esté logueado, se verá desde la pantalla del usuario y ahi se le asignará el objeto
"""  