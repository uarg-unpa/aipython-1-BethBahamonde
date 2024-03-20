# 14.Escribir un programa que recibe como entrada desde el usuario dos números
# enteros e imprimir todos los números pares entre ellos.

num1= int(input("Ingrese el 1er nro entero:"))

num2= int(input("Ingrese el 2do nro entero:"))

if num1>=0 and num2>=0:
    if num1 > num2:
        for n in range(num2+1,num1):
            if n%2==0:
                print(n,end="-")
    elif num1 < num2:
        for n in range(num1+1,num2):
            if n%2==0:
                print(n,end="-")
    elif num1 == num2:
        print(f"Los valores son iguales: {num1} y {num2}",end="-")
else:
    print("No es nro entero")

