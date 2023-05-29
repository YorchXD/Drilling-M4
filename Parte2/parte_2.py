from clases.vehiculo import Vehiculo
from clases.automovil import Automovil
from clases.particular import Particular
from clases.carga import Carga
from clases.bicicleta import Bicicleta
from clases.motocicleta import Motocicleta

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

print(particular.__str__())
print(carga.__str__())
print(bicicleta.__str__())
print(motocicleta.__str__())

print("\n\n")

print(f"Motocicleta es instancia con relación a Vehículo:{isinstance(motocicleta, Vehiculo)}")
print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, Particular)}")
print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, Carga)}")
print(f"Motocicleta es instancia con relación a Bicicleta:{isinstance(motocicleta, Bicicleta)}")
print(f"Motocicleta es instancia con relación a Motocicleta:{isinstance(motocicleta, Motocicleta)}")


















# cant_vehiculos = int(input("Cuantos Vehiculos desea insertar: "))
# automoviles = []

# for i in range(cant_vehiculos):
#     print(f"Datos del automovil {i+1}")
#     marca = input("Inserte la marca del automovil: ")
#     modelo = input("Inserte el modelo del automovil: ")
#     num_ruedas = int(input("Inserte el numero de ruedas: "))
#     velocidad = int(input("Inserte la velocidad en km/h: "))
#     cilindradas = int(input("Inserte el cilindraje en cc: "))
#     automoviles.append(Automovil(marca, modelo, num_ruedas, velocidad, cilindradas))
#     print("\n\n")
    
# print("Imprimiendo por pantalla los Vehiculos:\n")
# for i in range(len(automoviles)):
#     print(f"Datos del automóvil {i+1}: {automoviles[i].__str__()}\n")

