# preguntasTupla es una tupla que contiene tres listas, cada una representando un nivel de dificultad:
# fácil, medio y difícil. Dentro de cada nivel hay cinco listas vacías que sirven como categorías 
# iniciales. Estas listas pueden ser utilizadas para almacenar preguntas y respuestas organizadas por nivel y categoría.
preguntasTupla = (
    [[] for i in range(5)],  # Nivel de dificultad 1 (fácil)
    [[] for i in range(5)],  # Nivel de dificultad 2 (medio)
    [[] for i in range(5)]   # Nivel de dificultad 3 (difícil)
)



def leerPreguntas():
    # Intenta abrir y procesar el archivo
    try:
        with open('preguntas.txt', 'r', encoding='utf-8') as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                datos = linea.strip().split(';')

                if len(datos) < 4:
                    print(f"❌ Línea inválida en preguntas.txt (línea {numero_linea}): {linea.strip()}")
                    continue

                try:
                    categoria, dificultad, pregunta, *opciones, respuestaCorrecta = datos
                except ValueError:
                    print(f"❌ Error al desempaquetar línea {numero_linea}: {linea.strip()}")
                    continue

                fila = {'facil': 0, 'media': 1, 'dificil': 2}.get(dificultad)
                columna = {'geografía': 0, 'historia': 1, 'ciencia': 2, 'deporte': 3, 'arte': 4}.get(categoria)

                if fila is None or columna is None:
                    print(f"❌ Dificultad o categoría inválida en línea {numero_linea}: {linea.strip()}")
                    continue

                preguntasTupla[fila][columna].append({
                    'pregunta': pregunta,
                    'opciones': opciones,
                    'respuestaCorrecta': respuestaCorrecta
                })

    except FileNotFoundError:
        print("🚫 Error: El archivo 'preguntas.txt' no fue encontrado.")
    except UnicodeDecodeError:
        print("🚫 Error: Problema al leer 'preguntas.txt', puede tener un formato no compatible.")
    except Exception as e:
        print(f"🚫 Error inesperado: {e}")
