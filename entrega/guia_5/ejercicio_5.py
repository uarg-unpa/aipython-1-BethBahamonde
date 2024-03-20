# 5. Dada una lista mostrar el primer elemento, el del medio y el último.

def mostrar_menu():
    print()
    print("--------- Menu de la Lista de Frutas  ----------------------")
    print(f"1: Mostrar el 1er elemento. ")
    print(f"2: Mostrar el del medio. ")
    print(f"3: Mostrar el ultimo elemento. ")
    print(f"4: Imprimir Lista. ")
    print()
    print(f"0: Para Finalizar ")
    print("-----------------------------------------------------------")
    print()
    
    

lista_frutas=['Manzana Roja', 'Manzana Verde', 'Frutilla', 'Kiwi', 'Banana', 'Cereza', 'Frambuesa' ]

print(lista_frutas)

op=0
i=0

while True :
    mostrar_menu()
    op=int(input("Ingrese la opcion para operar con los numeros: "))
    if op >= 1 and op <=3 :
        if op == 1:
            print()
            print(f"El primer elemento de la lista es: {lista_frutas[0]}")
        elif op == 2:
            print()
            i = len(lista_frutas) // 2
            cadena= lista_frutas[i]
            print(f"El elemento del medio de la lista es: {cadena}")
            # print("Lista modificada: ")
            # print(lista_frutas)

        elif op == 3:
                print()
                print(f"El ultimo elemento de la lista es: {lista_frutas[-1]}")
                #print(lista_frutas)
        elif op == 4:
            print()
            print(lista_frutas)

    elif op == 0 :
        print("Adios vuelva pronto!!")
        break
    elif op!= 0 and op >= 4:
        print(f"Parece que {op} aun no esta definida entre las opciones \nprobemos de nuevo !!")
        continue  

