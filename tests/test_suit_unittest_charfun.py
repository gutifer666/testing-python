import unittest
from src.charfun import esPalindromo

class TestSuitUnitTestCharFun(unittest.TestCase):
    
    def test_cadena_palindroma_de_una_palabra_en_minusculas_devuelve_true(self):
        
        self.assertTrue(esPalindromo("oso"))

    def test_cadena_no_palindroma_de_una_palabra_en_minusculas_devuelve_false(self):
        
        self.assertFalse(esPalindromo("osa"))

    def test_cadena_vacia_devuelve_true(self):
        
        self.assertTrue(esPalindromo(""))

    def test_cadena_palindroma_con_espacio_devuelve_true(self):
        
        self.assertTrue(esPalindromo("os o"))

    def test_cadena_palindroma_con_puntuacion_devuelve_true(self):
        
        self.assertTrue(esPalindromo("os,o"))

    def test_cadena_palindroma_con_espacio_al_final_devuelve_true(self):
        
        self.assertTrue(esPalindromo("oso "))

    def test_cadena_palindroma_con_tilde_devuelve_true(self):
        
        self.assertTrue(esPalindromo("osó"))


