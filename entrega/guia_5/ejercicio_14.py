# 14. Escribir una función que tome dos listas como parámetros y las intercale en una
# nueva, retornar la nueva lista resultante.


def lista_intercalada(lista_1, lista_2):
    lista=[]
    dim_max=max(len(lista_1), len(lista_2))
    for i in range(dim_max):
        if(i < len(lista_2)):
            lista.append(lista_2[i])
        if (i < len(lista_1)):
            lista.append(lista_1[i])

    return lista

lista_a=[0,1,2,3,4]
#print(lista)
lista_b=[10,20,30,40,50]

print(f'{lista_intercalada(lista_a,lista_b)}')