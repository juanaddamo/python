def greet(name = "No tiene nombre", last_name = "No tiene apellido"):
    print("Hola", name, last_name)

nom = input("Cual es tu nombre? ")
ape = input("Cual es tu apellido? ")

greet(nom, ape)