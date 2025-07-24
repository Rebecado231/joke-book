"""Joke Book

Completa las secciones marcadas con TODO para que el juego funcione.
Ejecuta 'python joke_book.py' para probar tu implementación.
"""

from typing import TypedDict
import requests


# Utiliza esta constante allí donde debas leer o guardar los chistes.
JOKES_FILENAME = (
    ""  # TODO: Añade el nombre del archivo JSON donde se guardarán los chistes
)

# Utiliza esta constante para la URL base de la API de chistes.
BASE_URL = ""  # TODO: Añade la URL base de la API de chistes


class Joke(TypedDict):
    """Representa un chiste con su setup y punchline."""

    # TODO: Añade los campos necesarios para representar un chiste.


def format_joke(joke: Joke) -> str:
    """Formatea un chiste con su setup y punchline."""

    raise NotImplementedError()  # TODO: Implementa esta función


def get_random_joke() -> Joke:
    """Obtiene un chiste aleatorio de la API."""

    raise NotImplementedError()  # TODO: Implementa esta función


def save_joke(joke: Joke) -> None:
    """Guarda un chiste en un archivo JSON."""
    raise NotImplementedError()  # TODO: Implementa esta función


def load_jokes() -> list[Joke]:
    """Carga los chistes guardados desde un archivo JSON."""

    raise NotImplementedError()  # TODO: Implementa esta función


def main() -> None:
    """Función principal que ejecuta la utilidad de chistes."""

    # TODO: Implementa la lógica principal de la utilidad.
    # Utiliza un loop infinito para preguntar al usuario si quiere
    # obtener un chiste o leer los chistes guardados.
    # Si elige obtener un chiste, llama a get_random_joke() y muestra
    # el chiste formateado haciendo uso de format_joke().
    # Pregunta si quiere guardarlo y, si es así, llama a save_joke().
    # Si elige leer los chistes guardados, llama a load_jokes() y muestra
    # todos los chistes formateados con format_joke().


if __name__ == "__main__":
    main()
