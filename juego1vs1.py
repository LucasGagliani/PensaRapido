import funcionesTxt
import random  # Importar random para elegir preguntas aleatorias

preguntasMatriz = funcionesTxt.preguntasMatriz

validar_nombre = lambda nombre: nombre != "" and nombre.isalpha() and len(nombre) >= 3 and len(nombre) <= 20
def pedir_nombre(jugador_num):
    """
    Pide el nombre del jugador y valida que sea correcto.
    """
    while True:
        nombre = input(f"Nombre del Jugador {jugador_num}: ")
        if not validar_nombre(nombre):
            print("⚠️ El nombre solo debe contener letras, sin espacios ni símbolos ni números.")
        else:
            return nombre

def mostrarOpciones(lista):
    """
    Muestra las opciones de una lista y permite seleccionar por número.
    """
    for i in range(len(lista)):
        print(f"{i+1}. {lista[i]}")
    while True:
        entrada = input("Elegí una opción (número): ")
        if entrada.isdigit():
            numero = int(entrada)
            if 1 <= numero <= len(lista):
                return numero - 1
        print("Entrada inválida. Probá de nuevo.")

def hacerPreguntaAleatoria(preguntasMatriz):
    
    """
    Permite seleccionar una categoría y dificultad, luego muestra una pregunta aleatoria.
    """
    categorias = ['geografía', 'historia', 'ciencia', 'deporte', 'arte']
    dificultades = ['facil', 'media', 'dificil']

    # Mostrar opciones de categorías y dificultad
    print("\nSelecciona una categoría:")
    categoriaIndex = mostrarOpciones(categorias)

    print("\nSelecciona una dificultad:")
    dificultadIndex = mostrarOpciones(dificultades)

    # Obtener las preguntas correspondientes a la categoría y dificultad seleccionadas
    preguntasDisponibles = preguntasMatriz[dificultadIndex][categoriaIndex]

    if len(preguntasDisponibles) == 0:
        print("\nNo hay preguntas disponibles en esta categoría y dificultad.")
        return

    # Elegir una pregunta aleatoria
    pregunta = random.choice(preguntasDisponibles)
    print("\nPregunta seleccionada:")
    print(pregunta['pregunta'])

    # Mostrar opciones
    print("\nOpciones:")
    for i, opcion in enumerate(pregunta['opciones']):
        print(f"{i+1}. {opcion}")

    # Pedir respuesta al jugador
    while True:
        respuesta = input("\nElegí la respuesta (número): ")
        if respuesta.isdigit() and 1 <= int(respuesta) <= len(pregunta['opciones']):
            seleccion = pregunta['opciones'][int(respuesta) - 1]
            if seleccion == pregunta['respuestaCorrecta']:
                print("¡Correcto!")
                return True
            else:
                print(f"Incorrecto. La respuesta correcta era: {pregunta['respuestaCorrecta']}")
                return False
        print("Entrada inválida. Intentá de nuevo.")

import random  # Importamos random para preguntas aleatorias

def modo1vs1():
    """
    Modo de juego 1vs1 donde los jugadores compiten en varias rondas.
    """
    funcionesTxt.leer_preguntas()
    print("\n¡Bienvenidos al modo 1vs1!")
    nombreJugador1 = pedir_nombre(1)
    nombreJugador2 = pedir_nombre(2)
    puntajes = [0, 0]

    categorias = ['geografía', 'historia', 'ciencia', 'deporte', 'arte']
    dificultades = ['facil', 'media', 'dificil']

    rondas = 5  # Cantidad de rondas
    for ronda in range(rondas):
        print(f"\nRonda {ronda + 1} de {rondas}")

        # Turno Jugador 1
        print(f"\n{nombreJugador1}, elegí una categoría:")
        categoriaIndex = mostrarOpciones(categorias)
        print("\nElegí una dificultad:")
        dificultadIndex = mostrarOpciones(dificultades)

        preguntasDisponibles = preguntasMatriz[dificultadIndex][categoriaIndex]
        if len(preguntasDisponibles) == 0:
            print("No hay preguntas disponibles en esta categoría y dificultad.")
        else:
            preguntaSeleccionada = random.choice(preguntasDisponibles)
            print("\nPregunta:")
            print(preguntaSeleccionada['pregunta'])
            print("\nOpciones:")
            for i, opcion in enumerate(preguntaSeleccionada['opciones']):
                print(f"{i+1}. {opcion}")
            while True:
                respuesta = input("\nElegí la respuesta (número): ")
                if respuesta.isdigit() and 1 <= int(respuesta) <= len(preguntaSeleccionada['opciones']):
                    seleccion = preguntaSeleccionada['opciones'][int(respuesta) - 1]
                    if seleccion == preguntaSeleccionada['respuestaCorrecta']:
                        print("¡Correcto!")
                        puntajes[0] += (dificultadIndex + 1) * 10
                    else:
                        print(f"Incorrecto. La respuesta correcta era: {preguntaSeleccionada['respuestaCorrecta']}")
                    break
                print("Entrada inválida. Intentá de nuevo.")

        # Turno Jugador 2
        print(f"\n{nombreJugador2}, elegí una categoría:")
        categoriaIndex = mostrarOpciones(categorias)
        print("\nElegí una dificultad:")
        dificultadIndex = mostrarOpciones(dificultades)

        preguntasDisponibles = preguntasMatriz[dificultadIndex][categoriaIndex]
        if len(preguntasDisponibles) == 0:
            print("No hay preguntas disponibles en esta categoría y dificultad.")
        else:
            preguntaSeleccionada = random.choice(preguntasDisponibles)
            print("\nPregunta:")
            print(preguntaSeleccionada['pregunta'])
            print("\nOpciones:")
            for i, opcion in enumerate(preguntaSeleccionada['opciones']):
                print(f"{i+1}. {opcion}")
            while True:
                respuesta = input("\nElegí la respuesta (número): ")
                if respuesta.isdigit() and 1 <= int(respuesta) <= len(preguntaSeleccionada['opciones']):
                    seleccion = preguntaSeleccionada['opciones'][int(respuesta) - 1]
                    if seleccion == preguntaSeleccionada['respuestaCorrecta']:
                        print("¡Correcto!")
                        puntajes[1] += (dificultadIndex + 1) * 10
                    else:
                        print(f"Incorrecto. La respuesta correcta era: {preguntaSeleccionada['respuestaCorrecta']}")
                    break
                print("Entrada inválida. Intentá de nuevo.")

    # Resultados del juego
    print("\n¡Partida terminada!")
    print(f"{nombreJugador1} → {puntajes[0]} puntos")
    print(f"{nombreJugador2} → {puntajes[1]} puntos")
    if puntajes[0] > puntajes[1]:
        print(f"¡Ganó {nombreJugador1}!")
    elif puntajes[1] > puntajes[0]:
        print(f"¡Ganó {nombreJugador2}!")
    else:
        print("¡Empate!")