"""
Operadores comunes
Operador suma
"""

var1 = "7000"
var2 = 777
var3 = 3.1416

suma1 = int(var1) + var2
print(suma1)

nombre = "Sebastian"
apellido = "Segovia"

nombre_completo = nombre + " " + apellido
print(nombre_completo)

print("_________________________")
suma_2 = str(var2) + var1
print(suma_2)
print("Tipo de dato: {}".format(type(suma_2)))

print("_________________________")
suma_3 = var2 + var3
print("Tipo de dato: {}".format(type(suma_3)))

print("_________________________")
suma_4 = var1 + str(var2) + str(var3)
print("Tipo de dato: {}".format(type(suma_4)))

