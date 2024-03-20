
# 4. Obtenga dos números del usuario mediante input. Si a es mayor que b, devuelve a
# es mayor que b, si a es menor que b, devuelve a es menor que b de lo contrario, a
# es igual a b.

a=int(input("Ingrese el valor de A: "))
print("     ----------      ")
b=int(input("Ingrese el valor de B: "))

print("     ----------      ")
if a > b :
    print(f" El valor de A: {a} es mayor que B: {b}")
else:
    if a < b :
       print(f" El valor de A: {a} es menor que B: {b}")
    else:
        print("A es igual a B")
    

print("---------------------")