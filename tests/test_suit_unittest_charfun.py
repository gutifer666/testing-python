import unittest
from src.charfun import esPalindromo

class TestSuitUnitTestCharFun(unittest.TestCase):
    
    def test_cadena_palindroma_en_minusculas_devuelve_true(self):
        
        self.assertTrue(esPalindromo("oso"))


    def test_cadena_palindroma_en_minusculas_y_mayusculas_devuelve_true(self):
        
        self.assertTrue(esPalindromo("osO"))

    
    def test_cadena_palindroma_alfanumerica_devuelve_true(self):
        
        self.assertTrue(esPalindromo("0s0"))
    
    
    def test_cadena_no_palindroma_devuelve_false(self):
        
        self.assertFalse(esPalindromo("osa"))



    def test_cadena_vacia_devuelve_true(self):
        
        self.assertTrue(esPalindromo(""))


    def test_cadena_palindroma_con_espacio_devuelve_true(self):
        
        self.assertTrue(esPalindromo(" os o "))


    def test_cadena_palindroma_con_puntuacion_devuelve_true(self):
        
        self.assertTrue(esPalindromo("'!o?s,o.;:?"))

    
    def test_cadena_palindroma_con_simbolos_especiales_devuelve_true(self):
        
        self.assertTrue(esPalindromo("@o#s&o$"))
    
    
    def test_cadena_palindroma_con_simbolos_matematicos_devuelve_true(self):
        
        self.assertTrue(esPalindromo("+-0*s%=0&&||"))    
    
    
    def test_cadena_palindroma_con_unicode_devuelve_true(self):
        
        self.assertTrue(esPalindromo("osó"))


