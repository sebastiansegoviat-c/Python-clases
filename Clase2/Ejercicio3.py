"""
Requisitos:
"""

#Crear 2 variables enteras, 2 variables flotantes, 2 variables string, 1 variable string que contiene valor numérico y una variable boolean
a = 130
b = 200
c = 70.6
d = 10.78
e = "Sebastian Segovia"
f = "999"
g = True

#Obtener y mostrar la suma de una variable entera con la variable numérica.
suma = a + int(f)
print("La suma es: {}".format(suma))

#Obtener y mostrar la suma de las 2 variables enteras más la variable string numérica y la variable flotante
suma2 = a + b + int(f) + int(c)
print("La suma es: {}".format(suma2))

#Obtener y mostrar el módulo de las variables enteras: %
modulo1 = a % b
print("El modulo es: {}".format(modulo1))

#Obtener y mostrar el resultado de la parte entera de los variables enteras: //
div = a // b
print("El resultado es: {}".format(div))

#Obtener una potencia usando una de las variables flotantes y la variable entera como potencia
pow = d ** b
print("La potencia es: {}".format(pow))