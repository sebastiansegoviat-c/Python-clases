"""
Intervención
"""

"""Usando propiedades de string"""
"""
Requisitos:
- Ingresar su nombre y apellido por consola
(variables distintas)
- Obtener el tamaño de tu nombre completo y muéstralo en consola
- Imprimir el resultado final, todo en mayúsculas: .upper()
- Indicar mediante condicionales si el tamaño del nombre es mayor o no al apellido ingresado
- Solamente ingresar el apellido paterno

correo: docente.cerseu.unmsm@gmail.com
asunto: Participación para práctica 02
tiempo máximo de entrega: sábado 27 11:59 pm
Enviar en un mismo correo: ejercicio_07, ejercicio_12 y ejercicio_20
"""

nombre = input("Ingresar tu nombre: ")
apellido = input("Ingresar tu apellido: ")

nombre_completo = nombre + " " + apellido

print("El tamaño de tu nombre completo es: {}".format(len(nombre_completo.strip())))
print("El resultado final es: {}".format(nombre_completo.upper()))

if len(nombre) > len(apellido):
    print("El tamaño del nombre es mayor al del apellido: {}".format(len(nombre)))
elif len(nombre) < len(apellido):
    print("El tamaño del apellido es mayor al del nombre: {}".format(len(apellido)))
else:
    print("El tamaño y el apellido tienen el mismo tamaño")