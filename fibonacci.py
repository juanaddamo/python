def fibo (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo (n-1) + fibo (n-2)
    
nro = int(input("Ingrese cuantos numeros de la serie Fibonacci quiere mostrar :"))
print("Numero final de la serie: ", fibo(nro))