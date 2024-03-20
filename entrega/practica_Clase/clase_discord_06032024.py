#rebanadas
#["A I P Y T H O N"]
#  0 1 2 3 4 5 6 7
# -  7 6 5 4 3 2 1
# oracion="AIPYTHON"
# print(oracion[3])
#acceder usando un indice negativo
#print(oracion[-1])
#cadena[inicio:fin:paso]
oracion="A veces la persona qe nadie imagina capaz de nada es la que hace cosas que nadie imagina"
#las dos primeras palabras
dos_primeras_palabras=oracion[2:7]
print(dos_primeras_palabras)

#la ultima palabra
ultima_palabra=oracion[-7:]
print(ultima_palabra)

#de tres en tres
tres_en_tres=oracion[2::3]
print(tres_en_tres)

#invertir
oracion_invertida=oracion[::-1]
print(oracion_invertida)

#in y not in
if "persona" in oracion:
    print("La palabra persona forma parte de la oracion")
elif "Persona" in oracion:
    print("La palabra Persona forma parte de la cadena ")
oracion_2="     .   ffdldldl.    "
sin_espacios=oracion_2.strip()
print(sin_espacios)