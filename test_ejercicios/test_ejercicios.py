from ejercicios.ejercicio1 import hola

def test_hola(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda nombre: "natalia") 
    assert hola() == "hola natalia" # Lanza la comprobación
 
    # configuramos el test
    # hacemos lo mínimo para que el test funcione
    