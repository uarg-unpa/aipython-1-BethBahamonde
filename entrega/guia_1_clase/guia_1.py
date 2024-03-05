

#Ejercicio 1
#a
print("Las máquinas me sorprenden con mucha frecuencia.")

#b
print()

#c
print("Dia ventoso")

#d
print(23)
print("23")
#Sucedio que te muestra ambos nros pero con la diferencia que uno es de tipo entero y el otro una cadena

#e
print('Una computadora puede ser llamada "inteligente" si logra engañar a una persona haciéndole creer que es un humano.')

#f
print("Yohana","Bahamonde","27")

#g
print("Yohana","Bahamonde","27" ,sep="_")

#h
print("calle","numero","codigo postal",sep="\t")

#i
print("calle","numero","codigo postal",sep="\n")

#j
print("Feliz","Primavera","\t\t2024",sep="\t\n\t")

#k
print("Solo podemos ver poco del futuro", end=",")
print(" pero lo suficiente para darnos cuenta de que hay mucho que hacer")

#l
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

#Ejercicio 2
#@BethBahamonde ➜ /workspaces/aipython-1-BethBahamonde (main) $ python
#Python 3.10.13 (main, Feb  6 2024, 19:53:26) [GCC 9.4.0] on linux
#Type "help", "copyright", "credits" or "license" for more information.
# >>> 5+7
# 12
# >>> 0-9
# -9
# >>> 2*45
# 90
# >>> 3/2
# 1.5
# >>> 6**2
# 36
# >>> 3//2
# 1
# >>> x=1
# >>> x^2+6x+9
#   File "<stdin>", line 1
#     x^2+6x+9
#         ^
# SyntaxError: invalid decimal literal
# >>> x^2+6*x+9
# 16

#Ejercicio 3
#3. Definir nombres variables representativos para las siguientes características:
# a. tu nombre
nombre="Yohana"
# b. tu apellido
apellido="Bahamonde"
# c. tu edad
edad=27
# d. tu altura
altura=1.70
# e. un número de vuelo
nro_vuelo="#2457"
# f. La temperatura del ambiente
temp=18
# g. El salario mensual.
salario=15000
# h. Para representar que el juego termino
resultado="juego terminado "
# i. Para determinar si un número es par
esPar=True

#4. En base a la definición de las variables del ejercicio 3, ¿ Puedes mencionar con qué literales se asocian?
print(type(nombre))
print(type(apellido))
print(type(edad))
print(type(altura))
print(type(nro_vuelo))
print(type(temp))
print(type(salario))
print(type(resultado))
print(type(esPar))

# 5. Utilizando la función input
# a. Crear un programa que imprima un mensaje (usar función print) solicitando, el nombre, el apellido y la edad desde la terminal y luego darle un mensaje ,“ser creativo”, utilizando los tres datos ingresados.
nombre=input("Ingrese nombre: ")
apellido=input("Ingrese apellido: ")
edad=input("Ingrese edad: ")
print(nombre,apellido,edad,sep="\n")

# b. Modificar el ejercicio anterior para no utilizar la función print para mostrar el mensaje al solicitar los datos. Tip pasarle el argumento a la función input.
input(nombre+apellido+edad)


#6. Crear un programa que solicite dos números enteros, luego realizar:
num1=int(input("Ingrese el 1er nro: "))
num2=int(input("Ingrese el 2do nro: "))
# a. suma
print(f"{num1}+{num2}={num1+num2}")
# b. resta
print(f"{num1}-{num2}={num1-num2}")
# c. el producto
print(f"{num1}*{num2}={num1*num2}")
# d. la potencia
print(f"{num1}**{num2}={num1**num2}")
# e. el resto
print(f"{num1}%{num2}={num1%num2}")



#7.Modificar el ejercicio 6 para que reciba un entero y un float.
num1=int(input("Ingrese el 1er nro entero: "))
num2=float(input("Ingrese el 2do nro con coma: "))
# a. suma
print(f"{num1}+{num2}={num1+num2}")
# b. resta
print(f"{num1}-{num2}={num1-num2}")
# c. el producto
print(f"{num1}*{num2}={num1*num2}")
# d. la potencia
print(f"{num1}**{num2}={num1**num2}")
# e. el resto
print(f"{num1}%{num2}={num1%num2}")


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

# 10. Escribir un programa que pida una temperatura en grados Celsius al usuario, realice
# la transformación de grados Celsius a Fahrenheit e imprima el resultado por pantalla.

grados=float(input("Ingrese la temperatura (C°): "))

resultadoF=(grados*9/5)+32

print("---------------------------------------------------")
print(f"De {grados} C° a {resultadoF} F°  ")

# 11. Escribir un programa que pregunte al usuario por el número de horas trabajadas y el
# costo por hora. Después debe mostrar por pantalla el sueldo que le corresponde.


print("-----------  Calculo del Sueldo  ------------------")
hsTrabajadas=int(input("Ingrese el nro de hs trabajadas: "))
costo=int(input("Ingrese el costo por hs: "))

total=hsTrabajadas*costo

print("---------------------------------------------------")
print("El sueldo es: ", total)

# 12. Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
# y el número de años, y muestre por pantalla el capital obtenido en la inversión.

print("-----------  Calculo de inversion  ------------------")
inversion=float(input("Ingrese la cantidad a invertir: "))
interes=float(input("Ingrese el interes anual: "))
tiempo=int(input("Ingrese la cantidad de años: "))

total=inversion*interes*tiempo

print("---------------------------------------------------")
print("El capital obtenido en la inversión es: ", total)

# 13. Escribir un programa que calcule el promedio de precios de 10 productos.
