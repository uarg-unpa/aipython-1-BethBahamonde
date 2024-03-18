# 15. Implementar una función que tome una lista de números y retorna el promedio de
# sus elementos.
def calculo_promedio(lista):
    suma=0
    total=0
    cant=0
    promedio=0
    dim=len(lista)
    for i in range(dim):
        suma+=lista[i]
        cant+=1
    print(suma)
    print(cant)
    promedio=float(suma//cant)
    return promedio

lista_aux=[1, 2, 3, 4, 5, 6]
print(calculo_promedio(lista_aux))