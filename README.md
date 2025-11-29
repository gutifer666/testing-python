# 🛡️ Puesta en Producción Segura: Testing en Python

![Python](https://img.shields.io/badge/python-3.x-blue?logo=python)
![Testing](https://img.shields.io/badge/testing-unittest-green?logo=pytest)
![Status](https://img.shields.io/badge/status-stable-success)
![Author](https://img.shields.io/badge/author-Francisco_Javier_Gutiérrez_Pérez-orange)

> Implementación robusta de un detector de palíndromos aplicando principios de **TDD**, **Normalización Unicode**, **Inyección de Dependencias** y **Diseño por Contrato**.

---

## 📋 Descripción del Proyecto

Este repositorio contiene la evolución de un programa en Python (`charfun.py`) diseñado para verificar si una cadena de texto es palíndroma.El objetivo principal de la práctica no es solo la funcionalidad base, sino dotar al software de una estructura segura mediante una suite de pruebas exhaustiva.

El programa interactúa con el usuario solicitando frases hasta que se introduce el comando `salir`. La lógica de validación es capaz de identificar palíndromos ignorando:
Espacios y puntuación.
Diferencias entre mayúsculas y minúsculas.
Caracteres Unicode (tildes, diéresis, etc.)**.

---

## 🚀 Características Técnicas

| Componente | Implementación                                                                                 |
| :--- |:-----------------------------------------------------------------------------------------------|
| **Normalización** | Uso de `unicodedata` (NFD) para descomponer caracteres y filtrar marcas diacríticas (`Mn`).    |
| **Testing** | Suite realizada con `unittest`, cubriendo casos de éxito y fallo.                              |
| **Parametrización** | Uso de sub-tests para validar múltiples entradas en una sola función de prueba.                |
| **Mocking** | Inyección de dependencias (`input_fn`, `output_fn`) para simular la interacción del usuario.   |
| **Robustez** | Precondiciones para asegurar que el argumento de entrada es un `string` (Diseño por Contrato). |

---

## 🛠️ Instalación y Ejecución

### Requisitos Previa
Se requiere tener instalado **Python 3** y la librería estándar `unittest`.

### Ejecución del Programa
Para iniciar el bucle interactivo del programa principal:

```bash
python src/charfun.py
```