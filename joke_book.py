"""Joke Book

Completa las secciones marcadas con TODO para que el juego funcione.
Ejecuta 'python joke_book.py' para probar tu implementación.
"""

from typing import TypedDict
import json
import requests

# SYNTAX requests.methodname(params)
# Method	Description
# delete(url, args)	Sends a DELETE request to the specified url
# get(url, params, args)	Sends a GET request to the specified url
# head(url, args)	Sends a HEAD request to the specified url
# patch(url, data, args)	Sends a PATCH request to the specified url
# post(url, data, json, args)	Sends a POST request to the specified url
# put(url, data, args)	Sends a PUT request to the specified url
# request(method, url, args)	Sends a request of the specified method to the specified url

JOKES_FILENAME = "saved_jokes.json"

BASE_URL = "https://official-joke-api.appspot.com/"


class Joke(TypedDict):
    """Representa un chiste con su setup y punchline."""

    type: str
    setup: str
    punchline: str
    id: int


def format_joke(joke: Joke) -> str:
    """Formatea un chiste con su setup y punchline."""
    formated_joke = f"{joke['setup']}\n{joke['punchline']}"
    return formated_joke


def get_random_joke() -> Joke:
    """Obtiene un chiste aleatorio de la API."""
    response = requests.get(BASE_URL + "random_joke", timeout=5)
    new_joke = response.json()
    return new_joke


def save_joke(joke: Joke, user_name:str) -> None:
    """Guarda un chiste en un archivo JSON."""
    with open(JOKES_FILENAME, "r", encoding="utf-8") as file:
        saved_jokes = json.load(file)
    for user_record in saved_jokes:
        if user_record["user"] == user_name:
            my_jokes = user_record["jokes"]
            for single_joke in my_jokes:
                if single_joke["id"] == joke["id"]:
                    print("This joke is already saved")
                    break
            else:
                my_jokes.append(joke)
            break
    else:
        user_record = {"user": user_name, "jokes": [joke]}
        saved_jokes.append(user_record)

    with open(JOKES_FILENAME, "w", encoding="utf-8") as file:
        json.dump(saved_jokes, file, indent="\t")


def load_jokes(user_name:str) -> list[Joke]:
    """Carga los chistes guardados desde un archivo JSON."""
    with open(JOKES_FILENAME, "r", encoding="utf-8") as file:
        file_read = json.load(file)
        for sheet in file_read:
            if sheet["user"] == user_name:
                return sheet["jokes"]

    raise ValueError("User not found")


def main() -> None:
    """Función principal que ejecuta la utilidad de chistes."""
    user_name = str(input("User name: "))
    while True:
        new_joke = get_random_joke()
        ask = str(input("Yo want a new joke or a saved one? new / saved / exit"))
        if ask.lower().strip() == "new":
            print(format_joke(new_joke))
            save = str(input("Yo want to save this new joke? Y/N"))
            if save.upper().strip() == "Y":
                save_joke(new_joke, user_name)
                # por qué si le digo "y" no me lleva a save_joke y me pregunta el nombre?
        elif ask.lower().strip() == "saved":
            json_jokes = load_jokes(user_name)
            for joke in json_jokes:
                print(format_joke(joke))
        elif ask.lower().strip() == "exit":
            break

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
