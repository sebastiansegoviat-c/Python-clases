"""Diccionarios"""

"""sorted: obtener los nombres de los keys de un diccionario"""
base_datos = {'nombre': 'nicotina', 'tipo': 'alcaloide', 'metabolismo': 'hepático'}

keys = sorted(base_datos)
print(base_datos)

#Cuando se imprimen las keys están se convierten en listas
print(keys)

base_datos_keys_set = base_datos.keys()
print("Conjuntos keys: {}".format(base_datos_keys_set))
base_datos_keys = list(base_datos.keys())
print("keys: {}".format(base_datos_keys))