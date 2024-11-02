def fac (n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
    
nro = int(input("Ingrese el nummero para calcular el factorial: "))
res = fac(nro)
print("El numero ingresado es: ", nro)
print("El factorial de", nro, "es :", res)