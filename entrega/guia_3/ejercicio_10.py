# 10. Escribir un programa que imprima todas las fichas del domino, una por línea,
# sin repetir. Como se muestra a continuación
# 0 0
# 0 1
# 0 2
# 0 3
# 0 4
# 0 5
# 0 6
# ...

for i in range(7):
    # print(f"i: {i}")
    for j in range(7):
        # print(f"j: {j}")
        print(f"|_ {i} {j} _|")