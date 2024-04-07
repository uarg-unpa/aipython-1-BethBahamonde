# 8. Escribir un programa que pida un número entero positivo mayor a 3 y muestre
# por pantalla todos los números impares desde 1 hasta ese número.

num= int(input("Ingrese un nro entero: "))


for i in range(num):
    if num>=3:
        if i%2 == 1 :
            print(f"impar {i}",sep="\n")
    else:
        print("No es mayor a 3")
    
