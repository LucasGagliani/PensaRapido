# preguntasTupla es una tupla que contiene tres listas, cada una representando un nivel de dificultad:
# fácil, medio y difícil. Dentro de cada nivel hay cinco listas vacías que sirven como categorías 
# iniciales. Estas listas pueden ser utilizadas para almacenar preguntas y respuestas organizadas por nivel y categoría.
preguntasTupla = (
    [[] for i in range(5)],  # Nivel de dificultad 1 (fácil)
    [[] for i in range(5)],  # Nivel de dificultad 2 (medio)
    [[] for i in range(5)]   # Nivel de dificultad 3 (difícil)
)

def leerPreguntas():
    """
    Lee las preguntas desde el archivo 'preguntas.txt' y las organiza en una matriz según
    categoría y dificultad.

    Cada línea del archivo debe tener el siguiente formato:
        categoría;dificultad;pregunta;opción1;opción2;...;respuestaCorrecta

    Las preguntas se almacenan en la estructura global `preguntasTupla`, con la siguiente
    organización:
        - Filas: dificultad (fácil, media, difícil)
        - Columnas: categoría (geografía, historia, ciencia, deporte, arte)

    Si una línea del archivo no cumple con el formato esperado, se muestra un mensaje de error
    y se omite esa entrada.

    Maneja errores como:
        - Archivo no encontrado
        - Problemas de codificación (UTF-8)
        - Errores de estructura o desempaquetado

    No recibe parámetros ni retorna valores. Modifica la variable global `preguntasTupla`.
    """
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
