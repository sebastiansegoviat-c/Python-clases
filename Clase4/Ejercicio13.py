"""Uso de condicional if"""

edad_1 = int(input("Ingrese la primera edad: "))
edad_2 = int(input("Ingrese la segunda edad: "))

if edad_1 > edad_2:
    print("La primera edad es mayor a la segunda")
elif edad_1 == edad_2:
    print("Ambas edades son iguales")
    edad_2 = edad_2 + 5
    print("La segundad edad actualizada es {}".format(edad_2))
else:
    print("La segunda edad es mayor a la primera edad")