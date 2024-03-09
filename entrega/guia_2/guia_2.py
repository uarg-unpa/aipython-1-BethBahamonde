#1. Solicite información del usuario mediante el uso de input(“Ingrese su edad: ”). Si el
#usuario tiene 18 años o más, informar: tiene edad suficiente para conducir. Si tiene
#menos de 18 años,informe la cantidad de años que faltan.


edad=int(input("Ingrese su edad: "))

print("     ----------      ")
if edad > 18 :
    print("Tiene edad suficiente para conducir.")
else:
    resultado=18-edad
    print(f"Tienes menos de 18 años. Te faltan {resultado} años.")

print("---------------------")

# 2. Compare su edad y mi edad usando if..else. ¿Quién es mayor (vos o yo)?,
# para el ingreso de la edad use input(“Ingrese su edad: ”)
# Use un condición anidada para:
# Imprimir año si la diferencia es de 1, sino años para diferencias
# mayores.
# Cuando las edades son iguales imprimir un mensaje personalizado,
# ser creativo!!

edadMayor=int(input("Ingrese la edad del Profesor: "))
print("     ----------      ")
edad=int(input("Alumno ingrese su edad: "))

print("     ----------      ")
if edad < edadMayor :
    print("El Profesor es mayor que el Alumno.")
    resultado=edadMayor-edad

    if resultado==1 :
        print(f"Un año de diferencia!!!!!")
    else:
        print(f"Años de diferencia: {resultado}")

else:
    if edad==edadMayor :
        print("Al final, lo que importa no son los años de vida, sino la vida de los años")
    
    

print("---------------------")

# 3. Solicite al usuario una contraseña, utilizando input(“Ingrese su contraseña”),
# almacene esta contraseña en una variable. Luego informar si la contraseña
# introducida coincide con la guardada sin tener en cuenta mayúsculas y
# minúsculas .


clave=input("Ingrese su contraseña para guardar: ")
print("     ---10%---     ")
print("     ---50%---      ")
print("     ---75%---      ")
print("     ---100%---      ")
contrasena=input("Ingrese su contraseña: ")

clave=clave.lower()
contrasena=contrasena.lower()

print("     ----------      ")
if clave==contrasena :
    print("coincide con la guardada sin tener en cuenta mayúsculas y  minúsculas")
    
else:
   print("no coinciden claves ingresadas")
    
    

print("---------------------")

# 4. Obtenga dos números del usuario mediante input. Si a es mayor que b, devuelve a
# es mayor que b, si a es menor que b, devuelve a es menor que b de lo contrario, a
# es igual a b.

a=int(input("Ingrese el valor de A: "))
print("     ----------      ")
b=int(input("Ingrese el valor de B: "))

print("     ----------      ")
if a > b :
    print(f" El valor de A: {a} es mayor que B: {b}")
else:
    if a < b :
       print(f" El valor de A: {a} es menor que B: {b}")
    else:
        print("A es igual a B")
    

print("---------------------")

# 5. Escriba un programa que pida al usuario un número entero e indique si es par o
# impar.


num=int(input("Ingrese un nro entero: "))
print("     ----------      ")


print("     ----------      ")
if num%2 == 0 :
    print(f" El nro: {num} es PAR.")
else:
    print(f" El nro: {num} es IMPAR")
print("---------------------")

# 6. Escriba un programa que pida al usuario un número entero del 1 al 7 y muestre por
# pantalla a qué día de la semana corresponde. Controlar que el número se encuentre
# dentro del rango [1-7], sino es así, mostrar un mensaje. Por ejemplo, si se ingresa el
# número 2 la salida debe ser martes


num = input("Ingrese un nro del [1-7]: ")
print("     ----------      ")
match num :
    case "Lunes":
        print("Es lunes")
    case "Martes":
        print("es martes")
    case "Miercoles":
        print("es miercoles")
    case "Jueves":
        print("es jueves")
    case "Viernes":
        print("es viernes")
print("---------------------")


# 7. Genere un programa que clasifique a los estudiantes según sus puntuaciones:
# ● 80-100, A
# ● 70-89, B
# ● 60-69, C
# ● 50-59, D
# ● 0-49, F

calificacion=int(input("Ingrese la puntuacion del estudiante: "))
print("     ----------      ")


print("     ----------      ")
if calificacion >= 80 and calificacion <=100 :
    print(f" La calificacion: {calificacion} es A.")
elif calificacion >=70 and calificacion <= 89:
    print(f" La calificacion: {calificacion} es B.")
elif calificacion >=60 and calificacion <= 69:
        print(f" La calificacion: {calificacion} es C.")
elif calificacion >=50 and calificacion <= 59:
            print(f" La calificacion: {calificacion} es D.")
elif calificacion >=0 and calificacion <= 49:
                 print(f" La calificacion: {calificacion} es F.")
else:
    print(f" La calificacion: {calificacion} no es valido")
    
print("---------------------")

# 8. Escriba un programa para una empresa que tiene salas de juegos para todas las
# edades y quiere calcular de forma automática el precio que debe cobrar a sus
# clientes por entrar. El programa debe preguntar al usuario la edad del cliente y
# mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis,
# si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, $10.

edad=int(input("Ingrese la edad del cliente: "))
print("     ----------      ")


print("     ----------      ")
if edad > 4 and edad <= 0:
    print(f" Edad del cliente: {edad}.","Entra gratis!!", sep="\n")
elif edad >= 4 and edad <= 18 :
    print(f" Edad del cliente: {edad}.","Debe pagar $5 ", sep="\n")
else :
    print(f" Edad del cliente: {edad}.","Debe pagar $10 ", sep="\n")

    
print("---------------------")


# 9. Para pagar un determinado impuesto se debe ser mayor de 18 años y tener ingresos
# iguales o superiores a $100000 mensuales. Escribir un programa que pregunte al
# usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene
# que pagar o no el impuesto

edad=int(input("Ingrese la edad: "))
print("     ----------      ")
ingreso=float(input("Ingrese el monto de sus ingresos mensuales: "))
print("     ----------      ")

print("     ----------      ")
if edad >= 18 and ingreso >= 100000:
    print(f" Edad del cliente: {edad}.","Debe pagar el impuesto!!!", sep="\n")
else :
    print(f" Edad del cliente: {edad}.","No debe pagar el impuesto!! ", sep="\n")

    
print("---------------------")
