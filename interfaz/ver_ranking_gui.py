import tkinter as tk
from tkinter import ttk
import os
import csv

ARCHIVO_RANKING = 'puntuaciones.csv'

def ver_ranking_gui():
    if not os.path.exists(ARCHIVO_RANKING):
        tk.messagebox.showinfo("Ranking", "🚫 No hay resultados guardados aún.")
        return

    with open(ARCHIVO_RANKING, 'r', encoding='utf-8') as f:
        lineas = list(csv.reader(f))
        if len(lineas) <= 1:
            tk.messagebox.showinfo("Ranking", "🚫 No hay resultados para mostrar.")
            return
        encabezados = lineas[0]
        datos = lineas[1:]

    ventana = tk.Toplevel()
    ventana.title("📊 Ranking Modo Contra Reloj")
    ventana.geometry("900x600")
    ventana.configure(bg="white")

    ttk.Label(ventana, text="📊 Ranking Modo Contra Reloj", font=("Helvetica", 16)).pack(pady=10)

    estilo = ttk.Style()
    estilo.configure("Treeview", font=("Helvetica", 10), rowheight=25)
    estilo.configure("Treeview.Heading", font=("Helvetica", 11, "bold"))

    tree = ttk.Treeview(ventana, columns=encabezados[1:], show="headings", height=15)
    for encabezado in encabezados:
        if encabezado != "Posición":
            tree.heading(encabezado, text=encabezado)
            tree.column(encabezado, width=100, anchor='center')

    for fila in datos:
        tree.insert("", "end", values=fila[1:])  # Ignora la columna "Posición"

    tree.pack(expand=True, fill="both", padx=10, pady=10)

    tk.Button(ventana, text="Cerrar" ,font=("Helvetica", 14), width=30, command=ventana.destroy).pack(pady=10)
