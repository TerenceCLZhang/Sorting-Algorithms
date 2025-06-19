import time
from functools import wraps


def finished_animation(arr):
    for i in range(len(arr)):
        yield arr, [], list(range(i + 1))


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        for value in func(*args, **kwargs):
            yield value
        end = time.time()
        print(f"Time: {(end - start)} seconds")
    return wrapper