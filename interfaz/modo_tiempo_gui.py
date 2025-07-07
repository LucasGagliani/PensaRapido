import sys
import os
sys.path.append(os.path.abspath("./"))

import tkinter as tk
from tkinter import messagebox
import random
import funcionesTxt
import ranking

PENALIZACION_TIEMPO = 10
TIEMPO_LIMITE = 30

def iniciar_modo_tiempo(ventana_anterior):
    ventana_anterior.destroy()

    funcionesTxt.leerPreguntas()
    preguntas_matriz = funcionesTxt.preguntasTupla
    preguntas_usadas = []
    correctas = 0
    tiempo_total = 0
    turno = {"valor": 0}
    temporizador = {"tiempo": TIEMPO_LIMITE, "after_id": None}
    pregunta_actual = {}
    nombre_jugador = ""

    ventana = tk.Tk()
    ventana.title("Modo Contra Reloj")
    ventana.geometry("700x500")
    ventana.configure(bg="#f0f0f0")

    # Widgets globales
    pregunta_lbl = tk.Label(ventana, text="", font=("Helvetica", 16), wraplength=600, bg="#f0f0f0")
    opciones_btns = [tk.Button(ventana, text="", font=("Helvetica", 12), width=60) for _ in range(4)]
    feedback_lbl = tk.Label(ventana, text="", font=("Helvetica", 14), bg="#f0f0f0")
    tiempo_lbl = tk.Label(ventana, text="", font=("Helvetica", 12), fg="red", bg="#f0f0f0")

    def pedir_nombre():
        nonlocal nombre_jugador
        nombre_jugador = nombre_entry.get().strip()
        if not nombre_jugador:
            nombre_jugador = "Jugador"
        nombre_ventana.destroy()
        ventana.deiconify()
        siguiente_turno()

    nombre_ventana = tk.Toplevel()
    nombre_ventana.title("Ingresar Nombre")
    nombre_ventana.geometry("300x150")
    tk.Label(nombre_ventana, text="👤 Ingresá tu nombre:").pack(pady=10)
    nombre_entry = tk.Entry(nombre_ventana)
    nombre_entry.pack()
    tk.Button(nombre_ventana, text="Comenzar", command=pedir_nombre).pack(pady=10)
    ventana.withdraw()

    def siguiente_turno():
        nonlocal tiempo_total
        if turno["valor"] >= 10:
            finalizar()
            return

        dificultad = random.randint(0, 2)
        categoria = random.randint(0, 4)
        disponibles = preguntas_matriz[dificultad][categoria]
        filtradas = [p for p in disponibles if p not in preguntas_usadas]

        if filtradas:
            pregunta = random.choice(filtradas)
            preguntas_usadas.append(pregunta)
            mostrar_pregunta(pregunta)
        else:
            tiempo_total += PENALIZACION_TIEMPO
            turno["valor"] += 1
            siguiente_turno()

    def mostrar_pregunta(pregunta):
        pregunta_actual.clear()
        pregunta_actual.update(pregunta)

        pregunta_lbl.config(text=f"❓ {pregunta['pregunta']}")
        pregunta_lbl.pack(pady=10)

        opciones = pregunta["opciones"][:]
        random.shuffle(opciones)

        for i, opcion in enumerate(opciones):
            opciones_btns[i].config(
                text=opcion,
                state="normal",
                command=lambda opt=opcion: responder(opt)
            )
            opciones_btns[i].pack(pady=3)

        feedback_lbl.config(text="", fg="black")
        feedback_lbl.pack(pady=10)
        tiempo_lbl.pack(pady=5)

        temporizador["tiempo"] = TIEMPO_LIMITE
        actualizar_tiempo()

    def actualizar_tiempo():
        tiempo_lbl.config(text=f"⏳ Tiempo: {temporizador['tiempo']}s")
        if temporizador["tiempo"] > 0:
            temporizador["tiempo"] -= 1
            temporizador["after_id"] = ventana.after(1000, actualizar_tiempo)
        else:
            messagebox.showinfo("⏰ Tiempo agotado", "+10 segundos")
            procesar_respuesta(None)

    def responder(opcion):
        procesar_respuesta(opcion)

    def procesar_respuesta(opcion):
        nonlocal correctas, tiempo_total
        if temporizador["after_id"]:
            ventana.after_cancel(temporizador["after_id"])

        correcta = pregunta_actual["respuestaCorrecta"]
        if opcion == correcta:
            correctas += 1
            tiempo_total += TIEMPO_LIMITE - temporizador["tiempo"]
            feedback_lbl.config(text="✅ ¡Correcto!", fg="green")
        else:
            tiempo_total += PENALIZACION_TIEMPO
            feedback_lbl.config(text=f"❌ Incorrecto. Era: {correcta}", fg="red")

        for btn in opciones_btns:
            btn.config(state="disabled")

        turno["valor"] += 1
        ventana.after(1500, siguiente_turno)

    def finalizar():
        for widget in ventana.winfo_children():
            widget.pack_forget()

        resumen = f"🎯 Fin del juego\n👤 {nombre_jugador}\n✅ Correctas: {correctas}/10\n⏱️ Tiempo total: {round(tiempo_total, 2)}s"
        tk.Label(ventana, text=resumen, font=("Helvetica", 16), bg="#f0f0f0").pack(pady=30)
        tk.Button(ventana, text="Salir", command=ventana.destroy).pack(pady=20)

        # Guardar ranking
        ranking.guardar_resultado(nombre_jugador, correctas, round(tiempo_total, 2))

    ventana.mainloop()
