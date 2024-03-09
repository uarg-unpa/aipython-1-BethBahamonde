# 1.Iterar de 0 a 100 usando un bucle while y mostrar dichos números.

contador=0
while contador <= 100 :
    print(contador)
    contador=contador+1
print("-")

# 2. Tomar el ejercicio 1 y realizarlo con un bucle for, tip usar range. los números deben
# salir uno al lado del otro.

for contador in range(101) :
    print(contador, end="-")

print("")


# 3. Iterar de 10 a 0 usando un bucle while y un bucle for.

contador=10
while contador >= 0 :
    for i in range(contador,-1,-1):
        print(i,end="-")
    contador=-1
print("-")

# 4. Escribir un programa que pida al usuario dos números enteros e imprima todos los
# números entre ellos.

num1=int(input("Ingrese el 1er numero: "))
print("     ----------      ")
num2=int(input("Ingrese el 2do numero: "))
print("     ----------      ")

if num1 > num2:
    for n in range(num2+1,num1):
        print(n,end="-")
elif num1 < num2:
    for n in range(num1+1,num2):
        print(n,end="-")
else:
    print(f"Los valores son: {num1} y {num2}",end="-")
print("-")


# 5. Escribe un bucle que haga siete llamadas a print(), de modo que obtengamos
# en la salida el siguiente triángulo:
# #
# ##
# ###
# ####
# #####
# ######
# #######

for i in range(8):
    print("#"*i)


# 6. Usar bucles anidados para mostrar la siguiente figura
# ########
# ########
# ########
# ########
# ########
# ########
# ########
# ########
    
# 7. Escribir un programa que pregunte el nombre de usuario y un número entero
# e imprima en diferentes líneas el nombre de usuario tantas veces como el
# número introducido.
# 8. Escribir un programa que pida un número entero positivo mayor a 3 y muestre
# por pantalla todos los números impares desde 1 hasta ese número.
# 9. Escribir un programa que permita mostrar el siguiente patrón:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
    
# 10. Escribir un programa que imprima todas las fichas del domino, una por línea,
# sin repetir. Como se muestra a continuación
# 0 0
# 0 1
# 0 2
# 0 3
# 0 4
# 0 5
# 0 6
# ...
    
# 11. Escribir un programa que pida al usuario un número entero y muestre por
# pantalla un triángulo rectángulo como el que se muestra
# Si se ingresa el número 9, el resultado será
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1
    

# 12. Escribir un programa que pida un número natural N al usuario e imprima por
# pantalla la suma de los números naturales de 1 hasta N.
# Por ejemplo para N = 5, la salida debe ser:
# 1 + 2 + 3 + 4 + 5 = 15
    
# 13.Construir un programa que lea un número natural N y calcule la suma de los
# primeros N números pares.
    
# 14.Escribir un programa que recibe como entrada desde el usuario dos números
# enteros e imprimir todos los números pares entre ellos.
    
# 15.Escribir un programa que pida un número entero e informe si dicho número es
# primo o no primo.
