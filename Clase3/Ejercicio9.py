"""Listas en python"""

"""
Listas,
copy(): copia todos los elementos de una lista a una nueva
"""

var = ["etil", "metil", "amina", "hidroxi", "fenil", str(22)]

var2 = var.copy()
print("Mi lista 2 es: {}".format(var2))

var.pop(2)
print("Mi lista 1 es: {}".format(var))
print("Mi lista 2 es: {}".format(var2))