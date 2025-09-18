import os
while True:
    try:
        valor_1 = float(input("Introduce un primer valor numérico: "))
        valor_2 = float(input("Introduce un segundo valor numérico: "))

        print("Operaciones disponibles: +, -, *, /")
        operacion = input("Elige una operación")

        if operacion == "+":
            resultado = valor_1 + valor_2
        elif operacion == "-":
            resultado = valor_1 - valor_2
        elif operacion == "*":
            resultado = valor_1 * valor_2
        elif operacion == "/":
            if valor_2 != 0:
                resultado = valor_1 / valor_2
            else:
                resultado = "Error: 404 - Cuenta regresiva antes de autodestrucción"
        else:
            resultado = "Operación no valida"
            os.system("cacl")
        print("Resultado: {}".format(resultado))
    except ValueError:
        print("El valor ingresado es no valida!")