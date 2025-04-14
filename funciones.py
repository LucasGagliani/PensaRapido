


def crear_archivo():
    with open('preguntas.txt', 'w') as archivo:
        archivo.write('')
    print("archivo 'preguntas.txt' creado con éxito.")

def agregar_pregunta(pregunta, categoria,dificultad,respuesta):
    with open('preguntas.txt', 'a') as archivo:
        archivo.write(f'{pregunta};{categoria};{dificultad};{respuesta}\n')
    print("Pregunta agregada con éxito.")

def pedir_pregunta():
    pregunta = input("Ingrese la pregunta: ")
    categoria = input("Ingrese la categoria: ")
    dificultad = input("Ingrese la dificultad: ")
    respuesta = input("Ingrese la respuesta: ")
    agregar_pregunta(pregunta, categoria, dificultad, respuesta)

def leer_preguntas():
    preguntas = []
    with open('preguntas.txt', 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(';')
            preguntas.append(datos)  # Cada pregunta es una lista con sus datos
    print("Preguntas cargadas exitosamente",preguntas)
    return preguntas

crear_archivo()
pedir_pregunta()
pedir_pregunta()
leer_preguntas()