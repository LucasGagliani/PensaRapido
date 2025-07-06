import tkinter as tk
from tkinter import scrolledtext


def mostrar_reglas_gui():
    ventana = tk.Toplevel()
    ventana.title("📜 Reglas del Juego")
    ventana.geometry("900x600")
    ventana.configure(bg="white")

    tk.Label(
        ventana, text="📜 REGLAS DE PENSÁ RÁPIDO", font=("Helvetica", 16, "bold"),
        bg="white"
    ).pack(pady=10)

    texto = """
🎉 ¡BIENVENIDO A PENSÁ RÁPIDO! 🎉

🧠 JUEGO DE PREGUNTAS Y RESPUESTAS:
- Las preguntas están organizadas por categorías y niveles.
- Elegí una categoría y dificultad para responder.
- Ingresá el número de la opción que consideres correcta.

🎮 MODOS DE JUEGO:

⏱️ Modo por Tiempo:
- Responde preguntas aleatorias antes de que se acabe el tiempo.
- Las respuestas incorrectas agregan +10 segundos.
- Se muestra un ranking con los 20 mejores tiempos.

🤜🤛 Modo 1 vs 1:
- Dos jugadores se turnan para responder.
- Puntos por respuesta correcta:
  🟢 Fácil: +10 puntos
  🟡 Media: +20 puntos
  🔴 Difícil: +30 puntos
- Gana quien tenga más puntos al final.

📈 RANKING:
- Al finalizar el modo por tiempo, tu resultado se guarda en 'puntuaciones.csv'.
- Se muestran los 20 mejores tiempos y también el historial de partidas del modo 1vs1.

🎊 ¡Divertite y pensá rápido!
"""

    texto_area = scrolledtext.ScrolledText(
        ventana, wrap=tk.WORD, font=("Helvetica", 12), width=80, height=22, bg="#f8f8f8"
    )
    texto_area.insert(tk.END, texto)
    texto_area.configure(state='disabled')
    texto_area.pack(padx=20, pady=20)

    tk.Button(ventana, text="Cerrar",font=("Helvetica", 14), width=30, command=ventana.destroy).pack(pady=5)
