import random

# Listas de categorías y dificultades
categorias = ["Historia", "Ciencia", "Deportes", "Geografía", "Arte"]
dificultades = ["Fácil", "Media", "Difícil"]

# Matriz vacía [categoría][dificultad] → lista de preguntas
# Cada pregunta: [enunciado, [opcion1, opcion2, opcion3, opcion4], correcta]
preguntasMatriz = [[[] for _ in dificultades] for _ in categorias]

# Preguntas hardcodeadas para prueba del modo 1vs1

# Historia - Fácil
preguntasMatriz[0][0].append([
    "¿Quién fue el primer presidente de Argentina?",
    ["Manuel Belgrano", "Bernardino Rivadavia", "Juan Manuel de Rosas", "Domingo Sarmiento"],
    "Bernardino Rivadavia"
])
# Historia - Media
preguntasMatriz[0][1].append([
    "¿En qué año fue la Revolución Francesa?",
    ["1789", "1776", "1810", "1806"],
    "1789"
])
# Historia - Difícil
preguntasMatriz[0][2].append([
    "¿Cuál fue el emperador romano durante la erupción del Vesubio en el 79 d.C.?",
    ["Nerón", "Trajano", "Tito", "Augusto"],
    "Tito"
])

# Ciencia - Fácil
preguntasMatriz[1][0].append([
    "¿Cuál es el planeta más cercano al Sol?",
    ["Venus", "Mercurio", "Tierra", "Marte"],
    "Mercurio"
])
# Ciencia - Media
preguntasMatriz[1][1].append([
    "¿Cuál es la fórmula química del agua?",
    ["H2O", "CO2", "O2", "NaCl"],
    "H2O"
])
# Ciencia - Difícil
preguntasMatriz[1][2].append([
    "¿Qué partícula subatómica tiene carga negativa?",
    ["Protón", "Neutrón", "Electrón", "Positrón"],
    "Electrón"
])

# Deportes - Fácil
preguntasMatriz[2][0].append([
    "¿Cuántos jugadores hay en un equipo de fútbol?",
    ["7", "9", "11", "13"],
    "11"
])
# Deportes - Media
preguntasMatriz[2][1].append([
    "¿En qué deporte se utiliza una raqueta?",
    ["Fútbol", "Tenis", "Natación", "Ciclismo"],
    "Tenis"
])
# Deportes - Difícil
preguntasMatriz[2][2].append([
    "¿Quién ganó el Mundial de Fútbol de 1986?",
    ["Brasil", "Argentina", "Alemania", "Italia"],
    "Argentina"
])

# Mostrar opciones por número y validar elección
def elegirOpcion(lista):
    for i in range(len(lista)):
        print(f"{i+1}. {lista[i]}")
    while True:
        entrada = input("Elegí una opción (número): ")
        if entrada.isdigit():
            numero = int(entrada)
            if 1 <= numero <= len(lista):
                return numero - 1
        print("Entrada inválida. Probá de nuevo.")

# Mostrar una pregunta y verificar si el jugador responde bien
def hacerPregunta(nombreJugador, listaPreguntas):
    if len(listaPreguntas) == 0:
        print("No hay preguntas disponibles.")
        return False
    pregunta = random.choice(listaPreguntas)
    enunciado, opciones, correcta = pregunta
    print(f"\n{nombreJugador}, te toca:")
    print(f"Pregunta: {enunciado}")
    for i in range(4):
        print(f"{i+1}. {opciones[i]}")
    while True:
        respuesta = input("Elegí la respuesta (número): ")
        if respuesta.isdigit() and 1 <= int(respuesta) <= 4:
            seleccion = opciones[int(respuesta) - 1]
            if seleccion == correcta:
                print("¡Correcto!")
                return True
            else:
                print(f"Incorrecto. La respuesta correcta era: {correcta}")
                return False
        print("Respuesta inválida. Intentá de nuevo.")

# Lógica principal del juego 1vs1
def modo1vs1():
    print("\n¡Bienvenidos al modo 1vs1!")
    nombreJugador1 = input("Nombre del Jugador 1: ")
    nombreJugador2 = input("Nombre del Jugador 2: ")
    puntajes = [0, 0]

    rondas = 5
    for ronda in range(rondas):
        print(f"\nRonda {ronda + 1} de {rondas}")

        # Turno Jugador 1
        print(f"\n{nombreJugador1}, elegí una categoría:")
        catIndex = elegirOpcion(categorias)
        print("Elegí una dificultad:")
        difIndex = elegirOpcion(dificultades)
        if hacerPregunta(nombreJugador1, preguntasMatriz[catIndex][difIndex]):
            puntajes[0] += (difIndex + 1) * 10

        # Turno Jugador 2
        print(f"\n{nombreJugador2}, elegí una categoría:")
        catIndex = elegirOpcion(categorias)
        print("Elegí una dificultad:")
        difIndex = elegirOpcion(dificultades)
        if hacerPregunta(nombreJugador2, preguntasMatriz[catIndex][difIndex]):
            puntajes[1] += (difIndex + 1) * 10

    # Resultados
    print("\n¡Partida terminada!")
    print(f"{nombreJugador1} → {puntajes[0]} puntos")
    print(f"{nombreJugador2} → {puntajes[1]} puntos")
    if puntajes[0] > puntajes[1]:
        print(f"¡Ganó {nombreJugador1}!")
    elif puntajes[1] > puntajes[0]:
        print(f"¡Ganó {nombreJugador2}!")
    else:
        print("¡Empate!")

# Ejecutar el juego
modo1vs1()
