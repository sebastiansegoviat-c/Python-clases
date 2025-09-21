"""Uso de cond. if

Uso de if ternarios
Requisitos:
- Ingresar por teclado el sueldo del empleado
- Si el sueldo es mayor que 4000, imprimir "Su sueldo no tiene bonificación"
- Caso contrario indicar: "Su sueldo tiene bonificación este año y será de :
sueldo_final", sueldo_final = sueldo + 20% * sueldo

Para la entrega:
* Hora de entrega: 6:00 pm
* Correo a enviar: docente.cerseu.unmsm@gmail.com
* Asunto: Intervención a práctica 02
* Adjuntar archivo.py y screemshot con resultados

* Ambos ejercicios en un solo correo (11 y 19)

"""

while True:
    try:
        sueldo = int(input("Ingresar sueldo: "))
        if sueldo > 4000:
            print("Su sueldo no tiene bonificaciones")
        if sueldo <= 4000:
            sueldo_final = sueldo + (sueldo * 0.2)
            print("Su sueldo tiene bonificación este año y será de: {}".format(sueldo_final))
    except ValueError:
        print("Ingrese valores validos")

