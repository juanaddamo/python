var1 = lambda a, b, c : a + b + c
print(var1(1,2,3,))

#Muestro un rango de numeros
n = int(input("Ingrese un numero entero: "))
nros = range(n)

#Calculo del cuadrado de los numeros
cuadrado = list(map(lambda x: x**2, nros))
print("Calculo de cuadrado de los numeros", cuadrado)

#Mostrar los numeros pares
pares = list(filter( lambda x: x%2 == 0, nros))
print("Nros pares", pares)