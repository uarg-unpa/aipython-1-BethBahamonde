# 12. Escribir un programa que pida un número natural N al usuario e imprima por
# pantalla la suma de los números naturales de 1 hasta N.
# Por ejemplo para N = 5, la salida debe ser:
# 1 + 2 + 3 + 4 + 5 = 15

num= int(input("Ingrese un nro entero:"))
total=0
if num>= 1:
    for i in range(1,num+1):
        
        total+=i
        if i!=num:
            print(f" {i} ", end="+")
        elif i == num:
            print(f" {i} = ", end="" )
    print(f"{total}")
else:
    print("El numero ingresado no es un nro Natural.")