"""Listas en python"""

"""
Listas,
del: eliminar un valor indicando su índice de la lista
"""

paises = []
paises.extend(["Perú", "Chipre", "Burkina Faso", "Seychelles"])
print("Mi lista es: {}".format(paises))

del paises[2]
print("Mi lista es: {}".format(paises))