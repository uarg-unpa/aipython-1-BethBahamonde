
# 9. Crear una lista de letras (‘a’ hasta ‘j’)
# a. Imprima cada segundo elemento usando rebanadas.

# Crear una lista vacía para almacenar las letras del abecedario
lista_letras = []

# Iterar sobre los códigos Unicode de las letras minúsculas del alfabeto (97 a 122)
for codigo in range(65, 75):
    #for codigo in range(97, 123):
    # Convertir el código Unicode en el carácter correspondiente y agregarlo a la lista
    lista_letras.append(chr(codigo))

# Imprimir la lista resultante
print(lista_letras)


#a. Imprima cada segundo elemento usando rebanadas.
lista_alternados=lista_letras[1::2]
print(lista_alternados)