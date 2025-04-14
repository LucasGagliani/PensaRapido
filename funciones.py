


def crear_archivo():
    with open('preguntas.txt', 'w') as archivo:
        archivo.write('')
    print("archivo 'preguntas.txt' creado con éxito.")

def agregar_pregunta(pregunta, categoria,dificultad,respuesta):
    with open('preguntas.txt', 'a') as archivo:
        archivo.write(f'{pregunta};{categoria};{dificultad};{respuesta}\n')
    print("Pregunta agregada con éxito.")

