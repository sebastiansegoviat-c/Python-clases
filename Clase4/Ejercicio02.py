"""Diccionarios"""

"""del: elimina un key y su valor del diccionario"""

datos1 = {'nombre': 'Iris', 'edad': 30, 'promedio': 18}

datos1['distrito'] = "Comas"

del datos1['edad']
# Si no existe el dato, crashea: del datos1['domicilio']"

print("Diccionario actualizado: {}".format(datos1))