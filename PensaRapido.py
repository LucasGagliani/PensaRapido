import random

# Listas de categorías y dificultades
categorias = ["Historia", "Ciencia", "Deportes", "Geografía", "Arte"]
dificultades = ["Fácil", "Media", "Difícil"]

# Matriz vacía [categoría][dificultad] → lista de preguntas
# Cada pregunta: [enunciado, [opción1, opción2, opción3, opción4], correcta]
preguntas_matriz = [[[] for _ in dificultades] for _ in categorias]




# Hardcodeo de preguntas para probar modo 1v1

# ¡¡IMPORTANTE!! Aca falta hacer la funcionalidad para leer el txt con las preguntas y cargarlas en la matriz de preguntas
# una vez hecho esto, queda adaptar el codigo para que funcione con el txt y no con el hardcodeo




# Historia - Fácil
preguntas_matriz[0][0].append([
    "¿Quién fue el primer presidente de Argentina?",
    ["Manuel Belgrano", "Bernardino Rivadavia", "Juan Manuel de Rosas", "Domingo Sarmiento"],
    "Bernardino Rivadavia"
])
# Historia - Media
preguntas_matriz[0][1].append([
    "¿En qué año fue la Revolución Francesa?",
    ["1789", "1776", "1810", "1806"],
    "1789"
])
# Historia - Difícil
preguntas_matriz[0][2].append([
    "¿Cuál fue el emperador romano durante la erupción del Vesubio en el 79 d.C.?",
    ["Nerón", "Trajano", "Tito", "Augusto"],
    "Tito"
])

# Ciencia - Fácil
preguntas_matriz[1][0].append([
    "¿Cuál es el planeta más cercano al Sol?",
    ["Venus", "Mercurio", "Tierra", "Marte"],
    "Mercurio"
])

# Ciencia - Media
preguntas_matriz[1][1].append([
    "¿Cuál es la fórmula química del agua?",
    ["H2O", "CO2", "O2", "NaCl"],
    "H2O"
])

# Ciencia - Difícil
preguntas_matriz[1][2].append([
    "¿Qué partícula subatómica tiene carga negativa?",
    ["Protón", "Neutrón", "Electrón", "Positrón"],
    "Electrón"
])

# Deportes - Fácil
preguntas_matriz[2][0].append([
    "¿Cuántos jugadores hay en un equipo de fútbol?",
    ["7", "9", "11", "13"],
    "11"
])
# Deportes - Media
preguntas_matriz[2][1].append([
    "¿En qué deporte se utiliza una raqueta?",
    ["Fútbol", "Tenis", "Natación", "Ciclismo"],
    "Tenis"
])
# Deportes - Difícil
preguntas_matriz[2][2].append([
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
            num = int(entrada)
            if 1 <= num <= len(lista):
                return num - 1
        print("Entrada inválida. Probá de nuevo.")

# Mostrar una pregunta y verificar si el jugador responde bien
def hacerPregunta(jugador, preguntas):
    if len(preguntas) == 0:
        print("No hay preguntas disponibles.")
        return False
    pregunta = random.choice(preguntas)
    enunciado, opciones, correcta = pregunta
    print(f"\n{jugador}, te toca:")
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
    jugador1 = input("Nombre del Jugador 1: ")
    jugador2 = input("Nombre del Jugador 2: ")
    puntajes = [0, 0]

    rondas = 5
    for ronda in range(rondas):
        print(f"\n Ronda {ronda + 1} de {rondas}")

        # Turno Jugador 1
        print(f"\n{jugador1}, elegí una categoría:")
        cat_index = elegirOpcion(categorias)
        print("Elegí una dificultad:")
        dif_index = elegirOpcion(dificultades)
        if hacerPregunta(jugador1, preguntas_matriz[cat_index][dif_index]):
            puntajes[0] += (dif_index + 1) * 10

        # Turno Jugador 2
        print(f"\n{jugador2}, elegí una categoría:")
        cat_index = elegirOpcion(categorias)
        print("Elegí una dificultad:")
        dif_index = elegirOpcion(dificultades)
        if hacerPregunta(jugador2, preguntas_matriz[cat_index][dif_index]):
            puntajes[1] += (dif_index + 1) * 10

    # Resultados
    print("\n ¡Partida terminada!")
    print(f"{jugador1} → {puntajes[0]} puntos")
    print(f"{jugador2} → {puntajes[1]} puntos")
    if puntajes[0] > puntajes[1]:
        print(f" Ganó {jugador1}!")
    elif puntajes[1] > puntajes[0]:
        print(f" Ganó {jugador2}!")
    else:
        print(" ¡Empate!")

# Ejecutar el juego
modo1vs1()
