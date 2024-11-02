#sumatoria de numeros naturales
def sum_nat (n):
    if n == 0:
        return 0
    else:
        return n + sum_nat(n-1)

nro = int(input("Ingrese un numero natural: "))
print("La sumatoria de los", nro, "numeros naturales es: ",sum_nat(nro))