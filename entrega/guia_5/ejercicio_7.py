# 7. Almacenar los nombres de tus compañías favoritas en una lista.

lista=[]

def mostrar_menu():
    print()
    print("--------- Menu de la Lista de Frutas  ----------------------")
    print(f"1: 7. Almacenar los nombres de tus compañías favoritas en una lista. ")
    print(f"2: a. Recorrer la lista del ejercicio 7 y mostrar los datos con print ")
    print(f"3: b. Recorrer la lista del ejercicio 7 y mostrar el índice más el nombre de la compañía. ")
    print(f"4: c. Modificar alguna/as de las compañía/s de la lista del ejercicio 7 y luego mostrar la lista. ")
    print()
    print(f"0: Para Finalizar ")
    print("-----------------------------------------------------------")
    print()
    
    

op=0

while True :
    mostrar_menu()
    op=int(input("Ingrese la opcion para operar con los numeros: "))
    if op >= 1 and op <=4 :
        if op == 1:
            print()
            
            for i in range(4):
                compania=input("Ingrese el nombre de una compania: ")
                lista.append(compania)
                print("---   ---   ---   ---   ---")
            print(lista)

        elif op == 2:
            print()
            for i in range(len(lista)):
                print(lista[i])
            # print("Lista modificada: ")
            # print(lista_frutas)

        elif op == 3:
                print()
                for i in range(len(lista)):
                    print( f"({i})", f"[_ {lista[i]} _]")
                    #print(f"      ({i})     ")
                #print(lista_frutas)


        elif op == 4:
            print()
            num=int(input("Indique cual compañia desea modificar: "))
            cadena=input("Ingrese el nombre de la compañia a cambiar: ")
            lista[num]=cadena
            print("Lista modificada!!!!")
            print(lista)

    elif op == 0 :
        print("Adios vuelva pronto!!")
        break
    elif op!= 0 and op >= 5:
        print(f"Parece que {op} aun no esta definida entre las opciones \nprobemos de nuevo !!")
        continue  