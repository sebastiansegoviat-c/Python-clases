"""
Conversión de datos
"""

var_str = "123456"
nombre = "Sebastian"
modulo = 1
promedio = 17.9

#Conversión de string a int
var_int = int(var_str)
print(var_int)
print("Tipo de dato: {}".format(type(var_int)))

#Conversión de entero a string
var_mod = str(modulo)
print(var_mod)
print("Tipo de dato: {}".format(type(var_mod)))

#Conversión de string a entero no es posible
#var_nom = int(nombre)
#print(type(var_nom))

#Conversión de flotante a entero
var_int = int(promedio)
print("Tipo de dato es: {}".format(type(var_int)))
print(var_int)
