
# 9. Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
# calcule el índice de masa corporal y lo almacene en una variable. Luego debe
# mostrar por pantalla la frase: "Tu índice de masa corporal es: <imc>". Donde <imc>
# es el índice de masa corporal calculado. Tip. buscar en google cómo calcular el IMC.

import math

peso=float(input("Ingrese su peso (kg): "))
estatura=float(input("Ingrese su estatura (m): "))

indiceMasaCorporal=round(peso/math.pow(estatura,2),1)

print("---------------------------------------------------")
print("El resultado del IMC es: ", indiceMasaCorporal)
