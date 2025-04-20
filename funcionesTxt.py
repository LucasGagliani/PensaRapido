
preguntasMatriz = [
    [[] for i in range(5)],
    [[] for i in range(5)],
    [[] for i in range(5)]
]

""""def crear_archivo():
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
"""


def leer_preguntas():
    
    with open('preguntas.txt', 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            datos = linea.strip().split(';')
            categoria,dificultad,pregunta,*opciones,respuestaCorrecta = datos
    
            fila = {'facil':0,'media':1,'dificil':2}[dificultad]
            columna = {'geografía':0,'historia':1,'ciencia':2,'deporte':3,'arte':4}[categoria]

            preguntasMatriz[fila][columna].append({
            'pregunta': pregunta,
            'opciones': opciones,
            'respuestaCorrecta': respuestaCorrecta
            })

# Mostrar la matriz
    """print("Preguntas organizadas:")
    for i, fila in enumerate(preguntasMatriz):
        dificultad = ['facil', 'media', 'dificil'][i]
        print(f"Dificultad {dificultad}:")
        for j, preguntas in enumerate(fila):
            categoria = ['geografía', 'historia', 'ciencia', 'deporte','arte'][j]
            print(f"  Categoría {categoria}: {preguntas}")"""