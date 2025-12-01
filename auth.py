#inicio de sesion
from storage import *
import csv
usuarios_path = "usuarios.csv"



def login(username, password, users, cred_admin):
    if password ==  cred_admin[1] and username == cred_admin[0]:
            print("---------------------------------------------------------------")
            print("                      PANEL ADMINISTRADOR                      ")
            print("---------------------------------------------------------------")
            #funciones admin: listar visitantes, buscar visitantes por id(posiblemente tambien lo pueda hacer el usuario normal), ver misiones, agregar misiones, eliminar misiones, modificar misiones, estadisticas(contar visitantes, visitantes por especie, visitantes activos y retirados), artefactos
            menu = input("1. Listar visitantes \n2. Buscar visitante por username \n3. Ver misiones \n4. Agregar misiones \n5. Eliminar misiones \n6. Modificar misiones \n7. Estadísticas \n8. Gestionar artefactos: ")
            
            match menu:
                case "1": 
                    mostrar_usuarios(usuarios_path)  
                case "2":
                    usuario_buscar = input("Ingrese el nombre de usuario a buscar: ")
                    buscar_usuario(usuarios_path, usuario_buscar) 
                    
            valid_ingreso = True
    else:
        for user in users:
            if (username == users["Usuario"]) and password == users["Contrasena"]:
                print("---------------------------------------------------------------")
                print("                        PANEL USUARIO                          ")
                print("---------------------------------------------------------------")
                #funciones usuario: ver artefactos, ver misiones, buscar artefactos por id, buscar misiones por id, ver misiones asignadas, ver artefactos encontrados, modificar datos personales, eliminar cuenta
                valid_ingreso = True
                break
            cont += 1
        print("Nombre de usuario o contraseña incorrectos.")
        valid_ingreso = False
        
    return valid_ingreso
    
def registrar(users):
        print("---------------------------------------------------------------")
        print("                         REGISTRARSE                            ")
        print("---------------------------------------------------------------")

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
