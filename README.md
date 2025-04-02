Proyecto ¡Pensá Rápido!

ALGORITMOS Y ESTRUCTURAS DE DATOS I
Grupo N°: 13

Integrantes:
-Gabriel Carlos Vivo
-Lucas Gagliani
-Nicolás Ledesma
-Rodrigo Naconyszny


1. Descripción del Proyecto
El proyecto consiste en el desarrollo de un juego de preguntas y respuestas similar a "Preguntados", donde los jugadores deben responder preguntas de diversas categorías y niveles de dificultad. El juego se ejecuta en consola y utiliza matrices para organizar las preguntas y archivos de texto para gestionar el almacenamiento de preguntas y puntuaciones.

2. Objetivos
- Implementar un juego interactivo en Python basado en preguntas y respuestas.
- Organizar las preguntas en una matriz, categorizadas por tema y nivel de dificultad.
- Utilizar archivos de texto para cargar preguntas y tiempos en ranking.
- Implementar dos modos de juego: Modo por tiempo (contra la máquina) y Modo 1vs1.
- El jugador responderá seleccionando entre 4 opciones ingresando el número de la respuesta.
- Guardar y mostrar un ranking de puntuaciones al final de cada partida de los mejores 20 tiempos.

3. Alcance
El juego incluirá las siguientes funcionalidades:
✅ Carga de preguntas desde un archivo (`preguntas.txt`).
   - Cada pregunta se guardará con su categoría, nivel de dificultad, opciones de respuesta y respuesta correcta.
   - Formato: `Historia,Fácil,¿En qué año fue la Revolución Francesa?,1789, 1776, 1804, 1812, 1789`

✅ Uso de una matriz para organizar las preguntas.
   - Fila = Categoría (Historia, Ciencia, Deporte, etc.).
   - Columna = Dificultad (Fácil, Media, Difícil).

✅ Selección de pregunta según categoría y dificultad.
   - El jugador elige una categoría y un nivel de dificultad.
   - Se extrae una pregunta de la matriz y se muestra en pantalla con 4 opciones numeradas.
   - El jugador responde ingresando el número correspondiente a la opción correcta.

✅ Implementación de modos de juego.
   - Modo por tiempo: El jugador responde preguntas aleatorias dentro de un tiempo límite, compitiendo por tiempo.
   - Modo 1vs1: Dos jugadores se turnan para responder preguntas, ganando puntos por respuestas correctas.

✅ Registro de puntuaciones.
   - Al finalizar el juego, se muestra el puntaje de cada jugador y el ganador o el tiempo (dependiendo del modo de juego).
   - En el modo por tiempo, se muestra el ranking de los mejores 20 tiempos, y cómo se posiciono el jugador en el ranking.
   - En el modo por tiempo también se castiga por cada respuesta errónea con una penalización de +10seg.

✅ Sistema de puntuación.
   - Respuesta correcta (1vs1): +10 puntos (Fácil), +20 puntos (Media), +30 puntos (Difícil).
   - Respuesta incorrecta (1vs1): No suma puntos.
   - Respuesta correcta (Tiempo): Pasa a la siguiente pregunta.
   - Respuesta incorrecta (Tiempo): Se penaliza al jugador con 10 segundos extras.

✅ Ranking de mejores tiempos (`ranking.txt`).
   - Se guardaran todos los tiempos en un archivo formato ".txt".
   - Se muestra el ranking al finalizar el juego con el tiempo del jugador; se muestran los 20 mejores tiempos y tu posición en el ranking.

4. Entregables

40% de avance:
- Implementación de la estructura de archivos (`preguntas.txt`).
- Creación de la matriz de preguntas con categorización y niveles de dificultad.
- Desarrollo de la lógica para seleccionar preguntas aleatoriamente según la categoría y dificultad elegida.
- Implementación inicial del Modo 1vs1.

80% de avance:
- Implementación del sistema de puntuación y registro de respuestas del jugador.
- Funcionalidad de almacenamiento de puntuaciones en `puntuaciones.txt`.
- Ordenamiento y visualización del ranking de jugadores en consola.
- Desarrollo completo del Modo por tiempo.
- Implementación de validaciones en las respuestas ingresadas por el usuario.
- Pruebas de funcionamiento y ajuste de errores.

100% de avance:
- Optimización del código para mejorar eficiencia y legibilidad.
- Implementación de un menú interactivo para una mejor experiencia de usuario.
- Validación de entradas para evitar errores en el juego.
- Documentación completa del código y manual de usuario básico.
- Pruebas finales y entrega del proyecto listo para su ejecución.
- Proyecto terminado con interfaz visual en consola. 
*Si terminamos el proyecto antes de tiempo, vamos a intentar sumarle una interfaz gráfica (El 100% del entregable es por consola).

5. Conclusión
Este proyecto permite desarrollar habilidades en estructuras de datos (matrices), manejo de archivos y lógica de juego en Python. Además, es una aplicación interactiva y divertida que puede extenderse con nuevas funcionalidades o modos en futuras versiones.
