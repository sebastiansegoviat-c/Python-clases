"""
    Programación Orientada a Objetos (POO)
    Participación
Requerimientos:
- Crear una clase Alumno
- Debe tener un atributo de nacionalidad con el valor de "Peruano"
- Crear un método que indicará el promedio del alumno
- Tendrá 3 notas para 3 cursos (Cálculo II, Matemática Discreta y Redes neuronales), la nota inicial de c/u será de 0
(puedes basarte en diccionarios)
- Crear un método donde indicará qué curso fue que tuvo la mayor nota
- Crear un método que indicará si el alumno está aprobado o no de acuerdo a su promedio  (>= 13)
- Las notas serás pasadas por parámetro al momento de instanciar la clase
- Habrá un método adicional para obtener el nombre y distrito de residencia del alumno
-  Instanciar la clase para el caso de 2 alumnos por lo menos

Entregar solución al correo: docente.cerseu.unmsm@gmail.com
Asunto: Participación  - Examen final
Entre máxima: 8:00 pm - 28 de Set.
"""


class Alumno:
    def __init__(self, nombre, distrito, nota_1=0, nota_2=0, nota_3=0):
        self.nacionalidad = "Peruano"
        self.nombre = nombre
        self.distrito = distrito
        self.cursos = {"Cálculo II": nota_1, "Matemática Discreta": nota_2, "Redes neuronales": nota_3}

    def promedio(self):
        suma = 0
        for nota in self.cursos.values():
            suma += nota
        return suma / 3

    def curso_maxima_nota(self):
        mayor_curso = ""
        mayor_nota = -1

        for curso, nota in self.cursos.items():
            if nota > mayor_nota:
                maxima_nota = nota
                maximo_curso = curso

        return maximo_curso, maxima_nota

    def aprobado(self):
        promedio = self.promedio()
        return promedio >= 13

    def datos(self):
        return f"Nombre: {self.nombre}, Distrito: {self.distrito}"
alumno_1 = Alumno("Juan Pérez", "Miraflores", 13, 15, 11)
alumno_2 = Alumno("María García", "San Isidro", 10, 12, 14)

print("\nLos datos del alumno 1 son:")
print(alumno_1.datos())
print(f"Nacionalidad: {alumno_1.nacionalidad}")
print(f"Promedio: {alumno_1.promedio():.2f}")
curso_max, nota_max = alumno_1.curso_maxima_nota()
print(f"Curso con mayor nota: {curso_max} con {nota_max}")
print(f"¿Aprobado?: {'Sí' if alumno_1.aprobado() else 'No'}")
print("________________________________________________________________________________________-")
print("\nLos datos del alumno 2 son:")
print(alumno_2.datos())
print(f"Nacionalidad: {alumno_2.nacionalidad}")
print(f"Promedio: {alumno_2.promedio():.2f}")
curso_max, nota_max = alumno_2.curso_maxima_nota()
print(f"Curso con mayor nota: {curso_max} con {nota_max}")
print(f"¿Aprobado?: {'Sí' if alumno_2.aprobado() else 'No'}")