import csv
from storage import *
from admin_crud import agregar_mision
usuarios_path = "usuarios.csv"




def panel_admin(username):

    #funciones admin: listar visitantes, buscar visitantes por id(posiblemente tambien lo pueda hacer el usuario normal), ver misiones, agregar misiones, eliminar misiones, modificar misiones, estadisticas(contar visitantes, visitantes por especie, visitantes activos y retirados), artefactos
    salir = 1

    while salir != 0:
        print("---------------------------------------------------------------")
        print("                      PANEL ADMINISTRADOR                      ")
        print("---------------------------------------------------------------")
        menu = input("1. Listar visitantes \n2. Buscar visitante por nombre de usuario \n3. Ver misiones \n4. Agregar misiones \n5. Eliminar misiones \n6. Modificar misiones \n7. Estadísticas \n8. Gestionar artefactos \n9. Salir: ")
       
        match menu:  
          
            case "1": 
                mostrar_usuarios(usuarios_path)  
            case "2":
                usuario_buscar = input("Ingrese el nombre de usuario del usuario que quiere buscar: ")
                buscar_usuario(usuarios_path, usuario_buscar)
            case "3":
                print("Función de ver misiones en desarrollo...")
            case "4":
                print("""---------------------------------------------------------------
                        AGREGAR MISIÓN                            
---------------------------------------------------------------""")
                id = input("Ingrese el ID de la nueva misión: ")
                agregar_mision(id)
            case "5":
                print("Función de eliminar misiones en desarrollo...")
            case "6":
                print("Función de modificar misiones en desarrollo...")
            case "7":
                print("Función de estadísticas en desarrollo...")
            case "8":
                print("Función de gestionar artefactos en desarrollo...")
            case "9":
                salir = 0
                print("Saliendo del panel de administrador...") 
            case _:
                print("Opción no válida, por favor intente de nuevo....")
