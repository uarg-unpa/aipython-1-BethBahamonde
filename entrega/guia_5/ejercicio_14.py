# 14. Escribir una función que tome dos listas como parámetros y las intercale en una
# nueva, retornar la nueva lista resultante.
lista=[]

def lista_intercalada(lista_1, lista_2):
    i=0
    j=0
    dim=len(lista_1)+len(lista_2)
    print(dim)
    while i <= dim:# or i==j:
        if i != len(lista_1):
            #cadena=lista_1[i]
            lista.append(lista_1[i])
            print(lista)
            i+=1
            lista.append(lista_2[j])
            print(lista)
            j+=1
            i+=1
            print(i)
        else:
            lista.append(lista_2[j])
            print(lista)
            j+=1
            i+=1
            print(i)

    print(lista)

lista_a=[0,1,2,3,4]
print(lista)
lista_b=[10,20,30,40,50]

lista_intercalada(lista_a,lista_b)