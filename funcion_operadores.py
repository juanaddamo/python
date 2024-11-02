#def suma(a, b):
#    return a + b

def oper(a,b):
    print("suma: ", a + b)
    print("resta: ", a - b)
    print("multiplicacion:", a * b)
    if b!=0:
        print("division: ", a / b)
    else:
        print("no se puede dividir por 0")

num_1 = float(input("ingrese numero 1:"))
num_2 = float(input("ingrese numero 2:"))

oper(num_1, num_2)
