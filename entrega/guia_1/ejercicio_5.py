# 5. Utilizando la función input
# a. Crear un programa que imprima un mensaje (usar función print) solicitando, el nombre, el apellido y la edad desde la terminal y luego darle un mensaje ,“ser creativo”, utilizando los tres datos ingresados.
nombre=input("Ingrese nombre: ")
apellido=input("Ingrese apellido: ")
edad=input("Ingrese edad: ")
print(nombre,apellido,edad,sep="\n")

# b. Modificar el ejercicio anterior para no utilizar la función print para mostrar el mensaje al solicitar los datos. Tip pasarle el argumento a la función input.
input(nombre+apellido+edad)
