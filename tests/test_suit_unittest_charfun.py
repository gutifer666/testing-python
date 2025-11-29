import unittest
from src.charfun import esPalindromo

class TestSuitUnitTestCharFun(unittest.TestCase):

    def test_parametrizado_palindromos(self):
        # Casos que deben devolver True
        casos_true = [
            "oso",                 # minúsculas
            "Anita lava la tina",  # palíndromo con espacios y mayúsculas
            "osO",                 # mixto mayúsc/minúsc
            "0s0",                 # alfanumérico
            "",                    # cadena vacía
            " os o ",              # con espacios
            "'!o?s,o.;:?",         # con puntuación
            "@o#s&o$\\",          # con símbolos especiales
            "+-0*s%=0&&||",        # con símbolos matemáticos
            "osó",                 # unicode con tilde
        ]
        for s in casos_true:
            with self.subTest(caso=s):
                self.assertTrue(esPalindromo(s))

    def test_parametrizado_no_palindromos(self):
        # Casos que deben devolver False
        casos_false = [
            "osa",
            "Anita lava las tina",  # casi palíndromo,
            "!?oSa';:",             # no palíndromo con puntuación
            "osá"                   # no palindromo con tilde
        ]
        for s in casos_false:
            with self.subTest(caso=s):
                self.assertFalse(esPalindromo(s))
    
    def test_si_pasamos_un_entero_como_argumento_se_lanza_una_excepcion(self):
        cadena = 1221
        with self.assertRaises(TypeError):
            esPalindromo(cadena)
