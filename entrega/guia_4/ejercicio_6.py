# 6. Crear una función que calcule el factorial de un número.

def factorial(num1):
    factorial=1
    i=1
    while i<num1:
        factorial=factorial*1
        i=i+1
    print(f"El factorial de {num1}! es: {factorial}")

num=int(input("Ingrese un numero: "))
factorial(num)