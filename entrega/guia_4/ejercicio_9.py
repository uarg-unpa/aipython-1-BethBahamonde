# 9. Crear una función que tome un string como parámetro y verifique si es un
# palíndromo. Ejemplo: Arenera, Narran. etc.

def palindromo(txt):
    cadena=txt.lower().replace(" ", "")
    if(txt  ==cadena[::-1]):
        print("Es palindromo!!!")
        print(f" {txt}   {cadena[::-1]}")
    else:
        print("No es palindromo")
        print(f" {txt}   {cadena[::-1]}")

print("---------------------------")
print("     Palindromo     ")
print("---------------------------")
texto=input("Ingrese una cadena: ")

print("   -----   ------  ---  ")

palindromo(texto) 