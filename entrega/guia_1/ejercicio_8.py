
# 8. Se desea conocer el perímetro y el área de un rectángulo según su base y altura.
# Así mismo también se desean conocer los mismos datos para una circunferencia
# según su radio.
import math

base=float(input("Ingrese la base: "))
altura=float(input("Ingrese la altura: "))
radio=float(input("Ingrese el radio: "))

perimetro=2*(base+altura)
area=base*altura
circunsferencia=math.pi * radio**2

print("---------------------------------------------------")
print("El resultado del perimetro es: ", perimetro)
print("El resultado del area es: ", area)
print("El resultado del circunsferencia es: ", circunsferencia)
