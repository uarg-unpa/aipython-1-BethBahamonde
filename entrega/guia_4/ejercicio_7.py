# 7. Escribir una función que tome tres números como entrada y retorna el máximo.

def mayor(num_1, num_2, num_3):
    return max(num_1, num_2,num_3)


maximo=0
num1=int(input("Ingrese el 1er nro: "))

num2=int(input("Ingrese el 2do nro: "))

num3=int(input("Ingrese el 3er nro: "))

print("--------------------------")
maximo=mayor(num1, num2, num3)
print(f"El mayor es: {maximo}")

