# 10. Implementar una función que convierte temperaturas de fahrenheit a celsius.


def grados_Celsius(grados):
    resultadoC=(grados-32)*5/9
    return resultadoC

temperatura=float(input("Ingrese la temperatura (F°): "))

celsius=grados_Celsius(temperatura)

print("---------------------------------------------------")
print(f"De {temperatura} F° a {celsius} C°  ")
