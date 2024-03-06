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



