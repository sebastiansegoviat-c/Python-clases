"""Listas en python"""

"""
Listas,
pop(i): quitar un elemento en una posición dada
"""

colores = ["red", "yellow", "blue", "magenta", "ochre"]
print("Los colores son: {}".format(colores))

colores.pop()
print("Los colores actualizados son: {}".format(colores))

colores.pop(1)
print("Los colores actualizados son: {}".format(colores))

color_2 = colores[-1]
print("El valor de la variable es: {}".format(color_2))