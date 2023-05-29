import csv
from .particular import Particular
from .carga import Carga
from .bicicleta import Bicicleta
from .motocicleta import Motocicleta
import json
from json.decoder import JSONDecodeError

class Utilidades:
    def  guardar_datos_csv(self, archivo_csv, vehiculo):
        try:
            with open(archivo_csv, 'a', newline='') as archivo:
                writer = csv.writer(archivo)
                writer.writerow([vehiculo.__class__, str(vehiculo.__dic__())])
        except Exception as e:
            print(f"Error al guardar datos en el archivo CSV: {e}")
        
    def leer_datos_csv(self, archivo_csv):
        vehiculos = []
        #Leer el archivo CSV y crear las instancias de vehículos
        try:
            with open(archivo_csv, "r") as file:
                reader = csv.reader(file)
                for row in reader: #Cada linea que se lee del archivo se obtiene como una lista con el siguiente formato [clase, datos]
                    vehiculos.append(row)
        except FileNotFoundError:
            print("Archivo no encontradon\n\n")
        except Exception as e:
            print("Error: %s\n\n" %e)
        return vehiculos
    
    def procesar_datos(self, vehiculos_datos):
        # Mapeo de tipos de vehículos a sus clases correspondientes
        tipo_vehiculo_clase = {
            str(Particular.__mro__[0]): Particular,
            str(Carga.__mro__[0]): Carga,
            str(Bicicleta.__mro__[0]): Bicicleta,
            str(Motocicleta.__mro__[0]): Motocicleta
        }
        vehiculos = []
        for vehiculo in vehiculos_datos:
            try:
                tipo_vehiculo = vehiculo[0]
                datos_str = vehiculo[1].replace("'", "\"")  # Reemplazar comillas simples por comillas dobles
                datos = json.loads(datos_str)  # Convertir la cadena a un diccionario

                # Crear la instancia del vehículo correspondiente al tipo
                if tipo_vehiculo in tipo_vehiculo_clase:
                    vehiculo_clase = tipo_vehiculo_clase[tipo_vehiculo]
                    vehiculo = vehiculo_clase(**datos)
                    vehiculos.append(vehiculo)
            except JSONDecodeError as e:
                print(f"Error al decodificar JSON: {e}")
        return vehiculos
    
    def crear_datos(self):
        vehiculos = []
        vehiculos.append(Particular("Ford", "Fiesta", 4, "180", "500", 5))
        vehiculos.append(Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000"))
        vehiculos.append(Bicicleta("Shimano", "MT Ranger", 2, "Carrera"))
        vehiculos.append(Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21))
        return vehiculos
    
    def mostrar_lista_vehiculos(self, titulo, vehiculos):
        if(len(vehiculos)):
            print(titulo)
            for vehiculo in vehiculos:
                print(vehiculo.__dic__())
            print("\n\n")

    def mostrar_vehiculos(self, vehiculos):
        self.mostrar_lista_vehiculos("Lista de Vehiculos Particular", list(filter(lambda vehiculo: isinstance(vehiculo, Particular),vehiculos)))
        self.mostrar_lista_vehiculos("Lista de Vehiculos Carga", list(filter(lambda vehiculo: isinstance(vehiculo, Carga), vehiculos)))
        self.mostrar_lista_vehiculos("Lista de Vehiculos Bicicleta", list(filter(lambda vehiculo: isinstance(vehiculo, Bicicleta) and not isinstance(vehiculo, Motocicleta), vehiculos)))
        # self.mostrar_lista_vehiculos("Lista de Vehiculos Motocicleta", list(filter(lambda vehiculo: isinstance(vehiculo, Motocicleta), vehiculos)))
        self.mostrar_lista_vehiculos("Lista de Vehiculos Motocicleta", [item for item in vehiculos if isinstance(item, Motocicleta)])

    def __init__(self):
        # Este constructor esta vacio dado a que solo se quiere crear una instancia de esta y utiliar sus funciones
        pass