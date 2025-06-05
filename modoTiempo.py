import funcionesTxt
import random
import time
import threading
import juego1vs1
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
    print("\n⏱️ ¡Bienvenidos al modo *Contra Reloj*!")
    print("🎯 Cada jugador responderá 5 preguntas con un límite de 30 segundos por pregunta.")
    print("❌ Cada error o entrada inválida suma +10 segundos al tiempo total.\n")

    nombreJugador1 = juego1vs1.pedirNombre(1)
    nombreJugador2 = juego1vs1.pedirNombre(2)

    categorias = ['geografía', 'historia', 'ciencia', 'deporte', 'arte']
    dificultades = ['facil', 'media', 'dificil']

    tiempos_totales = [0, 0]
    correctas = [0, 0]
    preguntasUsadas = []

    for turno in range(5):
        for idx, nombre in enumerate([nombreJugador1, nombreJugador2]):
            print(f"\n🎯 Turno {turno + 1} para {nombre}")

            categoriaIndex = random.randint(0, len(categorias) - 1)
            dificultadIndex = random.randint(0, len(dificultades) - 1)

            preguntasDisponibles = preguntasMatriz[dificultadIndex][categoriaIndex]
            preguntasFiltradas = [p for p in preguntasDisponibles if p not in preguntasUsadas]

            if preguntasFiltradas:
                pregunta = random.choice(preguntasFiltradas)
                preguntasUsadas.append(pregunta)
                fueCorrecta, tiempo = hacerPregunta(nombre, pregunta)
                tiempos_totales[idx] += tiempo
                if fueCorrecta:
                    correctas[idx] += 1
            else:
                print("🚫 No hay preguntas disponibles. Se penaliza con +10 segundos.")
                tiempos_totales[idx] += PENALIZACION_TIEMPO

    print("\n🏁 ¡Fin del juego! Resultados:")
    print(f"🔵 {nombreJugador1}: ⏱️ {round(tiempos_totales[0], 2)} segundos totales - {correctas[0]} correctas")
    print(f"🔴 {nombreJugador2}: ⏱️ {round(tiempos_totales[1], 2)} segundos totales - {correctas[1]} correctas")

    # Guardar resultados ordenados por puntaje y tiempo
    ranking.guardar_resultado(nombreJugador1, correctas[0], round(tiempos_totales[0], 2))
    ranking.guardar_resultado(nombreJugador2, correctas[1], round(tiempos_totales[1], 2))

    if (correctas[0] > correctas[1]) or (correctas[0] == correctas[1] and tiempos_totales[0] < tiempos_totales[1]):
        print(f"\n🏆 ¡Ganó {nombreJugador1} con mejor puntaje y/o tiempo!")
    elif (correctas[1] > correctas[0]) or (correctas[1] == correctas[0] and tiempos_totales[1] < tiempos_totales[0]):
        print(f"\n🏆 ¡Ganó {nombreJugador2} con mejor puntaje y/o tiempo!")
    else:
        print("\n🤝 ¡Empate!")

    input("\n🔄 Presiona Enter para volver al menú...")
