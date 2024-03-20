
# 12. Crear la siguiente lista

# flores= [rosas, orquídea,lirio,tulipan, margarita, dalia, hortensia]
# a. Mostrar tres elementos desde el tercer elemento.
# b. Mostrar los elementos en posiciones pares desde la segunda posición
# c. Mostrar todos los elementos desde la primera posición saltando de a tres
# elementos.

flores=['rosas', 'orquídea','lirio','tulipan', 'margarita', 'dalia', 'hortensia']
fin=len(flores)

print("Mostrar tres elementos desde el tercer elemento.")
for i in range(2,5):
    print(flores[i])

print("Mostrar los elementos en posiciones pares desde la segunda posición")
for i in range(1,fin):
    if i%2==0:
        print(flores[i])

print("Mostrar todos los elementos desde la primera posición saltando de a tres elementos")
print(flores[0::3])
