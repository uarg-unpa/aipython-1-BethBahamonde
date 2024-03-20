# 11. Escribir un programa que pida al usuario un número entero y muestre por
# pantalla un triángulo rectángulo como el que se muestra
# Si se ingresa el número 9, el resultado será
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

num= int(input("Ingrese un nro entero:"))

for i in range(1,num+1,2):
    # print(f"i: {i}")
    for j in range(i,0, -2):
        # print(f"j: {j}"):
            print(j, end=" ")
    print()