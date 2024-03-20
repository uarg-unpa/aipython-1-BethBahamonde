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