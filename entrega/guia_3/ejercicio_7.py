# 7. Escribir un programa que pregunte el nombre de usuario y un número entero
# e imprima en diferentes líneas el nombre de usuario tantas veces como el
# número introducido.

nombre=str(input("Ingrese su nombre: "))
num= int(input("Ingrese un nro entero para repetir:"))


for i in range(num):
    print(f"{nombre}",sep="\n")
    print(" --- --- --- ---  ")
print(f"La cantidad ingresada: {num} repetir")