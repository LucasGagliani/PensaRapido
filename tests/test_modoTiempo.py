# test_modoTiempo.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from juego1vs1 import validar_nombre, mostrarOpciones


import pytest
from modoTiempo import hacerPregunta, pedirRespuestaConTiempo, PENALIZACION_TIEMPO
import builtins

def test_pedirRespuestaConTiempo_respuesta_rapida(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    assert pedirRespuestaConTiempo() == "1"

def test_hacerPregunta_correcta(monkeypatch):
    pregunta = {
        "pregunta": "¿Capital de Francia?",
        "opciones": ["Madrid", "París", "Roma", "Berlín"],
        "respuestaCorrecta": "París"
    }

    # Capturamos cómo quedó el orden después de mezclar
    opciones_ordenadas = pregunta["opciones"][:]
    import random
    random.shuffle(opciones_ordenadas)

    index_correcto = opciones_ordenadas.index("París") + 1
    monkeypatch.setattr("builtins.input", lambda _: str(index_correcto))

    # Para forzar el orden que se usó arriba, lo seteamos de nuevo
    monkeypatch.setattr("random.shuffle", lambda x: x.__setitem__(slice(None), opciones_ordenadas))

    correcto, tiempo = hacerPregunta("Lucas", pregunta)
    assert correcto is True


def test_hacerPregunta_incorrecta(monkeypatch):
    pregunta = {
        "pregunta": "¿Capital de Francia?",
        "opciones": ["Madrid", "París", "Roma", "Berlín"],
        "respuestaCorrecta": "París"
    }
    monkeypatch.setattr("builtins.input", lambda _: "1")
    correcto, tiempo = hacerPregunta("Lucas", pregunta)
    assert correcto is False
    assert tiempo >= PENALIZACION_TIEMPO
