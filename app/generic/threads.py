from concurrent.futures.thread import ThreadPoolExecutor
from concurrent. futures import as_completed
from typing import Callable
import logging

def run_threaded(funcion: Callable, *args, **kwargs):
    '''
    funcion: is the function to be executed\n
    args: contains the arguments to be passed to the function: url1, url2, url3, ...\n
    kwargs: contains the keyword arguments to be passed to the function: cookies=cookies, headers=headers, ...
    '''
    with ThreadPoolExecutor(max_workers=len(args)) as executor:
        futures = {executor.submit(funcion, i, kwargs): i for i in args}
        results = set()
        for future in as_completed(futures):
            try:
                result = future.result()
            except Exception as e:
                print(f"Thread {futures[future]} generated an exception: {e}")
            else:
                results.update(result)

        return results


def _test_f(num: int, dic: dict):
    return f"{num} {dic.items()}"

def _test():
    logging.debug(run_threaded(_test_f, 1, 2, 3, 4, hola="buenos dias", adios="buenas noches"))