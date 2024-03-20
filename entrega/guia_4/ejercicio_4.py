# 4. Escribir una función que tome un número como entrada e imprima la tabla de
# multiplicar del 1 al 10, con el siguiente formato.
#                       4 x 1 = 4
#                       …………
#                       …………

def tabla_mult(num1):
    contador=0
    while contador <=10:
        total=num1*contador
        
        print(f" {num1} x {contador} = ", total)
        contador+=1
    



numero=int(input("Ingrese un nro: "))
if(numero>=0):
    tabla_mult(numero)
else:
    print("Ingreso un nro negativo, por favor vuelva intentarlo...")

