"""Listas en python"""
from itertools import count

"""
Listas,
count(): cantidad de veces que se repite un elemento de la lista
"""

elementos = ["boro", "silicio", "radio", "selenio", "selenio", "selenio", "boro"]

elementos.append("cromo")
elementos.append("cromo")
elementos.append("cromo")
elementos.append("cromo")

print("Mi lista es: {}".format(elementos))

print("Cantidad de veces que se repite 'cromo': {}".format(elementos.count("cromo")))