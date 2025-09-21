"""Diccionarios"""

"""Values: obtener los valores de los keys de un diccionario"""

base_datos = {'nombre': 'nicotina', 'tipo': 'alcaloide', 'metabolismo': 'hepático'}

"""Convertir diccionario a lista para keys y valores"""

base_datos_list = list(base_datos)
print('Diccionario (keys) convertido en lista: {}'.format(base_datos_list))

base_datos_values = list(base_datos.values())
print('Diccionario (valores) convertido en lista: {}'.format(base_datos_values))

base_datos_keys = list(base_datos.keys())
print('key: {}'.format(base_datos_keys))

base_datos_items = list(base_datos.items())
print('item: {}'.format(base_datos_items))