#Raymond Sandí Morales
# Desarrolle un algoritmo que almacene las materias de un curso (mínimo 5 materias) en una lista y la muestre por pantalla.
# Definimos las materias del curso

Curso = ['Matemáticas', 'Ciencia', 'Español', 'Estudios Sociales', 'Inglés']

# Luego que muestre en pantalla el mensaje: Yo estudio <materia>, donde <materia> es cada una de las materias de la lista.

print("\nMaterias del curso:")
for materia in Curso:
    print(materia)

print("\nMaterias que estudio:")
for materia in Curso:
    print("Yo estudio", materia)

# Aunado a esto pregunte al usuario la nota que ha sacado en cada curso, y después las muestre por pantalla con el mensaje:
# En <materia> has sacado <nota> donde <materia> es cada una de las materias de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

notas = {}
for materia in Curso:
    nota = input("Ingresa la nota que has sacado en " + materia + ": ")
    notas[materia] = int(nota)

print("\nNotas del usuario:")
for materia, nota in notas.items():
    print("En", materia, "has sacado", nota)

# Al final el programa debe mostrar en el monitor las materias que el usuario tiene que repetir, sacando o eliminando de la lista las materias que si fueron aprobadas.

Curso_repetir = []
for materia in Curso:
    if notas[materia] < 70:
        Curso_repetir.append(materia)
        Curso.remove(materia)

if len(Curso_repetir) > 0:
    print("\nMaterias que el usuario tiene que repetir:")
    for materia in Curso_repetir:
        print(materia)
else:
    print("Felicidades, ha aprobado todo el curso")


