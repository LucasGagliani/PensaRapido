import funcionesTxt
import random
import time
import threading
import ranking

PENALIZACION_TIEMPO = 10  # segundos extra por respuesta incorrecta o timeout
TIEMPO_LIMITE = 30        # máximo de 30 segundos por pregunta

def pedir_respuesta_con_tiempo():
    respuesta = [None]

    def obtener_respuesta():
        respuesta[0] = input("\n📝 Elegí la respuesta (número): ")

    hilo = threading.Thread(target=obtener_respuesta)
    hilo.start()
    hilo.join(timeout=TIEMPO_LIMITE)

    if hilo.is_alive():
        print("⏰ ¡Tiempo agotado!")
        hilo.join()  # Forzar a que termine
        return None
    return respuesta[0]

def hacerPregunta(nombre, pregunta):
    print(f"\n❓ {nombre}, respondé esta pregunta:")
    print(pregunta["pregunta"])

    opciones = pregunta["opciones"][:]
    random.shuffle(opciones)

    for i, opcion in enumerate(opciones):
        print(f"   {i+1}. {opcion}")

    tiempo_inicio = time.time()
    respuesta = pedir_respuesta_con_tiempo()
    tiempo_fin = time.time()

    tiempo_respuesta = tiempo_fin - tiempo_inicio

    if respuesta is None:
        print(f"❌ No respondiste a tiempo. Se suma una penalización de +{PENALIZACION_TIEMPO} segundos.")
        return False, TIEMPO_LIMITE + PENALIZACION_TIEMPO

    if respuesta.isdigit():
        indice = int(respuesta)
        if 1 <= indice <= len(opciones):
            seleccion = opciones[indice - 1]
            if seleccion == pregunta["respuestaCorrecta"]:
                print("✅ ¡Correcto!")
                return True, tiempo_respuesta
            else:
                print(f"❌ Incorrecto. La respuesta correcta era: {pregunta['respuestaCorrecta']}")
                return False, tiempo_respuesta + PENALIZACION_TIEMPO

    print("❌ Entrada inválida. Se cuenta como incorrecta.")
    return False, tiempo_respuesta + PENALIZACION_TIEMPO

def modoContraReloj():
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

    tiempo_total = 0
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
            tiempo_total += tiempo
            if fueCorrecta:
                correctas += 1
        else:
            print("🚫 No hay preguntas disponibles. Se penaliza con +10 segundos.")
            tiempo_total += PENALIZACION_TIEMPO

    print("\n🏁 ¡Fin del juego! Resultados:")
    print(f"⏱️ Tiempo total: {round(tiempo_total, 2)} segundos")
    print(f"✅ Respuestas correctas: {correctas} de 10")

    # Guardar resultado en el archivo puntuaciones.csv
    ranking.guardar_resultado(nombreJugador, correctas, round(tiempo_total, 2))

    input("\n🔄 Presiona Enter para volver al menú...")
