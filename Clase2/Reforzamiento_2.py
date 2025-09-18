#Ejercicio 1
nombre = "Sebastian Segovia"
print("Hi {}".format(nombre))
print("La clase es: {}".format(type("Hola {}".format(nombre))))

print("______________________________")
#Ejercicio 2
var1 = 15
var2 = var1 * 10
var3 = var2 - 10
varfloat = float(var3)
print(varfloat)
print("La clase es: {}".format(type(varfloat)))

print("______________________________")
#Ejercicio 3
varstr = "777"
varint = 23
suma = int(varstr) + varint
print(suma)

print("______________________________")
#Ejercicio 4
radio = 5.5
pi = 3.14159
volumen = (4/3) * pi * (radio ** 3)
print("Radio de la esfera: {}".format(radio))
print("Volumen de la esfera: {}".format(f"{volumen:.2f}"))

print("______________________________")
#Ejercicio 5
sueldo = 4297
if sueldo % 2 == 0:
    print("El sueldo de {} es par".format(sueldo))
if sueldo % 2 :
    print("El sueldo de {} es impar".format(sueldo))

print("______________________________")
#Ejercicio 6
num1 = 13.56
num2 = 37.12
num3 = 6.78
num4 = 11.13
num5 = 9.98
media = (num1 + num2 + num3 + num4 + num5) / 5
print("La media es: {}".format(f"{media:.2f}"))
print("La clase de la media es: {}".format(type(media)))

print("______________________________")
#Ejercicio 7

num_1 = 77
num_2 = -109
num_3 = 59
modulo1 = num_1 % 3
modulo2 = num_2 % 5
modulo3 = num_3 % 7
suma_modulo = modulo1 + modulo2 + modulo3
print("El valor de la suma es: {}".format(suma_modulo))

print("______________________________")
#Ejercicio 8
lista1 = [3, 9, 27, 81]
lista2 = []

if lista1 == 0:
    print("La lista 1 esta vacía")
else:
    print("La lista 1 esta llena")
if not lista2 == 0:
    print("La lista 2 esta vacía")
else:
    print("La lista 2 esta llena")

print("______________________________")
#Ejercicio 9
base = 4
pow1 = base ** 6
resultado = pow1 - (2 * pow1)
print("El resultado es: {}".format(resultado))

print("______________________________")
#Ejercicio 10
flotante1 = 2.718281
print("El número con un decimal es: {}".format(f"{flotante1:.1f}"))
print("El número con un decimal es: {}".format(f"{flotante1:.2f}"))
print("El número con un decimal es: {}".format(f"{flotante1:.4f}"))

print("______________________________")
#Ejercicio 11
mi_edad = 19
pow_edad = mi_edad ** 5
div_edad = pow_edad / 10
mod_edad = div_edad % 3
print("El resultado de la división es: {} y su módulo es: {}".format(f"{div_edad:.2f}", f"{mod_edad:.2f}"))

print("______________________________")
#Ejercicio 12
nombre_1 = "Sebastian"
producto = "acetona"
precio_unitario = 248.7
cantidad = "3 galones"
print("Buen día {}, el detalle de su compra es el siguiente:".format(nombre_1))
print("- Producto: {}".format(producto))
print("- Precio_unitario: {}".format(precio_unitario))
print("- Cantidad: {}".format(cantidad))

print("______________________________")
#Ejercicio 13
celsius1 = 60
fahrenheit1 = (celsius1 * 9) / 5 + 32

celsius2 = 15
fahrenheit2 = (celsius2 * 9) / 5 + 32
print("La temperatura en °C: {}".format(celsius1))
print("La temperatura en Fahrenheit: {}".format(f"{fahrenheit1:.2f}"))

print("La temperatura en °C: {}".format(celsius2))
print("La temperatura en Fahrenheit: {}".format(f"{fahrenheit2:.2f}"))