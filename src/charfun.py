"""
charfun.py
Programa que determina si una cadena proporcionada por el
usuario es palíndroma. Para ello se preguntará por teclado al
usuario tantas veces como quiera hasta que escriba la palabra
salir.
Ultima Modificación. 21/11/2024
Autor. Gregorio Coronado Morón
Dependencias. Unicodedata
"""
import unicodedata

def esPalindromoOriginal(cadena):
    """
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas y tildes.
    """
    # Convertir la cadena a minúsculas y eliminar caracteres no alfabéticos
    cadena_limpia = ''.join(char.lower() for char in cadena if
    char.isalnum())

    # Comparar la cadena limpia con su reverso
    return cadena_limpia == cadena_limpia[::-1]

def esPalindromo(cadena):
    """
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas y tildes.
    """
    # 1. Normalizar: Descompone caracteres (ej: 'ó' se convierte en 'o' + '´')
    cadena_nfd = unicodedata.normalize('NFD', cadena)
    
    # 2. Filtrar: Nos quedamos solo con lo que NO sea una marca de acento ('Mn')
    # y que sea alfanumérico
    cadena_limpia = ''.join(
        c.lower() 
        for c in cadena_nfd 
        if unicodedata.category(c) != 'Mn' and c.isalnum()
    )

    # 3. Comparar
    return cadena_limpia == cadena_limpia[::-1]

frase = input("Introduce una frase (o escribe 'salir' para terminar): ")

if frase.lower() == "salir":
    print("Programa finalizado.")
else:
    # Comprobar si es palíndromo
    if esPalindromo(frase):
        print("La frase es palíndroma.")
    else:
        print("La frase no es palíndroma.")