import tkinter as tk
from tkinter import messagebox
from modo_tiempo_gui import iniciar_modo_tiempo
from juego1vs1_gui import iniciar_modo_1vs1
from ver_ranking_gui import ver_ranking_gui
from reglas_gui import mostrar_reglas_gui

# Acá después importaremos las funciones reales como modoTiempo.modoContraReloj(), etc.
# Por ahora simulamos cada opción con un mensaje


def jugar_1vs1():
    iniciar_modo_1vs1(ventana)
def jugar_tiempo():
    iniciar_modo_tiempo(ventana)
def ver_ranking():
    ver_ranking_gui()
def ver_reglas():
    mostrar_reglas_gui()
def salir():
    ventana.destroy()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("¡Pensá Rápido!")
ventana.geometry("900x600")
ventana.configure(bg="#f5f5f5")

# Título
titulo = tk.Label(
    ventana, 
    text="🎉  ¡PENSÁ RÁPIDO! 🎉", 
    font=("Helvetica", 20, "bold"), 
    fg="#2c3e50", 
    bg="#f5f5f5"
)
titulo.pack(pady=20)

subtitulo = tk.Label(
    ventana, 
    text="📋 Menú Principal", 
    font=("Helvetica", 16), 
    fg="#34495e", 
    bg="#f5f5f5"
)
subtitulo.pack(pady=10)

# Botones del menú
boton_1vs1 = tk.Button(ventana, text="Jugar Modo 1 vs 1", font=("Helvetica", 14), width=30, command=jugar_1vs1)
boton_1vs1.pack(pady=5)

boton_tiempo = tk.Button(ventana, text="Jugar Modo por Tiempo", font=("Helvetica", 14), width=30, command=jugar_tiempo)
boton_tiempo.pack(pady=5)

boton_ranking = tk.Button(ventana, text="Ver Ranking", font=("Helvetica", 14), width=30, command=ver_ranking)
boton_ranking.pack(pady=5)

boton_reglas = tk.Button(ventana, text="Ver Reglas del Juego", font=("Helvetica", 14), width=30, command=ver_reglas)
boton_reglas.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", font=("Helvetica", 14), width=30, command=salir, bg="#e74c3c", fg="white")
boton_salir.pack(pady=20)

# Ejecutar app
ventana.mainloop()
