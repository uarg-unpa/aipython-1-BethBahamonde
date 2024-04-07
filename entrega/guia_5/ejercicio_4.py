# 4. Crear una lista de tus frutas favoritas

def mostrar_menu():
    print()
    print("--------- Menu de la Lista de Frutas  ----------------------")
    print(f"1: Imprimir la longitud. ")
    print(f"2: Eliminar el primer elemento de la lista. ")
    print(f"3: Agregar un elemento al final de la lista. ")
    print(f"4: Imprimir los resultados anteriores. ")
    print()
    print(f"0: Para Finalizar ")
    print("-----------------------------------------------------------")
    print()
    
    

lista_frutas=['Manzana Roja', 'Manzana Verde', 'Frutilla', 'Kiwi', 'Banana', 'Cereza', 'Frambuesa' ]

print(lista_frutas)

op=0

while True :
    mostrar_menu()
    op=int(input("Ingrese la opcion para operar con los numeros: "))
    if op >= 1 and op <=4 :
        if op == 1:
            print()
            print(f"La longitud de la lista es: {len(lista_frutas)}")
        elif op == 2:
            print()
            lista_frutas = lista_frutas[1:]
            print(f"Se elimino el 1er elemento: {lista_frutas[0]} .")
            # print("Lista modificada: ")
            # print(lista_frutas)

        elif op == 3:
                print()
                cadena=input("Ingrese el nombre del elemento: ")
                lista_frutas.append(cadena)
                print("  ---   ---   ---   ---   ---   ---   ")
                print(f"Se agrego exitosamente!!!")
                #print(lista_frutas)


        elif op == 4:
            print()
            print(lista_frutas)

    elif op == 0 :
        print("Adios vuelva pronto!!")
        break
    elif op!= 0 and op >= 5:
        print(f"Parece que {op} aun no esta definida entre las opciones \nprobemos de nuevo !!")
        continue  
