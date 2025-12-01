import csv
from storage import *
from auth import *



print("--------------------------------------------------------------")
print("Bienvenido a galáctic library. ¿Que deseas hacer el dia de hoy")
print("--------------------------------------------------------------")
menu = input("1. Iniciar sesion \n2. Registrarse \n3. Ver vitrina de artefáctos encontrados \n4. Misiones disponibles: ")
users = cargar_usuarios("usuarios.csv")
cred_admin = cargar_admin("admin_access.csv")

match menu:
    case "1":
        print("---------------------------------------------------------------")
        print("                        INICIO DE SESION                       ")
        print("---------------------------------------------------------------")

        username = input("Usuario: ")
        password = input("Contraseña: ")
        intentos = 0        
        valid_ingreso = login(username, password, users, cred_admin)
        if valid_ingreso == False:
            intentos += 1
            while intentos < 3:
                print(f"Intento {intentos + 1} de 3")
                username = input("Usuario: ")
                password = input("Contraseña: ")
                if login(username, password, users) is not None:
                    break
                intentos += 1
            if intentos == 3:
                print("Has excedido el número máximo de intentos. Inténtalo más tarde.") 
        
    case "2":
        registrar(users)