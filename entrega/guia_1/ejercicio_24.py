# 24. Usar el carácter de escape y nueva línea para separar la frase del ejercicio 22 en
# dos líneas.

cadena="El razonamiento matemático puede considerarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio"
print(f"{cadena[0:15]}",f"{cadena[16:]}", sep="\n")
