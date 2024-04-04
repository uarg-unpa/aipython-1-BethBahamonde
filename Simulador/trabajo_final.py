import random #esta linea la van a poner al principio del archivo.
# Función para lanzar un dado, como vemos nos dará un número entre 1  y el número de caras, en este caso si incluye a caras entre las posibilidades a diferencia de range.
#Si por ejemplo caras vale 6, nos dará un número entre el 1 y el 6.

def lanzar_dado(caras):
     return random.randint(1, caras)


# cant=0
lista_resultado=[]

# listas = [] #lISTA GENERAL
# lista = [] #lista especifica

# num=lanzar_dado(10)
# print(num)
def crear_Dado():
    cant_dados=int(input("Ingrese la cantidad de dados: "))
    cant_caras=int(input("Ingrese la cantidad de caras: "))
    
    listas = []
    for i in range(cant_dados):
        lista = []
        for j in range(1, cant_caras+1):
            lista.append(j)
        listas.append(lista)
     # Imprimir las listas

    print("Se creo con exito!!!!!!!!")
    print()
    for i, lista in enumerate(listas):
        print(f"Dado {i + 1}: {lista}")
    print()
    mostrar_juego(cant_caras, cant_dados)



          
def mostrar_juego(caras, dados):
    cant=0
    op1=0

    
    while True :
        mostrar_menuJuego()
        op1=int(input("Elija una opcion: "))

        if op1 >= 1 and op1 <=4 :
            if op1 == 1:
                tirada=int(input("Ingrese la cantidad de veces que tirara los dados: "))
                
                cant+=tirada
                # for i in range(cant):
                #     num=lanzar_dado(caras)
                #     lista_resultado.append(num)


                listas_1 = []
                for i in range(dados):
                    lista_2 = []
                    for j in range(tirada):
                        num=lanzar_dado(caras)
                        lista_2.append(num)
                        lista_resultado.append(num)
                    
                    listas_1.append(lista_2)


                print()
                print("Lista de resultados de los dados: ")


                print("Jugando!!!!!!!!")
                print()
                for i, lista_2 in enumerate(listas_1):
                    print(f"Dado {i + 1}: {lista_2}")


                # print(lista_resultado)
                print()    
                
            elif op1 == 2:
                print(cant)
            elif op1 == 3:
                print("Los valores de los dados son: ")
                print(lista_resultado)
                print()    
        elif op1 == 0:
                print("Adios vuelva pronto!!")
                break
        elif op1!= 0 and op1 >= 5:
                print(f"Parece que {op1} aun no esta definida entre las opciones \nprobemos de nuevo !!")
                continue

def mostrar_menuJuego():
    print("--------- Juego de Dados  ----------------------")
    print(f"1: Tirar dados. ")
    print(f"2: Cantidad tiros hechos. ")
    print(f"3: Mostrar todos los valores de los dados que ya salieron. ")
    
    print()
    print(f"0: Salir ")
    print("-----------------------------------------------------------")
    print()

def mostrar_menu():
    print()
    print("--------- Menu de Simulacion de Dados  ----------------------")
    print(f"1:  Crear dados. (Nueva Partida) ")
    print(f"2: Estadisticas. (Segun generala= 5 dados) ")
    print(f"3: idem (Segun Farkle = 6 dados) (El Craps- Pase inglés)")
    print(f"4: c. ... ")
    print()
    print(f"0: Salir ")
    print("-----------------------------------------------------------")
    print()
    
    

op=0

while True :
    mostrar_menu()
    op=int(input("Ingrese la opcion para operar con los numeros: "))
    if op >= 1 and op <=4 :
        if op == 1:
            print()
            crear_Dado()
            
        #     num_listas = 5
        #     cant_dados=int(input("Ingrese la cantidad de dados: "))
        #     cant_caras=int(input("Ingrese la cantidad de caras: "))
        #     listas = []
        #     for i in range(cant_dados):
        #             lista = []
        #             for j in range(1, cant_caras+1):
        #                 lista.append(j )
        #             listas.append(lista)
        #   # Imprimir las listas
        #     for i, lista in enumerate(listas):
        #        print(f"Dado {i + 1}: {lista}")

          #   for i in range(cant_dados):
          #      i=crear_Dado()
          #       compania=input("Ingrese el nombre de una compania: ")
          #       lista.append(compania)
          #       print("---   ---   ---   ---   ---")
          #   print(lista)

        elif op == 2:
            # print("Los valores de los dados son: ")
            
            # print()
            # print(f"La cantidad de tiros que se hizo: ", cant)
            print(f"La cantidad de puntos: ")
            print(lista_resultado)
           # crear la suma de todos y dividirlo por la cantidad de dados
        
          #       print()
               # for i in range(len(lista)):
               #  print(lista[i])
            # print("Lista modificada: ")
            # print(lista_frutas)
          
                    #print(f"      ({i})     ")
                #print(lista_frutas)


        elif op == 4:
            print()
            # num=int(input("Indique cual compañia desea modificar: "))
            # cadena=input("Ingrese el nombre de la compañia a cambiar: ")
            # lista[num]=cadena
            # print("Lista modificada!!!!")
            # print(lista)

    elif op == 0 :
        print("Adios vuelva pronto!!")
        break
    elif op!= 0 and op >= 5:
        print(f"Parece que {op} aun no esta definida entre las opciones \nprobemos de nuevo !!")
        continue  