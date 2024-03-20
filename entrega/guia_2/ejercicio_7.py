
# 7. Genere un programa que clasifique a los estudiantes según sus puntuaciones:
# ● 80-100, A
# ● 70-89, B
# ● 60-69, C
# ● 50-59, D
# ● 0-49, F

calificacion=int(input("Ingrese la puntuacion del estudiante: "))
print("     ----------      ")


print("     ----------      ")
if calificacion >= 80 and calificacion <=100 :
    print(f" La calificacion: {calificacion} es A.")
elif calificacion >=70 and calificacion <= 89:
    print(f" La calificacion: {calificacion} es B.")
elif calificacion >=60 and calificacion <= 69:
        print(f" La calificacion: {calificacion} es C.")
elif calificacion >=50 and calificacion <= 59:
            print(f" La calificacion: {calificacion} es D.")
elif calificacion >=0 and calificacion <= 49:
                 print(f" La calificacion: {calificacion} es F.")
else:
    print(f" La calificacion: {calificacion} no es valido")
    
print("---------------------")