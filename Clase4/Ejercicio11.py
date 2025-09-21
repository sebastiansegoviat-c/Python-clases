"""
Intervención

Requisitos:
Requisitos:
- Dentro de una empresa se vaa solicitar pedir el nombre y apelldio del empleado (input)
- Distrito de residencia ingresado por teclado
- Sueldo y cálculo del bono final de año, que será el triple del sueldo mensual menos el 10% del sueldo
- Todos estos datos se van a ingresar a un diccionario
- Asignar a 3 variables los valores del diccionario
- Mostrar por la terminal (output) el mensaje de: "'Nombre' 'Apellido',
recibirá 'bono' soles de fin de año"


Para la entrega:
* Hora entrega:
* Correo: 
* Asunto: Intervención 02
* Adjuntar archivo.py y screenshot con resultados
"""

var_1 = input("Ingresa tu nombre y apellido: ")
var_2 = input("Ingresa tu distrito de residencia: ")
var_3 = int(input("Ingresa tu sueldo: "))

var_4 = (var_3 * 3) - ((var_3 * 10)/100)

datos_usuario = {"nombre y apellido": var_1, "distrito de residencia": var_2, "sueldo": var_3, "bono final": var_4}
valor_usuario = list(datos_usuario.values())
print("Datos de usuario: {} recibira {} soles al fin de año".format(datos_usuario["nombre y apellido"], datos_usuario["bono final"]))





