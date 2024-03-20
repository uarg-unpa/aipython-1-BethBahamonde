# 6. Escriba un programa que pida al usuario un número entero del 1 al 7 y muestre por
# pantalla a qué día de la semana corresponde. Controlar que el número se encuentre
# dentro del rango [1-7], sino es así, mostrar un mensaje. Por ejemplo, si se ingresa el
# número 2 la salida debe ser martes


num = input("Ingrese un nro del [1-7]: ")
print("     ----------      ")
match num :
    case "Lunes":
        print("Es lunes")
    case "Martes":
        print("es martes")
    case "Miercoles":
        print("es miercoles")
    case "Jueves":
        print("es jueves")
    case "Viernes":
        print("es viernes")
print("---------------------")
