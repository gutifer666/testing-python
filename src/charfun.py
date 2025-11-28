"""
charfun.py
Programa que determina si una cadena proporcionada por el
usuario es palíndroma. Para ello se preguntará por teclado al
usuario tantas veces como quiera hasta que escriba la palabra
salir.
Ultima Modificación. 28/11/2025
Autor. Francisco Javier Gutiérrez Pérez
Dependencias. Unicodedata
"""
import unicodedata

def esPalindromo(cadena):
    """
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas y tildes.
    """
    # Normalizar: Descompone caracteres (ej: 'ó' se convierte en 'o' + '´')
    cadena_nfd = unicodedata.normalize('NFD', cadena)
    
    # Filtrar: Nos quedamos solo con lo que NO sea una marca de acento ('Mn')
    # y que sea alfanumérico
    cadena_limpia = ''.join(
        c.lower() 
        for c in cadena_nfd 
        if unicodedata.category(c) != 'Mn' and c.isalnum()
    )

    # # Comparar la cadena limpia con su reverso
    return cadena_limpia == cadena_limpia[::-1]

def ejecutar_app(input_fn=input, output_fn=print):
    """
    Bucle interactivo hasta que el usuario escriba 'salir'.
    Creamos `input_fn` y `output_fn` para facilitar el testing.
    """
    while True:
        frase = input_fn("Introduce una frase (o escribe 'salir' para terminar): ")
        if frase.lower() == "salir":
            output_fn("Programa finalizado.")
            break
        if esPalindromo(frase):
            output_fn("La frase es palíndroma.")
        else:
            output_fn("La frase no es palíndroma.")


if __name__ == "__main__":
    ejecutar_app()