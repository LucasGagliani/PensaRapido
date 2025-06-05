import csv
import os
from datetime import datetime

RANKING_1VS1_FILE = "ranking_1vs1.csv"
RANKING_TIEMPO_FILE = "ranking_tiempo.csv"
MAX_RANKING_ENTRIES = 20

def guardar_resultado(nombre, puntaje, modo_juego, tiempo=None):
    """
    Guarda un resultado en el archivo de ranking correspondiente.
    """
    try:
        # Determinar qué archivo usar
        ranking_file = RANKING_TIEMPO_FILE if modo_juego == "ContraReloj" else RANKING_1VS1_FILE
        
        # Crear el archivo si no existe
        if not os.path.exists(ranking_file):
            with open(ranking_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                if modo_juego == "ContraReloj":
                    writer.writerow(["Fecha", "Nombre", "Preguntas Correctas", "Tiempo Total", "Modo"])
                else:
                    writer.writerow(["Fecha", "Nombre", "Puntaje", "Modo"])
        
        # Leer el archivo existente
        resultados = []
        with open(ranking_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Saltar la cabecera
            resultados = list(reader)
        
        # Agregar el nuevo resultado
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if modo_juego == "ContraReloj":
            resultados.append([fecha_actual, nombre, str(puntaje), str(tiempo), modo_juego])
        else:
            resultados.append([fecha_actual, nombre, str(puntaje), modo_juego])
        
        # Ordenar según el modo de juego
        if modo_juego == "ContraReloj":
            # Ordenar por más preguntas correctas y menor tiempo
            resultados.sort(key=lambda x: (-int(x[2]), float(x[3])))
        else:
            # Ordenar por mayor puntaje
            resultados.sort(key=lambda x: -int(x[2]))
        
        # Mantener solo los mejores MAX_RANKING_ENTRIES resultados
        resultados = resultados[:MAX_RANKING_ENTRIES]
        
        # Escribir de vuelta al archivo
        with open(ranking_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if modo_juego == "ContraReloj":
                writer.writerow(["Fecha", "Nombre", "Preguntas Correctas", "Tiempo Total", "Modo"])
            else:
                writer.writerow(["Fecha", "Nombre", "Puntaje", "Modo"])
            writer.writerows(resultados)
            
    except Exception as e:
        print(f"❌ Error al guardar el ranking: {e}")

def mostrarRanking():
    """
    Muestra el ranking seleccionado por el usuario.
    """
    try:
        while True:
            limpiarConsola()
            print("\n" + "=" * 70)
            print("🏆 SELECCIONAR TIPO DE RANKING 🏆")
            print("=" * 70)
            print("\n1️⃣ Ranking Modo 1vs1 (por puntaje)")
            print("2️⃣ Ranking Modo Contra Reloj (por preguntas correctas y tiempo)")
            print("3️⃣ Volver al menú principal")
            print("=" * 70 + "\n")
            
            opcion = input("👉 Elige una opción: ")
            
            if opcion == "1":
                mostrar_ranking_1vs1()
            elif opcion == "2":
                mostrar_ranking_tiempo()
            elif opcion == "3":
                return
            else:
                print("❌ Opción inválida. Por favor, elige 1, 2 o 3.")
                input("🔄 Presiona Enter para continuar...")
                
    except Exception as e:
        print(f"\n❌ Error al mostrar el ranking: {e}")
        input("🔄 Presiona Enter para volver al menú...")

def mostrar_ranking_1vs1():
    """
    Muestra el ranking del modo 1vs1 ordenado por puntaje.
    """
    try:
        limpiarConsola()
        print("\n" + "=" * 70)
        print("🏆 RANKING MODO 1VS1 (MEJORES PUNTAJES) 🏆")
        print("=" * 70)
        
        if not os.path.exists(RANKING_1VS1_FILE):
            print("\nℹ️ No hay registros en el ranking 1vs1 todavía.")
            print("¡Juega en modo 1vs1 para aparecer aquí!")
            print("=" * 70 + "\n")
            input("🔄 Presiona Enter para volver...")
            return
        
        with open(RANKING_1VS1_FILE, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Saltar la cabecera
            
            print("\n{:<5} {:<20} {:<15} {:<20}".format(
                "Pos.", "Nombre", "Puntaje", "Fecha"))
            print("-" * 70)
            
            for i, row in enumerate(reader, start=1):
                fecha, nombre, puntaje, modo = row
                fecha_corta = fecha.split()[0]
                print("{:<5} {:<20} {:<15} {:<20}".format(
                    f"{i}°", nombre[:18], puntaje, fecha_corta))
                
                if i >= MAX_RANKING_ENTRIES:
                    break
        
        print("=" * 70 + "\n")
        input("🔄 Presiona Enter para volver...")
        
    except Exception as e:
        print(f"\n❌ Error al leer el ranking 1vs1: {e}")
        input("🔄 Presiona Enter para volver...")

def mostrar_ranking_tiempo():
    """
    Muestra el ranking del modo Contra Reloj ordenado por preguntas correctas y tiempo.
    """
    try:
        limpiarConsola()
        print("\n" + "=" * 70)
        print("🏆 RANKING MODO CONTRA RELOJ 🏆")
        print("=" * 70)
        print("(Ordenado por más preguntas correctas y menor tiempo)")
        print("=" * 70)
        
        if not os.path.exists(RANKING_TIEMPO_FILE):
            print("\nℹ️ No hay registros en el ranking Contra Reloj todavía.")
            print("¡Juega en modo Contra Reloj para aparecer aquí!")
            print("=" * 70 + "\n")
            input("🔄 Presiona Enter para volver...")
            return
        
        with open(RANKING_TIEMPO_FILE, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Saltar la cabecera
            
            print("\n{:<5} {:<20} {:<10} {:<15} {:<20}".format(
                "Pos.", "Nombre", "Correctas", "Tiempo (s)", "Fecha"))
            print("-" * 70)
            
            for i, row in enumerate(reader, start=1):
                fecha, nombre, correctas, tiempo, modo = row
                fecha_corta = fecha.split()[0]
                tiempo_formateado = f"{float(tiempo):.2f}"
                print("{:<5} {:<20} {:<10} {:<15} {:<20}".format(
                    f"{i}°", nombre[:18], correctas, tiempo_formateado, fecha_corta))
                
                if i >= MAX_RANKING_ENTRIES:
                    break
        
        print("=" * 70 + "\n")
        input("🔄 Presiona Enter para volver...")
        
    except Exception as e:
        print(f"\n❌ Error al leer el ranking Contra Reloj: {e}")
        input("🔄 Presiona Enter para volver...")

def limpiarConsola():
    """Limpia la consola dependiendo del sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')