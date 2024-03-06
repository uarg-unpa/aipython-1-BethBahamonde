

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
# 13. Escribir un programa que calcule el promedio de precios de 10 productos
print("-----------  Calculo del promedio de precios (10 produ)  ------------------")
producto1=float(input("Ingrese el precio del 1er producto: "))
producto2=float(input("Ingrese el precio del 2do producto: "))
producto3=float(input("Ingrese el precio del 3ero producto: "))
producto4=float(input("Ingrese el precio del 4to producto: "))
producto5=float(input("Ingrese el precio del 5to producto: "))
producto6=float(input("Ingrese el precio del 6to producto: "))
producto7=float(input("Ingrese el precio del 7mo producto: "))
producto8=float(input("Ingrese el precio del 8vo producto: "))
producto9=float(input("Ingrese el precio del 9no producto: "))
producto10=float(input("Ingrese el precio del 10mo producto: "))

suma=(producto1 + producto2 + producto3 + producto4 + producto5 + producto6 + producto7 + producto8 + producto9 + producto10)
promedio=suma/10

print("---------------------------------------------------")
print("El promedio de precios de 10 productos es: ", promedio)

# 14. Concatenar el string ‘Una ambiciosa’, ‘Introducción’, ‘a Python’, ‘Parte 1’.
print('Una ambiciosa'+' '+'Introducción'+' '+'a Python'+' '+'Parte 1')


# 15. Inicializar una variable llamada sociedad con el valor inicial de ‘aiPython P1’
# a. Imprimir la variable utilizando print()
texto="EsTo eS uN texTo MeZclAdO"
print(texto)
# b. Imprimir la longitud de la variable sociedad usando len() y print()
print(len(texto))
# c. Cambiar todos los caracteres a mayúsculas usando el método upper()
print(texto.upper())
# d. Cambiar todos los caracteres a minúsculas usando el método lower()
print(texto.lower())


# 16. Usar los métodos capitalize(), title(), swapcase() para formatear el valor del string
# “sometimes it is the people no one imagines anything of who do the things that no
# one can imagine.”

texto="sometimes it is the people no one imagines anything of who do the things that no one can imagine"

print("Con capitalize() ")
print(texto.capitalize())
print("   -------    ")
print("Con title() ")
print(texto.title())
print("   -------    ")
print("Con swapcase() ")
print(texto.swapcase())
print("   -------    ")


# 17. Escribir un programa que pregunte el nombre completo del usuario y después
# muestre por pantalla el nombre completo del usuario tres veces.

nombreCompleto=input("Ingrese el nombre completo")
print(nombreCompleto*3)

# 18. Hacer más grande el árbol, conservando proporciones.
print("              *")
print("             * *")
print("            *   *")
print("           *     *")
print("          *       *")
print("         *         *")
print("        *           *")
print("       *             *")
print("      *               *")
print("     *                 *")
print("    *                   *")
print("   *                     *")
print("  *                       *")
print(" *                         *")
print("*                           *")
print("  *                     *")
print("  *                     *")
print("  *                     *")
print("  *                     *")
print("  *                     *")
print("   *********************")

# 19. Utilizar un solo print y /n para dibujar el mismo árbol.

print("\t              *","             * *","            *   *","           *     *","          *       *","         *         *","        *           *","       *             *","      *               *","     *                 *","    *                   *","   *                     *","  *                       *"," *                         *","*                           *","  *                     *","  *                     *","  *                     *","  *                     *","   *********************",sep="\t\n\t")

print("              *","             * *","            *   *","           *     *","          *       *","         *         *","        *           *","       *             *","      *               *","     *                 *","    *                   *","   *                     *","  *                       *"," *                         *","*                           *","  *                     *","  *                     *","  *                     *","  *                     *","   *********************",sep="\n")



# 20. Dibujar dos árboles uno al lado del otro.

print("    *          *","   * *        * *","  *   *      *   *"," *     *    *     *","*       *  *       *","  *   *      *   *","  *   *      *   *","   ***        ***",sep="\n")

# 21. Escribir un programa que pida una palabra al usuario y reemplace todas las letras
# "a" por 😃 y muestre el resultado por pantalla.

palabra=input("Ingrese una palabra: ")

print(palabra.replace("a","😃"))

# 22. Cortar las dos primeras palabras de la frase ‘’El razonamiento matemático puede
# considerarse más bien esquemáticamente como el ejercicio de una combinación de
# dos instalaciones, que podemos llamar la intuición y el ingenio”.


cadena="El razonamiento matemático puede considerarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio"
#print(len(cadena))
print(cadena[:15],cadena[15:175], sep="\n")

# 23. Remover los espacios en blanco del principio y final de la siguiente frase, “ La
# ciencia es una ecuación diferencial. La religión es una condición de frontera. “

cadena="    La ciencia es una ecuación diferencial. La religión es una condición de frontera.   "
print(len(cadena))
print(cadena[4:85])


# 24. Usar el carácter de escape y nueva línea para separar la frase del ejercicio 22 en
# dos líneas.

cadena="    La ciencia es una ecuación diferencial. La religión es una condición de frontera.   "
print(len(cadena))
print(cadena.split())
