# 13.Construir un programa que lea un número natural N y calcule la suma de los
# primeros N números pares.

num= int(input("Ingrese un nro entero:"))
total=0
if num>= 1:
    for i in range(1,num+1):
        
        if i!=num:
            if i%2 == 0:
                # print(f" {i} ", end="")
                # print("+ ")
                total+=i
        elif i == num:
            if i%2 == 0:
                total+=i
                # print(f" {i} = {total}", end="" )
                print(f"La suma de los primeros N nros pares: {total} ")
            else:
               print(f"La suma de los primeros N nros pares: {total} ")
    # print(f"{total}")
else:
    print("El numero ingresado no es un nro Natural.")