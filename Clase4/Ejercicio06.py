"""Diccionarios"""

"""Participación
- Crear diccionario de contacto, el cual tendrá como keys: 
Nombre, value: telefono,
- Verificar si existe el número de contcto de una persona, para esto estos valores 
serán verificados con variables entre 2 que existan y dos que no existan
- Indicar mediante un mensaje si estan o no agregados a la agenda de 
contactos
- En caso que no exista agregarlo al diccionario de contactos
- Mostar el diccionario actualizado
"""

contactos = {"José": 997122767, "Adrian": 988840091, "María": 901971334, "Iris": 990807144}

key1 = input("Introduzca el nombre del contacto: ")
if key1 in contactos:
    print("El número del contacto es: {}".format(contactos[key1]))
    print("___________________________________________________")
else:
    print("El contacto no está agendado")
    contactos[key1] = int(input("Introduzca el número del contacto: "))
    print("___________________________________________________")

key2 = input("Introduzca el nombre del contacto: ")
if key2 in contactos:
    print("El número del contacto es: {}".format(contactos[key2]))
    print("___________________________________________________")
else:
    print("El contacto no está agendado")
    contactos[key2] = int(input("Introduzca el número del contacto: "))
    print("___________________________________________________")

key3 = input("Introduzca el nombre del contacto: ")
if key3 in contactos:
    print("El número del contacto es: {}".format(contactos[key3]))
    print("___________________________________________________")
else:
    print("El contacto no está agendado")
    contactos[key3] = int(input("Introduzca el número del contacto: "))
    print("___________________________________________________")

key4 = input("Introduzca el nombre del contacto: ")
if key4 in contactos:
    print("El número del contacto es: {}".format(contactos[key4]))
    print("___________________________________________________")
else:
    print("El contacto no está agendado")
    contactos[key4] = int(input("Introduzca el número del contacto: "))
    print("___________________________________________________")

print("Lista de contacto actualizada: {}".format(contactos))



