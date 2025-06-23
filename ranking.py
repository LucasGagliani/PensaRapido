import os
from datetime import datetime

ARCHIVO_RANKING = 'puntuaciones.csv'

def guardarResultado(nombre, puntaje, tiempo):
    """
    Guarda un nuevo resultado en el archivo de ranking y actualiza la tabla con orden y posiciones.

    Si el archivo no existe, lo crea con los encabezados correspondientes. Luego:
    - Lee los resultados existentes.
    - Agrega el nuevo resultado con fecha y hora actual.
    - Ordena los resultados por mayor puntaje y menor tiempo.
    - Reescribe el archivo con las posiciones actualizadas.

    Parámetros:
    nombre (str): Nombre del jugador.
    puntaje (int): Puntaje obtenido en la partida.
    tiempo (float): Tiempo en segundos que duró la partida.

    Requiere:
    - La constante global ARCHIVO_RANKING que define el nombre del archivo CSV.

    No retorna ningún valor. Guarda la información directamente en el archivo.
    """
    
    if not os.path.exists(ARCHIVO_RANKING):
        with open(ARCHIVO_RANKING, 'w', encoding='utf-8') as f:
            f.write("Posición,Nombre,Puntaje,Tiempo,Fecha,Hora\n")

    # Leer resultados actuales
    resultados = []
    with open(ARCHIVO_RANKING, 'r', encoding='utf-8') as f:
        next(f)
        for linea in f:
            partes = linea.strip().split(',')
            if len(partes) == 6:
                pos, nom, pts, tpo, fecha, hora = partes
                resultados.append({
                    'nombre': nom,
                    'puntaje': int(pts),
                    'tiempo': float(tpo.replace('s','')),
                    'fecha': fecha,
                    'hora': hora
                })

    # Agregar nuevo resultado (fecha y hora actual)
    ahora = datetime.now()
    fecha_str = ahora.strftime("%d/%m/%Y")
    hora_str = ahora.strftime("%H:%M:%S")
    resultados.append({
        'nombre': nombre,
        'puntaje': puntaje,
        'tiempo': tiempo,
        'fecha': fecha_str,
        'hora': hora_str
    })

    # Ordenar: primero puntaje desc, luego tiempo asc
    resultados.sort(key=lambda x: (-x['puntaje'], x['tiempo']))

    # Reescribir archivo con posiciones actualizadas
    with open(ARCHIVO_RANKING, 'w', encoding='utf-8') as f:
        f.write("Posición,Nombre,Puntaje,Tiempo,Fecha,Hora\n")
        for i, res in enumerate(resultados, start=1):
            f.write(f"{i},{res['nombre']},{res['puntaje']},{res['tiempo']}s,{res['fecha']},{res['hora']}\n")

def mostrarRanking():
    """
    Muestra en consola el ranking de resultados del modo 'Contra Reloj'.

    Lee el archivo definido en `ARCHIVO_RANKING` y presenta una tabla con:
    posición, nombre del jugador, puntaje, tiempo, fecha y hora de cada resultado.

    Si el archivo no existe o no contiene resultados, muestra un mensaje informativo.

    No recibe parámetros ni retorna valores; toda la salida es por consola.
    """
    if not os.path.exists(ARCHIVO_RANKING):
        print("🚫 No hay resultados guardados aún.")
        return

    with open(ARCHIVO_RANKING, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    if len(lineas) <= 1:
        print("🚫 No hay resultados para mostrar.")
        return

    print("\n📊 RANKING MODO CONTRA RELOJ\n")
    print(f"{'Pos':<4} {'Nombre':<12} {'Puntaje':<7} {'Tiempo':<8} {'Fecha':<11} {'Hora':<8}")
    print("-" * 55)

    for linea in lineas[1:]:
        partes = linea.strip().split(',')
        if len(partes) < 6:
            continue
        posicion, nombre, puntaje, tiempo, fecha, hora = partes
        print(f"{posicion:<4} {nombre:<12} {puntaje:<7} {tiempo:<8} {fecha:<11} {hora:<8}")
