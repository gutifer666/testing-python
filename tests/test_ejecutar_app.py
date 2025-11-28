import unittest
from src.charfun import ejecutar_app

class TestEjecutarApp(unittest.TestCase):
    def test_bucle_hasta_salir(self):
        entradas = iter(["oso", "osa", "salir"])  # iterador para entrada simulada
        salidas = []

        def fake_input(cadena):
            return next(entradas)

        def fake_output(mensaje_salida):
            salidas.append(mensaje_salida)

        ejecutar_app(input_fn=fake_input, output_fn=fake_output)

        # Comprobaciones
        self.assertEqual(salidas[0], "La frase es palíndroma.")
        self.assertEqual(salidas[1], "La frase no es palíndroma.")
        self.assertEqual(salidas[-1], "Programa finalizado.")
