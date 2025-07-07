import sys
import os
sys.path.append(os.path.abspath("./"))
import tkinter as tk
from tkinter import messagebox
import random
import funcionesTxt

def iniciar_modo_1vs1(ventana_anterior):
    ventana_anterior.destroy()
    funcionesTxt.leerPreguntas()
    preguntasTupla = funcionesTxt.preguntasTupla
    preguntas_usadas = []

    ventana = tk.Tk()
    ventana.title("Modo 1 vs 1")
    ventana.geometry("700x500")
    ventana.configure(bg="#f0f0f0")

    frame = tk.Frame(ventana, bg="#f0f0f0")
    frame.pack(expand=True, fill="both")

    nombre1 = tk.StringVar()
    nombre2 = tk.StringVar()
    puntajes = [0, 0]
    turno = [0]  # valor mutable
    jugador_actual = [0]  # 0: jugador 1, 1: jugador 2

    def pedir_nombres():
        limpiar_pantalla()
        tk.Label(frame, text="👤 Ingresá el nombre del Jugador 1:", font=("Helvetica", 14), bg="#f0f0f0").pack(pady=10)
        tk.Entry(frame, textvariable=nombre1, font=("Helvetica", 14)).pack(pady=5)

        tk.Label(frame, text="👤 Ingresá el nombre del Jugador 2:", font=("Helvetica", 14), bg="#f0f0f0").pack(pady=10)
        tk.Entry(frame, textvariable=nombre2, font=("Helvetica", 14)).pack(pady=5)

        tk.Button(frame, text="🎮 Iniciar Juego", font=("Helvetica", 14), command=iniciar_ronda).pack(pady=20)

    def iniciar_ronda():
        if not nombre1.get().isalpha() or not nombre2.get().isalpha():
            messagebox.showerror("Error", "Los nombres deben contener solo letras.")
            return
        mostrar_turno()

    def mostrar_turno():
        limpiar_pantalla()
        jugador = nombre1.get() if jugador_actual[0] == 0 else nombre2.get()
        tk.Label(frame, text=f"🎯 Ronda {turno[0] + 1} - Turno de {jugador}", font=("Helvetica", 16), bg="#f0f0f0").pack(pady=10)

        categorias = ['geografía', 'historia', 'ciencia', 'deporte', 'arte']
        dificultades = ['facil', 'media', 'dificil']

        tk.Label(frame, text="📚 Elegí una categoría:", font=("Helvetica", 14), bg="#f0f0f0").pack()
        for i, cat in enumerate(categorias):
            tk.Button(frame, text=cat.capitalize(), font=("Helvetica", 12),
                      command=lambda i=i: elegir_dificultad(i)).pack(pady=2)

    def elegir_dificultad(categoria_idx):
        limpiar_pantalla()
        dificultades = ['facil', 'media', 'dificil']
        tk.Label(frame, text="⚙️ Elegí una dificultad:", font=("Helvetica", 14), bg="#f0f0f0").pack()
        for i, dif in enumerate(dificultades):
            tk.Button(frame, text=dif.capitalize(), font=("Helvetica", 12),
                      command=lambda i=i, c=categoria_idx: mostrar_pregunta(i, c)).pack(pady=2)

    def mostrar_pregunta(dificultad, categoria):
        limpiar_pantalla()
        preguntas = preguntasTupla[dificultad][categoria]
        disponibles = [p for p in preguntas if p not in preguntas_usadas]

        if not disponibles:
            messagebox.showinfo("Sin preguntas", "No hay preguntas disponibles en esa categoría/dificultad.")
            avanzar_turno()
            return

        pregunta = random.choice(disponibles)
        preguntas_usadas.append(pregunta)

        tk.Label(frame, text=pregunta["pregunta"], wraplength=600, font=("Helvetica", 14), bg="#f0f0f0").pack(pady=10)
        opciones = pregunta["opciones"][:]
        random.shuffle(opciones)

        for opcion in opciones:
            tk.Button(frame, text=opcion, font=("Helvetica", 12),
                      command=lambda opt=opcion, correcta=pregunta["respuestaCorrecta"], dif=dificultad: responder(opt, correcta, dif)).pack(pady=5)

    def responder(opcion, correcta, dificultad):
        jugador = nombre1.get() if jugador_actual[0] == 0 else nombre2.get()

        if opcion == correcta:
            puntos = (dificultad + 1) * 10
            puntajes[jugador_actual[0]] += puntos
            messagebox.showinfo("✅ Correcto", f"¡Bien hecho, {jugador}! +{puntos} puntos")
        else:
            messagebox.showinfo("❌ Incorrecto", f"La respuesta correcta era: {correcta}")

        avanzar_turno()

    def avanzar_turno():
        if jugador_actual[0] == 1:
            turno[0] += 1
        if turno[0] >= 5:
            mostrar_resultado()
        else:
            jugador_actual[0] = 1 - jugador_actual[0]
            mostrar_turno()

    def mostrar_resultado():
        limpiar_pantalla()
        p1 = puntajes[0]
        p2 = puntajes[1]
        n1 = nombre1.get()
        n2 = nombre2.get()

        tk.Label(frame, text="🏁 Juego terminado", font=("Helvetica", 18), bg="#f0f0f0").pack(pady=20)
        tk.Label(frame, text=f"🔵 {n1}: {p1} puntos", font=("Helvetica", 14), bg="#f0f0f0").pack(pady=5)
        tk.Label(frame, text=f"🔴 {n2}: {p2} puntos", font=("Helvetica", 14), bg="#f0f0f0").pack(pady=5)

        if p1 > p2:
            ganador = n1
        elif p2 > p1:
            ganador = n2
        else:
            ganador = "Empate"

        tk.Label(frame, text=f"🏆 Ganador: {ganador}", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=15)
        tk.Button(frame, text="Salir", font=("Helvetica", 14), command=ventana.destroy).pack(pady=10)

    def limpiar_pantalla():
        for widget in frame.winfo_children():
            widget.destroy()

    pedir_nombres()
    ventana.mainloop()
