# 11. Escribir un programa que pregunte al usuario por el número de horas trabajadas y el
# costo por hora. Después debe mostrar por pantalla el sueldo que le corresponde.


print("-----------  Calculo del Sueldo  ------------------")
hsTrabajadas=int(input("Ingrese el nro de hs trabajadas: "))
costo=int(input("Ingrese el costo por hs: "))

total=hsTrabajadas*costo

print("---------------------------------------------------")
print("El sueldo es: ", total)
