import funcionesTxt
import random
import time
import threading
import ranking

PENALIZACION_TIEMPO = 10  # segundos extra por respuesta incorrecta o timeout
TIEMPO_LIMITE = 30        # máximo de 30 segundos por pregunta

def pedirRespuestaConTiempo():
    """
    Solicita una respuesta numérica del usuario con un límite de tiempo.

    Inicia un hilo para esperar la entrada del usuario y permite un tiempo máximo
    definido por `TIEMPO_LIMITE`. Si el usuario no responde a tiempo, retorna None.

    Retorna:
        str or None: La respuesta ingresada por el usuario como cadena, o None si se agotó el tiempo.
    """
    respuesta = [None]

    def obtenerRespuesta():
        respuesta[0] = input("\n📝 Elegí la respuesta (número): ")

    hilo = threading.Thread(target=obtenerRespuesta)
    hilo.start()
    hilo.join(timeout=TIEMPO_LIMITE)

    if hilo.is_alive():
        print("⏰ ¡Tiempo agotado!")
        hilo.join() 
        return None
    return respuesta[0]


def hacerPregunta(nombre, pregunta):
    """
    Presenta una pregunta al jugador, mide el tiempo de respuesta y evalúa su respuesta.

    Muestra la pregunta y opciones desordenadas, solicita la respuesta con límite de tiempo,
    y devuelve si la respuesta fue correcta junto con el tiempo que tardó o la penalización.

    Parámetros:
    nombre (str): Nombre del jugador a quien se le hace la pregunta.
    pregunta (dict): Diccionario con las claves:
        - 'pregunta' (str): Texto de la pregunta.
        - 'opciones' (list): Lista de opciones posibles.
        - 'respuestaCorrecta' (str): Opción correcta.

    Retorna:
    tuple (bool, float):  
        - bool: True si la respuesta es correcta, False si es incorrecta o inválida o tiempo agotado.  
        - float: Tiempo en segundos que tardó en responder (incluye penalización si aplica).
    """
    print(f"\n❓ {nombre}, respondé esta pregunta:")
    print(pregunta["pregunta"])

    opciones = pregunta["opciones"][:]
    random.shuffle(opciones)

    for i, opcion in enumerate(opciones):
        print(f"   {i+1}. {opcion}")

    tiempoInicio = time.time()
    respuesta = pedirRespuestaConTiempo()
    tiempoFin = time.time()

    tiempoRespuesta = tiempoFin - tiempoInicio

    if respuesta is None:
        print(f"❌ No respondiste a tiempo. Se suma una penalización de +{PENALIZACION_TIEMPO} segundos.")
        return False, TIEMPO_LIMITE + PENALIZACION_TIEMPO

    if respuesta.isdigit():
        indice = int(respuesta)
        if 1 <= indice <= len(opciones):
            seleccion = opciones[indice - 1]
            if seleccion == pregunta["respuestaCorrecta"]:
                print("✅ ¡Correcto!")
                return True, tiempoRespuesta
            else:
                print(f"❌ Incorrecto. La respuesta correcta era: {pregunta['respuestaCorrecta']}")
                return False, tiempoRespuesta + PENALIZACION_TIEMPO

    print("❌ Entrada inválida. Se cuenta como incorrecta.")
    return False, tiempoRespuesta + PENALIZACION_TIEMPO

def modoContraReloj():
    """
    Ejecuta el modo de juego 'Contra Reloj', donde el jugador debe responder 10 preguntas
    con un límite de tiempo por pregunta y penalizaciones por errores o entradas inválidas.

    El jugador ingresa su nombre y responde preguntas aleatorias de categorías y dificultades
    variadas. Cada respuesta incorrecta o inválida suma una penalización de tiempo.

    Al finalizar, muestra el tiempo total y la cantidad de respuestas correctas, y guarda
    el resultado en el ranking.

    No recibe parámetros ni retorna valores; toda la interacción es por consola.
    """

    funcionesTxt.leerPreguntas()
    preguntasMatriz = funcionesTxt.preguntasTupla
    print("\n⏱️ ¡Bienvenid@ al modo *Contra Reloj*!")
    print("🎯 Vas a responder 10 preguntas con un límite de 30 segundos por pregunta.")
    print("❌ Cada error o entrada inválida suma +10 segundos al tiempo total.\n")

    nombreJugador = input("👉 Ingresá tu nombre: ").strip()
    if not nombreJugador:
        nombreJugador = "Jugador"

    categorias = ['geografía', 'historia', 'ciencia', 'deporte', 'arte']
    dificultades = ['facil', 'media', 'dificil']

    tiempoTotal = 0
    correctas = 0
    preguntasUsadas = []

    for turno in range(10):
        print(f"\n🎯 Pregunta {turno + 1} de 10")

        categoriaIndex = random.randint(0, len(categorias) - 1)
        dificultadIndex = random.randint(0, len(dificultades) - 1)

        preguntasDisponibles = preguntasMatriz[dificultadIndex][categoriaIndex]
        preguntasFiltradas = [p for p in preguntasDisponibles if p not in preguntasUsadas]

        if preguntasFiltradas:
            pregunta = random.choice(preguntasFiltradas)
            preguntasUsadas.append(pregunta)
            fueCorrecta, tiempo = hacerPregunta(nombreJugador, pregunta)
            tiempoTotal += tiempo
            if fueCorrecta:
                correctas += 1
        else:
            print("🚫 No hay preguntas disponibles. Se penaliza con +10 segundos.")
            tiempoTotal += PENALIZACION_TIEMPO

    print("\n🏁 ¡Fin del juego! Resultados:")
    print(f"⏱️ Tiempo total: {round(tiempoTotal, 2)} segundos")
    print(f"✅ Respuestas correctas: {correctas} de 10")

    ranking.guardar_resultado(nombreJugador, correctas, round(tiempoTotal, 2))

    input("\n🔄 Presiona Enter para volver al menú...")
