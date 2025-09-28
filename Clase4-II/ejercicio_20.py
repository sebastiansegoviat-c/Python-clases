"""Manejo de errores"""
"""
Requisitos:
- Crear una función la cuál va a evaluar una lista y un índice
- Habrá una exepción donde dentro de la función que sa a considerar 
una lista con 4 valores
- Cuando se va a modificar una de las posiciones no existentes
crear un nuevo índice y darle un valor de 0
- Mostrar la lista final

correo: docente.cerseu.unmsm@gmail.com
asunto: Participación para práctica 02
tiempo máximo de entrega: sábado 27 11:59 pm
Enviar en un mismo correo: ejercicio_07, ejercicio_12 y ejercicio_20
"""

def funcion(lista, indice):
    try:
        valor_1 = lista[indice]
        print(f"El índice: {indice} existe y su valor es: {valor_1}")
    except IndexError:
        print(f"El indice: {indice} no existe, pero se creara uno a continuación:")

        while len(lista) <= indice:
            lista.append(0)
        print(f"El nuevo indice: {indice} tiene un valor 0")
    return lista

lista_1 = [70, 134, 11, 78]
print(f"La lista inicial es de: {lista_1}")

resultado_1 = funcion(lista_1, 1)
print(f"La lista final es de: {resultado_1}")

resultado_2 = funcion(lista_1, 8)
print(f"La lista final es de: {resultado_2}")

