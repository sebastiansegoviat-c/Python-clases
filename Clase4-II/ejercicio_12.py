"""
Participación
"""
"""Programación funcional"""

"""
Requisitos:
- Crear una función que multiplicará 4 valores (int y floats)
- La función tendrá un parámetro o que contendrá un valor
- Mostrar 2 casos donde ese ingresó los valores donde uno no afectará el valor del parámetro
que ya contiene un valor y otro donde si lo estará afectando

correo: docente.cerseu.unmsm@gmail.com
asunto: Participación para práctica 02
tiempo máximo de entrega: sábado 27 11:59 pm
Enviar en un mismo correo: ejercicio_07, ejercicio_12 y ejercicio_20
"""

def multiplicacion(num_1=17, num_2=16, num_3=21.67, num_4=11.4):
    return num_1 * num_2 * num_3 * num_4


resultado_1 = multiplicacion(5, 7)
print(f"El primer resultado es {resultado_1} y solo dos valores han sido reemplazados")

resultado_2 = multiplicacion(5, 7, 999, 1)
print(f"El ultimo resultado es {resultado_2} y todos los valores han sido reemplazados")