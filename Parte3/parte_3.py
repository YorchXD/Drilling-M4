from clases.utilidades import Utilidades

def menu():
    print("######################## MENU #########################")
    print("#                                                     #")
    print("# 1. Crear datos                                      #")
    print("# 2. Mostrar datos                                    #")
    print("# 3. Guardar datos                                    #")
    print("# 4. Leer datos                                       #")
    print("# 5. Hacer todo (crear, guardar, leer y mostrar)      #")
    print("# 6. Salir                                            #")
    print("#                                                     #")
    print("#######################################################\n\n")
    opcion = int(input("Ingrese una opcion: "))
    print("\n\n\n")
    return opcion

def guardar_datos(archivo_csv, vehiculos):
    for vehiculo in vehiculos:
        utilidades.guardar_datos_csv(archivo_csv, vehiculo)
        
def mostrar_datos(vehiculos):
    print("Lista de vehiculos...\n")
    for vehiculo in vehiculos:
        print(vehiculo.__str__())
    print("\n\n")
    
################### MAIN FUN ###################
vehiculos= []
archivo_csv = 'vehiculos.csv '
utilidades = Utilidades()

while True:
    opcion = menu()
    match opcion:
        case 1:
            vehiculos=utilidades.crear_datos()
        case 2:
            mostrar_datos(vehiculos)
        case 3:
            guardar_datos(archivo_csv, vehiculos)
        case 4:
            vehiculos_data=utilidades.leer_datos_csv(archivo_csv)
            vehiculos=utilidades.procesar_datos(vehiculos_data)
            utilidades.mostrar_vehiculos(vehiculos)
        case 5:
            vehiculos=utilidades.crear_datos()
            guardar_datos(archivo_csv, vehiculos)
            vehiculos_data=utilidades.leer_datos_csv(archivo_csv)
            vehiculos=utilidades.procesar_datos(vehiculos_data)
            utilidades.mostrar_vehiculos(vehiculos) 
        case 6:
            print("Adios!!")
            break # Quiebra el ciclo infinito
        case _:
            print("Opcion mal ingresada, por favor vuelva a intentarlo")
