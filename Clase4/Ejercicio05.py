"""Diccionarios"""

"""lista: recorrido de las listas en un bucle for"""

notas = [10, 13, 16, 12, 15, 19, 14]
print("Las notas son: {}".format(notas))
print("____________________________________________")

i = 0
for nota in notas:
    print("La nota inicial es: {}".format(notas[i]))
    notas[i] = nota / 2
    print("Nota actualizada: {}".format(notas[i]))
    i = i + 1

print("____________________________________________")
notas.insert(7, 18)
notas.insert(8, 19)
print("La nota actualizada con dos nuevas notas: {}".format(notas))

