import concurrent.futures
from typing import Callable


def run_threaded(func: Callable, iterator, *args):
    """
    Ejecuta la función `func` en paralelo usando hilos para cada elemento de `lista`,
    pasando los parámetros `args` adicionales a cada llamada.

    Parámetros:
    - func: La función que se ejecutará en cada hilo.
    - iterator: Una lista cuyos elementos se usarán para crear un hilo por cada uno.
    - *args: Parámetros adicionales que se pasarán a la función `func`.

    Retorna:
    - Una lista con los resultados concatenados de cada hilo.
    """
    def wrapper(item):
        return func(
            item, *args
        )  # Llama a la función con el item de la lista y los argumentos adicionales

    # Crear un ThreadPoolExecutor para manejar los hilos
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Ejecutar la función en paralelo, creando un hilo por cada elemento de la lista
        resultados = list(executor.map(wrapper, iterator))

    # Concatenar los resultados y devolverlos
    return "".join(map(str, resultados))