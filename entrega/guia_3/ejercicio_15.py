# 15.Escribir un programa que pida un número entero e informe si dicho número es
# primo o no primo.

num= int(input("Ingrese un nro entero:"))
primo=True

if num>=0:
    if num <=1:
          print()
          primo= False
    else:
          for n in range(2, num):
            if num % n == 0:
                 print("No es primo", n, "es divisor")
                 primo= False
    if primo:
        print("es primo")
    else:
           print("No es nro primo")
else:
      print("No es un nro natural")  
            
