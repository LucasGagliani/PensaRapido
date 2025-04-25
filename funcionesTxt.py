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


def leerPreguntas():
    with open('preguntas.txt', 'r', encoding='utf-8') as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            datos = linea.strip().split(';')
            
            # Depuración: Imprimir la línea si tiene un formato incorrecto
            if len(datos) < 4:
                print(f"❌ Línea inválida en preguntas.txt (línea {numero_linea}): {linea.strip()}")
                continue
            
            categoria, dificultad, pregunta, *opciones, respuestaCorrecta = datos
            
            fila = {'facil': 0, 'media': 1, 'dificil': 2}.get(dificultad)
            columna = {'geografía': 0, 'historia': 1, 'ciencia': 2, 'deporte': 3, 'arte': 4}.get(categoria)
            
            if fila is None or columna is None:
                print(f"❌ Dificultad o categoría inválida en línea {numero_linea}: {linea.strip()}")
                continue
            
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