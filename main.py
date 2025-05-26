import os
import juego1vs1
import reglas
import ranking
import modoTiempo


def limpiarConsola():
    """Limpia la consola dependiendo del sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrarMenu():
    print("\n" + "=" * 70)
    print("🎉  BIENVENIDO AL JUEGO DE PREGUNTAS Y RESPUESTAS:  ¡PENSÁ RÁPIDO! 🎉")
    print("=" * 70)
    print("📋 MENÚ PRINCIPAL:")
    print("1️⃣  Jugar Modo 1 vs 1")
    print("2️⃣  Jugar Modo por Tiempo")  # Activar cuando esté implementado
    print("3️⃣  Ver Ranking")            # Activar cuando esté implementado
    print("4️⃣  Ver Reglas del Juego")
    print("5️⃣  Salir")
    print("=" * 70 + "\n")

# Bucle principal del menú
while True:
    limpiarConsola()
    mostrarMenu()
    opcion = input("👉 Elige una opción: ")

    if opcion == "1":
        juego1vs1.modo1vs1()
    elif opcion == "2":
        modoTiempo.modoContraReloj()
    elif opcion == "3":
        ranking.mostrarRanking() 
    elif opcion == "4":
        reglas.mostrarReglas()
    elif opcion == "5":
        print("👋 Saliendo del programa... ¡Gracias por jugar!")
        break
    else:
        print("❌ Opción inválida. Por favor, elige una opción del 1 al 5.")
