# Joke Book 😂

En este proyecto de Python, crearás una pequeña utilidad para obtener chistes aleatorios a través de una API pública. Además, la utilidad permitirá guardar aquellos chistes que te han hecho más gracia, para que puedas volver a leerlos en otro momento. Aprenderás a realizar peticiones HTTP con la librería `requests`, y profundizaras en el manejo de JSONs y archivos.

## 1. Requisitos

- `python ≥ 3.12`
- `git`

## 2. Arranque rápido

```bash
# Clona tu propio fork
git clone <tu‑fork‑url> joke-book
cd joke-book

# Crea y activa un entorno virtual
python -m venv .venv
source .venv/bin/activate      # Windows: .\.venv\Scripts\activate

# Instala dependencias de desarrollo
pip install -r requirements-dev.txt

# Formatea y analiza (solo deberían aparecer TODOs sin implementar)
black .
pylint joke_book.py
mypy joke_book.py

# Ejecuta la utilidad (fallará hasta que completes el código)
python joke_book.py
```

## 3. Tareas a completar

1. Implementa las funciones marcadas con **`TODO`** en `joke_book.py`.
2. La lógica básica es:
   - Al iniciar, la utilidad debe solicitar al usuario si quiere obtener un chiste aleatorio o leer los chistes guardados.
   - Si elige obtener un chiste, se realiza una petición a la API pública de chistes (https://official-joke-api.appspot.com/) y se muestra el chiste al usuario.
   - Después de mostrar el chiste, se pregunta al usuario si quiere guardarlo. Si responde afirmativamente, se guardará en un JSON que actue como registro de chistes.
   - Si elige leer los chistes guardados, se cargan desde el JSON y se muestran al usuario.
3. Ejecuta `black`, `pylint` y `mypy --strict` hasta que no queden advertencias.
4. Es conveniente que te familiarices primero con el formato de las respuestas de la API. De la misma manera, piensa en cómo estructurar el JSON para guardar los chistes. Puedes usar un formato simple como una lista de diccionarios, donde cada diccionario representa un chiste con sus campos correspondientes.
