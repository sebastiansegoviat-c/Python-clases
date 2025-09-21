"""
Uso de la condicional if
"""

edad = int(input("Ingrese edad: "))
if 0 < edad < 18:
    print("Usted es menor de edad")
elif 18 <= edad < 65:
    print("Usted es una persona adulta")
elif 65 <= edad < 100:
    print("Usted es un persona de la tercera edad")
else:
    print("Usted ha ingresado una edad incorrecta. Ingrese una edad valida, por favor")
