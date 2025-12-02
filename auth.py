#inicio de sesion
from storage import *
import csv
from paneles import panel_admin
usuarios_path = "usuarios.csv"



def login(username, password, users, cred_admin):
    if password ==  cred_admin[1] and username == cred_admin[0]:
            panel_admin(username)
            valid_ingreso = True
    else: 
        cont = 0
        for user in users:
            if (username == users[cont]["Usuario"]) and (password == users[cont]["Contrasena"]):
                print("---------------------------------------------------------------")
                print("                        PANEL USUARIO                          ")
                print("---------------------------------------------------------------")
                #funciones usuario: ver artefactos, ver misiones, buscar artefactos por id, buscar misiones por id, ver misiones asignadas, ver artefactos encontrados, modificar datos personales, eliminar cuenta
                valid_ingreso = True
                break
            cont += 1
        else:
            valid_ingreso = None

    return valid_ingreso
    
def registrar(users):
        print("""---------------------------------------------------------------
                        REGISTRARSE                            
---------------------------------------------------------------""")

        new_user = input("Ingrese su nuevo usuario: ")
        new_password = input("Ingrese su nueva contraseña: ")

        users.append({
            "Nombre": input("Ingrese su nombre: "),
            "Especie": input("Ingrese su especie: "),
            "Usuario": new_user,
            "Contrasena": new_password,
            "Estado": "Activo"
        })
        guardar_usuarios(users)
        print("¡Registro exitoso! Ahora puedes iniciar sesión con tus credenciales.")
        return new_user, new_password

