from clases.automovil import Automovil

cant_vehiculos = int(input("Cuantos Vehiculos desea insertar: "))
automoviles = []

for i in range(cant_vehiculos):
    print(f"Datos del automovil {i+1}")
    marca = input("Inserte la marca del automovil: ")
    modelo = input("Inserte el modelo del automovil: ")
    num_ruedas = int(input("Inserte el numero de ruedas: "))
    velocidad = int(input("Inserte la velocidad en km/h: "))
    cilindradas = int(input("Inserte el cilindraje en cc: "))
    automoviles.append(Automovil(marca, modelo, num_ruedas, velocidad, cilindradas))
    print("\n\n")
    
print("Imprimiendo por pantalla los Vehiculos:\n")
for i in range(len(automoviles)):
    print(f"Datos del automóvil {i+1}: {automoviles[i].__str__()}\n")