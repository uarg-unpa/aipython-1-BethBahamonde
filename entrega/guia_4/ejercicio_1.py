#1. Escribir una función que tome dos números y retorne la multiplicación entre ellos.

def multiplicacion(num1, num2):
    return num1*num2

num1=int(input("Ingrese el 1er nro: "))
num2=int(input("Ingrese el 2do nro: "))

if(num1>=0 and num2>=0):
    print( f" {num1} x {num2}= ",multiplicacion(num1,num2))
else:
    print("Ingreso un nro negativo, por favor vuelva intentarlo...")
