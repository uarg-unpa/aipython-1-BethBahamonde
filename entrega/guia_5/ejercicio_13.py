
# 13. Escribir una función que dada una lista de caracteres cuente la cantidad de vocales
# y retorne esa información.
lista_palabras=[]

def cant_vocales(cadena):
    contador=0
    vocal = "aeiouAEIOU"
    for texto in cadena:
        if texto in vocal:
            contador+=1
        
    return contador
#print(f"Estos son la cantidad de vocales que presenta la lista: {contador}")
 


print("Creando mi lista de palabras favoritas.")
for i in range(4):
    palabra=input("Ingrese un cadena de caracteres: ")
    lista_palabras.append(palabra)
    print("---   ---   ---   ---   ---")
print(lista_palabras)
print()
for cadena in lista_palabras:
    cantidad_de_vocales = cant_vocales(cadena)
    print(f"La palabra '{cadena}' tiene {cantidad_de_vocales} vocales.")

