import csv
from storage import *
from admin_crud import *

usuarios_path = "usuarios.csv"




def panel_admin(username):

    #funciones admin: listar visitantes, buscar visitantes por id(posiblemente tambien lo pueda hacer el usuario normal), ver misiones, agregar misiones, eliminar misiones, modificar misiones, estadisticas(contar visitantes, visitantes por especie, visitantes activos y retirados), artefactos
    salir = 1

    while salir != 0:
        print("---------------------------------------------------------------")
        print("                      PANEL ADMINISTRADOR                      ")
        print("---------------------------------------------------------------")
        menu = input("1. Listar visitantes \n2. Buscar visitante por nombre de usuario \n3. Ver misiones \n4. Agregar misiones \n5. Eliminar misiones \n6. Modificar misiones  \n7. Gestionar artefactos \n8. Salir: ")
       
        match menu:  
          
            case "1": 
                mostrar_usuarios(usuarios_path)  
            case "2":
                usuario_buscar = input("Ingrese el nombre de usuario del usuario que quiere buscar: ")
                print("---------------------------------------------------------------")

                buscar_usuario(usuarios_path, usuario_buscar)
            case "3":
                ver_misiones_disponibles()
            case "4":
                mision_agg = None
                while mision_agg != True:
                    print("---------------------------------------------------------------")

                    id = input("Ingrese el ID de la nueva misión: ")
                    mision_agg = agregar_mision(id)
                    if mision_agg == False:
                        desicion = input("Desea intentar con otro ID? (s/n): ")
                        if desicion.lower() == "s":
                            mision_agg = desicion
                        elif desicion.lower() == "n":
                            mision_agg = True
                        else:
                            print("Opción no válida")
                    elif mision_agg == True:
                        print("Misión agregada correctamente.")
                        mision_agg = True
                    else:
                        print("Opción no válida")   
            case "5":
                eliminar_mision(input("Ingrese el ID de la misión que desea eliminar: "))

            case "6":
                modificar_mision(input("Ingrese el ID de la misión que desea modificar: "))
            case "7":
                print("Función de gestionar artefactos en desarrollo...")
                salir = 0
                while salir < 1:
                    menu = menu_objetos()

                    match menu:
                        case "1":
                            crear_objeto()
                        case "5":
                            print("Saliendo de gestion de artefactos...")
                            salir = 2
                        case _:
                            print("Opcion inválida")
                           
            case "8":
                salir = 0
                print("Saliendo del panel de administrador...") 
            case _:
                print("Opción no válida, por favor intente de nuevo....")
