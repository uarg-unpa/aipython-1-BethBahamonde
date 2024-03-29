import random #esta linea la van a poner al principio del archivo.
# Función para lanzar un dado, como vemos nos dará un número entre 1  y el número de caras, en este caso si incluye a caras entre las posibilidades a diferencia de range.
#Si por ejemplo caras vale 6, nos dará un número entre el 1 y el 6.

def lanzar_dado(caras):
     return random.randint(1, caras)


num=lanzar_dado(10)
print(num)

#vamos a modificar la calculadora para usar funciones
#Calculadora AIPython, solo trabaja con dos numeros enteros
#revisar su funcionamiento
#agregar valores por defecto
#modificar como mas les guste
#terminar la funcion de mostrar_estadistica
def suma(a,b): 
 return a+b
def resta(a,b): 
 return a-b
def producto(a,b): 
 return a*b
def division(a,b): 
 return a/b
def potencia(a,b): 
 return a**b
def div_entera(a,b): 
 return a//b
def mostrar_menu(): 
 print(f"1: Para sumar ") 
 print(f"2: Para restar ") 
 print(f"3: Para multiplicar ") 
 print(f"4: Para dividir ") 
 print(f"5: Para calcular la potencia ") 
 print(f"6: Para obtener la division entera 
entre ") 
 print(f"7: Para Finalizar ") 
 
def mostrar_estadistica(sumas, restas, 
cant_operaciones, cant_operaciones_incorrectas): 
 #mostrar esta estadistica utilizando tabulacion y que se imprima como una tabla
 #que tenga titulos y la informacion
 pass
def main(): 
 print("Bienvenidos a la calculadora AIPython P1") 
 cant_ope=0
 cant_operaciones_incorrectas=0
 sumas=0
 restas=0
 op=0
 while True : 
 mostrar_menu() 
 op=int(input("Ingrese la opcion para 
operar con los numeros: ")) 
 if op >= 1 and op <=6 : 
 num1=int(input("Ingrese el primer 
numero: ")) 
 num2=int(input("Ingrese el segundo 
numero: ")) 
 if op == 1: 
 sum=suma(num1,num2) 
 cant_ope+=1
 print(f"La suma es {sum}") 
 elif op == 2: 
 resta=resta(num1,num2) 
 cant_ope+=1
 print(f"La resta es {resta}") 
 elif op == 3: 
 multiplicacion=producto(num1,num2) 
 cant_ope+=1
 print(f"El producto es 
{multiplicacion}") 
 elif op == 4: 
 div=division(num1,num2) 
 cant_ope+=1
 print(f"La division es {div}") 
 elif op == 5 : 
 pote= potencia(num1,num2) 
 cant_ope+=1
 print(f"La potencia es {pote}") 
 elif op == 6 : 
 division_en= 
division_entera(num1,num2) 
 cant_ope+=1
 print(f"La division entera es 
{division_en}") 
 elif op == 7 : 
 print("Adios vuelva pronto!!") 
 print(f"La cantidad de operaciones 
realizadas fueron: {cant_ope}") 
 print(f"Intentos en opciones no 
disponibles: {cant_operaciones_incorrectas}") 
 break 
 elif op!= 7: 
 print(f"Parece que {op} aun no esta 
definida entre las opciones \nprobemos de 
nuevo !!") 
 cant_operaciones_incorrectas+=1
 continue
main() 