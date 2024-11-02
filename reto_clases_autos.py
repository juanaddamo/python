# Desarrolla una concesionaria de vehículos en la cual se puedan gestionar las compras y ventas de vehículos. 
# Un usuario podrá ver los vehículos disponibles, su precio y realizar la compra de uno. 

from typing import Any

class car:
    def __init__(self, ind, brand, model, color, year, price):
        self.ind = ind
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def __str__(self):
        return f"Indice: {self.ind} Marca: {self.brand}, Modelo: {self.model}, Color: {self.color}, Año: {self.year}, Precio: ${self.price}"

class car_dealership:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_cars(self):
        for car in self.cars:
            print(car)

    def buy_car(self, inde):
        if inde < len(self.cars):
            car_bought = self.cars.pop(inde)
            print(f"El usuario ha comprado el automovil --> {car_bought}")
        else:
            print("El automovil seleccionado es inválido.")

# Creo car_deealership
concesionaria = car_dealership()

#Agrego los automoviles a la concesionaria
concesionaria.add_car(car("0","Toyota", "Corolla", "Gris claro", 2023, 25000))
concesionaria.add_car(car("1","Honda", "Civic", "Blanco", 2022, 22000))
concesionaria.add_car(car("2","Nissan", "Sentra", "Negro", 2023, 23000))
concesionaria.add_car(car("3","Toyota", "Corolla Cross", "Gris oscuro", 2024, 28000))

# Mostrar los vehículos disponibles
print("Automoviles disponibles:")
concesionaria.show_cars()

# Seleccionar el automovil y comprarlo
indice_auto = int(input("Ingrese el índice del automovil que desea comprar: "))
concesionaria.buy_car(indice_auto)

# Mostrar los vehículos disponibles
print("Automoviles disponibles:")
concesionaria.show_cars()