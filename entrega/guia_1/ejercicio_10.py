
# 10. Escribir un programa que pida una temperatura en grados Celsius al usuario, realice
# la transformación de grados Celsius a Fahrenheit e imprima el resultado por pantalla.

grados=float(input("Ingrese la temperatura (C°): "))

resultadoF=(grados*9/5)+32

print("---------------------------------------------------")
print(f"De {grados} C° a {resultadoF} F°  ")
