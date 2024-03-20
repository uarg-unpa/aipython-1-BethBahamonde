
# 12. Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
# y el número de años, y muestre por pantalla el capital obtenido en la inversión.

print("-----------  Calculo de inversion  ------------------")
inversion=float(input("Ingrese la cantidad a invertir: "))
interes=float(input("Ingrese el interes anual: "))
tiempo=int(input("Ingrese la cantidad de años: "))

total=inversion*interes*tiempo

print("---------------------------------------------------")
print("El capital obtenido en la inversión es: ", total)
