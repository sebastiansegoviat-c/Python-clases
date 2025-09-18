var_1 = 15.499
var_2 = -19.56223

print("El valor de var_1 es: {} y el valor de mi var_2 es: {}".format(var_1, var_2))
print("El valor de mi var_2 modificado con 2 decimales es: {}".format(f"{var_2:.2f}"))
print("El valor de mi var_1 modificado con 1 decimal es: {}".format(f"{var_1:.1f}"))
print("El valor de la suma de var_1 y var_2 es: {}".format(f"{var_1 + var_2:.2f}"))
print("El valor de la resta de var_1 y var_2 es: {}".format(f"{var_1 - var_2:.2f}"))
print("El valor del producto de var_1 y var_2 es: {}".format(f"{var_1 * var_2:.2f}"))
print("El valor del cociente de var_1 y var_2 es: {}".format(f"{var_1 / var_2:.2f}"))

try:
    x = input("Ingresa una nueva valor: ")
    x = int(x)
except ValueError:
    print("El valor ingresado no valido")
else:
    print("El valor impreso es:", x)

