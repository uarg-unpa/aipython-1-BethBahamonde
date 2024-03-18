
# 11. Crear una lista de tus palabras favoritas
# a. Extraer una sub lista conteniendo desde la segunda hasta la cuarta palabra.
lista_palabrasFavoritas=[]
print("Creando mi lista de palabras favoritas.")
for i in range(8):
    palabra=input("Ingrese una palabra Favorita: ")
    lista_palabrasFavoritas.append(palabra)
    print("---   ---   ---   ---   ---")
print(lista_palabrasFavoritas)

miniLista=lista_palabrasFavoritas[1:5]
print(miniLista)
