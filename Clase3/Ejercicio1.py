"""Listas en Python"""

"""
Listas, 
len(): obtener tamaño de las listas en python
append(): agrega elementos en la lista
"""

comidas = [] #inicio: lista vacia
print("Mi lista de países contiene los valores: ".format(comidas))
print("Tamaño de lista: {}".format(len(comidas)))

"""Agregar datos a la lista"""

comidas.append("Causa")
comidas.append("Ceviche")
comidas.append("Chaufa")

print("Mi lista de países: {}".format(comidas))

comidas.append("Pollo a la brasa")
print("Mi lista de países: {}".format(comidas))

comida = comidas[2]
print("El primer valor, elemento 0, de mi lista es: {}".format(comida))

#El valor dentro de una lista lo obtenemos mediante su índice
#Siempre el primer valor empieza en índice 0