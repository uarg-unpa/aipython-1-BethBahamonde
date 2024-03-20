# 5. Implementar una función que determine si dado un número este es par o impar.

def es_par(num1):
    if num1%2==0:
        print(f" El numero: {num1} es par.")
    else:
        print(f" El numero: {num1} es impar.")
    



numero=int(input("Ingrese un nro: "))
if(numero>=0):
    es_par(numero)
else:
    print("Ingreso un nro negativo, por favor vuelva intentarlo...")