print("usando la funcion"+"print()")
print("usando la funcion print()"*3)

#Argumentos Posicionales
print(10,3.14,"Cadena", True)

edad=int(input("Ingrese su edad:"));
#print("su edad es:"+edad) esta mal
print("su edad es:", edad)
print("2-Su edad es: "+str(edad))


num1=4
num2=6
print(f"{num1}+{num2}={num1+num2}")
print(f"{num1}-{num2}={num1-num2}")
print(f"{num1}*{num2}={num1*num2}")
print(f"{num1}%{num2}={num1%num2}")
print(f"{num1}/{num2}={num1/num2}")
print(f"{num1}//{num2}={num1//num2}")
print(f"{num1}**{num2}={num1**num2}")

suma=f"{num1}+{num2}={num1+num2}"
print("suma: ", suma)

#
texto="eStO eS uN tExTo MeZcLaDo"
print(texto.title())
print(texto)
texto=texto.title()
print(texto)

#upper  lower
print(texto.upper())
print(texto.lower())

# replace
print(texto.replace(" ","-"))



