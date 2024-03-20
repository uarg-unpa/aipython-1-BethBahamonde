
# 9. Para pagar un determinado impuesto se debe ser mayor de 18 años y tener ingresos
# iguales o superiores a $100000 mensuales. Escribir un programa que pregunte al
# usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene
# que pagar o no el impuesto

edad=int(input("Ingrese la edad: "))
print("     ----------      ")
ingreso=float(input("Ingrese el monto de sus ingresos mensuales: "))
print("     ----------      ")

print("     ----------      ")
if edad >= 18 and ingreso >= 100000:
    print(f" Edad del cliente: {edad}.","Debe pagar el impuesto!!!", sep="\n")
else :
    print(f" Edad del cliente: {edad}.","No debe pagar el impuesto!! ", sep="\n")

    
print("---------------------")