# test_juego.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from juego1vs1 import validar_nombre, mostrarOpciones

import pytest
from juego1vs1 import validar_nombre, mostrarOpciones

def test_validar_nombre_valido():
    assert validar_nombre("Lucas") is True

def test_validar_nombre_invalido_corto():
    assert validar_nombre("Lu") is False

def test_validar_nombre_con_numeros():
    assert validar_nombre("Lucas123") is False

def test_mostrar_opciones(monkeypatch):
    opciones = ['opcion1', 'opcion2', 'opcion3']
    monkeypatch.setattr('builtins.input', lambda _: "2")  # simula que se elige la segunda opción
    resultado = mostrarOpciones(opciones)
    assert resultado == 1
