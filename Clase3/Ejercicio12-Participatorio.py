"""
Participación
"""

lista1 = []
lista2 = []
print("La lista 1 inicial es: {}".format(lista1))
print("La lista 2 inicial es: {}".format(lista2))

print("_______________________________________________________")
lista1.extend(["Sebastian", "Segovia", 19, "Químico Farmacéutico"])
lista2.extend(["Sebastian", "Segovia", 19, "Químico Farmacéutico"])

edad_1 = lista1[2]
edad_2 = lista2[2]
suma_edad = edad_1 + edad_2
print("La suma de las edades de ambas listas es: {}".format(suma_edad))

suma_lista = lista1 + lista2
print("La suma de las listas es: {}".format(suma_lista))

print("_______________________________________________________")
lista1.reverse()
lista2.reverse()
nueva_lista = lista1 + lista2
print("La suma de las listas invertidas es: {}".format(lista1 + lista2))

print("_______________________________________________________")
lista1.pop(1)
lista2.pop(1)
lista2[0] = "Biotecnólogo"
print("La lista 1 actualizada es: {}".format(lista1))
print("La lista 2 actualizada es: {}".format(lista2))