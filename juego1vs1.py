import funcionesTxt
import random
import ranking

# Cargar preguntas al inicio del módulo
funcionesTxt.leerPreguntas()
preguntasTupla = funcionesTxt.preguntasTupla

validar_nombre = lambda nombre: nombre != "" and nombre.isalpha() and len(nombre) >= 3 and len(nombre) <= 20

def pedirNombre(jugador_num):
    while True:
        print("🎮--------------------------------------------------")
        nombre = input(f"🧑 Nombre del Jugador {jugador_num}: ")
        if not validar_nombre(nombre):
            print("⚠️ El nombre solo debe contener letras, sin espacios, símbolos, ni números. Intentá de nuevo.")
        else:
            print(f"✅ ¡Bienvenido/a, {nombre}! 🎉")
            print("--------------------------------------------------🎮")
            return nombre

def mostrarOpciones(lista):
    for i in range(len(lista)):
        print(f"   {i+1}. {lista[i].capitalize()} 🎯")
    while True:
        entrada = input("👉 Elegí una opción (número): ")
        if entrada.isdigit():
            numero = int(entrada)
            if 1 <= numero <= len(lista):
                return numero - 1
        print("❌ Entrada inválida. Probá de nuevo.")

def hacerPreguntaAleatoria(preguntasMatriz):
    categorias = ['geografía', 'historia', 'ciencia', 'deporte', 'arte']
    dificultades = ['facil', 'media', 'dificil']

    print("\n🌍 Selecciona una categoría:")
    categoriaIndex = mostrarOpciones(categorias)

    print("\n⚙️ Selecciona una dificultad:")
    dificultadIndex = mostrarOpciones(dificultades)

    preguntasDisponibles = preguntasMatriz[dificultadIndex][categoriaIndex]

    if len(preguntasDisponibles) == 0:
        print("\n🚫 No hay preguntas disponibles en esta categoría y dificultad.")
        return None

    pregunta = random.choice(preguntasDisponibles)
    print("\n🧠 Pregunta seleccionada:")
    print(f"❓ {pregunta['pregunta']}")

    opciones = pregunta['opciones'][:]
    random.shuffle(opciones)

    print("\n📌 Opciones:")
    for i, opcion in enumerate(opciones):
        print(f"   {i+1}. {opcion}")

    while True:
        respuesta = input("\n📝 Elegí la respuesta (número): ")
        if respuesta.isdigit() and 1 <= int(respuesta) <= len(opciones):
            seleccion = opciones[int(respuesta) - 1]
            if seleccion == pregunta['respuestaCorrecta']:
                print("🎉 ¡Correcto!")
                return True
            else:
                print(f"❌ Incorrecto. La respuesta correcta era: {pregunta['respuestaCorrecta']}")
                return False
        print("❗ Entrada inválida. Intentá de nuevo.")

def modo1vs1():
    print("\n🕹️ Bienvenidos al modo *1 vs 1*! 🕹️")
    print("🔥 Que gane el mejor... ¡A jugar!\n")

    nombreJugador1 = pedirNombre(1)
    nombreJugador2 = pedirNombre(2)
    puntajes = [0, 0]

    categorias = ['geografía', 'historia', 'ciencia', 'deporte', 'arte']
    dificultades = ['facil', 'media', 'dificil']
    rondas = 5

    preguntasUsadas = []

    for ronda in range(rondas):
        print(f"\n🎲 Ronda {ronda + 1} de {rondas}")
        print("--------------------------------------------------")

        # Turno Jugador 1
        print(f"\n🔵 Turno de {nombreJugador1}")
        print("📚 Elegí una categoría:")
        categoriaIndex = mostrarOpciones(categorias)
        print("\n⚙️ Elegí una dificultad:")
        dificultadIndex = mostrarOpciones(dificultades)

        preguntasDisponibles = preguntasTupla[dificultadIndex][categoriaIndex]
        preguntasFiltradas = [p for p in preguntasDisponibles if p not in preguntasUsadas]

        if not preguntasFiltradas:
            print("🚫 No hay más preguntas disponibles sin repetir en esta categoría y dificultad.")
            # Seleccionar cualquier pregunta si no hay disponibles sin repetir
            if preguntasDisponibles:
                preguntaSeleccionada = random.choice(preguntasDisponibles)
            else:
                print("⚠️ No hay preguntas en esta categoría/dificultad. Saltando turno.")
                continue
        else:
            preguntaSeleccionada = random.choice(preguntasFiltradas)
        
        preguntasUsadas.append(preguntaSeleccionada)
        print(f"\n❓ {preguntaSeleccionada['pregunta']}")
        
        opciones = preguntaSeleccionada['opciones'][:]
        random.shuffle(opciones)

        print("\n🔢 Opciones:")
        for i, opcion in enumerate(opciones):
            print(f"   {i+1}. {opcion}")
        
        while True:
            respuesta = input("\n👉 Elegí la respuesta (número): ")
            if respuesta.isdigit() and 1 <= int(respuesta) <= len(opciones):
                seleccion = opciones[int(respuesta) - 1]
                if seleccion == preguntaSeleccionada['respuestaCorrecta']:
                    print("✅ ¡Correcto!")
                    puntajes[0] += (dificultadIndex + 1) * 10
                else:
                    print(f"❌ Incorrecto. La respuesta correcta era: {preguntaSeleccionada['respuestaCorrecta']}")
                break
            print("❗ Entrada inválida. Intentá de nuevo.")

        # Turno Jugador 2
        print(f"\n🔴 Turno de {nombreJugador2}")
        print("📚 Elegí una categoría:")
        categoriaIndex = mostrarOpciones(categorias)
        print("\n⚙️ Elegí una dificultad:")
        dificultadIndex = mostrarOpciones(dificultades)

        preguntasDisponibles = preguntasTupla[dificultadIndex][categoriaIndex]
        preguntasFiltradas = [p for p in preguntasDisponibles if p not in preguntasUsadas]

        if not preguntasFiltradas:
            print("🚫 No hay más preguntas disponibles sin repetir en esta categoría y dificultad.")
            if preguntasDisponibles:
                preguntaSeleccionada = random.choice(preguntasDisponibles)
            else:
                print("⚠️ No hay preguntas en esta categoría/dificultad. Saltando turno.")
                continue
        else:
            preguntaSeleccionada = random.choice(preguntasFiltradas)
        
        preguntasUsadas.append(preguntaSeleccionada)
        print(f"\n❓ {preguntaSeleccionada['pregunta']}")
        
        opciones = preguntaSeleccionada['opciones'][:]
        random.shuffle(opciones)

        print("\n🔢 Opciones:")
        for i, opcion in enumerate(opciones):
            print(f"   {i+1}. {opcion}")
        
        while True:
            respuesta = input("\n👉 Elegí la respuesta (número): ")
            if respuesta.isdigit() and 1 <= int(respuesta) <= len(opciones):
                seleccion = opciones[int(respuesta) - 1]
                if seleccion == preguntaSeleccionada['respuestaCorrecta']:
                    print("✅ ¡Correcto!")
                    puntajes[1] += (dificultadIndex + 1) * 10
                else:
                    print(f"❌ Incorrecto. La respuesta correcta era: {preguntaSeleccionada['respuestaCorrecta']}")
                break
            print("❗ Entrada inválida. Intentá de nuevo.")

    # Resultado final
    print("\n🎉 ¡Partida terminada! 🎉")
    print("--------------------------------------------------")
    print(f"🏆 Puntajes finales:")
    print(f"   🔵 {nombreJugador1}: {puntajes[0]} puntos")
    print(f"   🔴 {nombreJugador2}: {puntajes[1]} puntos")
    print("--------------------------------------------------")
    
    # Desempate si hay empate
    if puntajes[0] == puntajes[1]:
        print("\n⚡ ¡Empate! Vamos a un desempate rápido. ⚡")
        while puntajes[0] == puntajes[1]:
            print(f"\n🔵 Turno de desempate para {nombreJugador1}")
            if hacerPreguntaAleatoria(preguntasTupla) is not None:
                if hacerPreguntaAleatoria(preguntasTupla):
                    puntajes[0] += 10

            print(f"\n🔴 Turno de desempate para {nombreJugador2}")
            if hacerPreguntaAleatoria(preguntasTupla) is not None:
                if hacerPreguntaAleatoria(preguntasTupla):
                    puntajes[1] += 10

            print(f"\n⚖️ Puntajes de desempate: {nombreJugador1}: {puntajes[0]} - {nombreJugador2}: {puntajes[1]}")

    # Determinar ganador
    if puntajes[0] > puntajes[1]:
        print(f"\n🥇 ¡Ganó {nombreJugador1}! 🏆")
        ranking.guardar_resultado(nombreJugador1, puntajes[0], "1vs1")
    else:
        print(f"\n🥇 ¡Ganó {nombreJugador2}! 🏆")
        ranking.guardar_resultado(nombreJugador2, puntajes[1], "1vs1")
    
    print("--------------------------------------------------")
    input("🔄 Presiona Enter para volver al menú...")