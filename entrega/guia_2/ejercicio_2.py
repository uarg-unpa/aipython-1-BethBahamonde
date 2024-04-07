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