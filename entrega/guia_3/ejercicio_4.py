# 4. Escribir un programa que pida al usuario dos números enteros e imprima todos los
# números entre ellos.

num1=int(input("Ingrese el 1er numero: "))
print("     ----------      ")
num2=int(input("Ingrese el 2do numero: "))
print("     ----------      ")

if num1 > num2:
    for n in range(num2+1,num1):
        print(n,end="-")
elif num1 < num2:
    for n in range(num1+1,num2):
        print(n,end="-")
else:
    print(f"Los valores son: {num1} y {num2}",end="-")
print("-")
