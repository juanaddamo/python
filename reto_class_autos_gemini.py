class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Precio: ${self.precio}"

class Concesionaria:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrar_vehiculos(self):
        for vehiculo in self.vehiculos:
            print(vehiculo)

    def comprar_vehiculo(self, indice):
        if indice < len(self.vehiculos):
            vehiculo_comprado = self.vehiculos.pop(indice)
            print(f"¡Felicidades! Has comprado un {vehiculo_comprado}")
        else:
            print("Índice de vehículo inválido.")

# Crear una concesionaria
concesionaria = Concesionaria()

# Agregar vehículos a la concesionaria
concesionaria.agregar_vehiculo(Vehiculo("Toyota", "Corolla", 2023, 25000))
concesionaria.agregar_vehiculo(Vehiculo("Honda", "Civic", 2022, 22000))

# Mostrar los vehículos disponibles
print("Vehículos disponibles:")
concesionaria.mostrar_vehiculos()

# Comprar un vehículo (el índice comienza desde 0)
indice_vehiculo = int(input("Ingrese el índice del vehículo que desea comprar: "))
concesionaria.comprar_vehiculo(indice_vehiculo)