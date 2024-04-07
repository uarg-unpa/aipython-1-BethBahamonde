import random #esta linea la van a poner al principio del archivo.
# Función para lanzar un dado, como vemos nos dará un número entre 1  y el número de caras, en este caso si incluye a caras entre las posibilidades a diferencia de range.
#Si por ejemplo caras vale 6, nos dará un número entre el 1 y el 6.

def lanzar_dado(caras):
     return random.randint(1, caras)


lista_resultado=[]


def crear_Dado():
    cant_dados=int(input("Ingrese la cantidad de dados: "))
    cant_caras=int(input("Ingrese la cantidad de caras: "))
    
    listas = []
    for i in range(cant_dados):
        lista = []
        for j in range(1, cant_caras+1):
            lista.append(j)
        listas.append(lista)

    print("Se creo con exito!!!!!!!!")
    print()
    for i, lista in enumerate(listas):
        print(f"Dado {i + 1}: {lista}")
    print()
    mostrar_juego(cant_caras, cant_dados)

def suma():
    suma=0;
    for i in range(len(lista_resultado)):
        suma+=lista_resultado[i]
    return suma


          
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

                print()    
                
            elif op1 == 2:
                print(f"La cantidad de tiros es: ", cant)
            elif op1 == 3:
                print("Los valores de los dados son: ")
                print(lista_resultado)
                print()    
            elif op1 == 4:
                
                print(f"La cantidad de puntos: ")
                print(lista_resultado)
                print("--------")
                resultado=suma()
                promedio=resultado/cant
                print(f"El promedio es: ",promedio)
                
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
    print(f"4: Promedio cantidad de puntos de los dados.")
    
    print()
    print(f"0: Salir ")
    print("-----------------------------------------------------------")
    print()

def mostrar_menu():
    print()
    print("--------- Menu de Simulacion de Dados  ----------------------")
    print(f"1: Crear dados. (Nueva Partida) ")
    

    print()
    print(f"0: Salir ")
    print("-----------------------------------------------------------")
    print()
    
    

op=0

while True :
    mostrar_menu()
    op=int(input("Ingrese la opcion para operar con los numeros: "))
    if op >= 1 and op <=2 :
        if op == 1:
            print()
            crear_Dado()
            
        elif op == 2:
           print(f"La mejor partida es: ")
            

           
    elif op == 0 :
        print("Adios vuelva pronto!!")
        break
    elif op!= 0 and op >= 3:
        print(f"Parece que {op} aun no esta definida entre las opciones \nprobemos de nuevo !!")
        continue  