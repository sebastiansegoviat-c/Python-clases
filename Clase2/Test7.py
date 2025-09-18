"""
Reconocimiento de tipos de datos: type()
"""

nombre = "Sebastian"
ciudad = "Lima"
sueldo = 6000
empresa = False
correo = "sebastian123@gmail.com"
empleado = [nombre, ciudad, sueldo, empresa]
empleado1 = {'nombre': nombre, 'ciudad': ciudad, 'sueldo': sueldo,}

print("Tipo de variable para 'nombre' es {}".format(type(nombre)))
print("Tipo de variable para 'ciudad' es {}".format(type(ciudad)))
print("Tipo de variable para 'sueldo' es {}".format(type(sueldo)))
print("Tipo de variable para 'empresa' es {}".format(type(empresa)))
print("Tipo de variable para 'correo' es {}".format(type(correo)))
print("Tipo de variable para 'empleado' es {}".format(type(empleado)))
print("Tipo de veriable variable para 'empleado1' es {}".format(type(empleado1)))