import os
import pickle
from functools import wraps


def cache(filename, key_type='positional'):
    def decorator(func):
        memory_cache = {}

        if os.path.exists(filename):
            try:
                with open(filename, 'rb') as f:
                    file_cache = pickle.load(f)
                    if isinstance(file_cache, dict):
                        memory_cache.update(file_cache.get(func.__name__, {}))
            except Exception:
                pass

        @wraps(func)
        def wrapper(*args, **kwargs):
            if key_type == 'positional':
                key = args
            elif key_type == 'named':
                key = tuple(sorted(kwargs.items()))
            else:
                raise ValueError("key_type должен быть 'positional' или 'named'")

            if key in memory_cache:
                return memory_cache[key]

            result = func(*args, **kwargs)
            memory_cache[key] = result

            all_cache = {}
            if os.path.exists(filename):
                try:
                    with open(filename, 'rb') as f:
                        all_cache = pickle.load(f)
                        if not isinstance(all_cache, dict):
                            all_cache = {}
                except Exception:
                    all_cache = {}

            func_cache = all_cache.get(func.__name__, {})
            func_cache.update(memory_cache)
            all_cache[func.__name__] = func_cache

            with open(filename, 'wb') as f:
                pickle.dump(all_cache, f)

            return result

        return wrapper

    return decorator

@cache('sum_cache.pkl', key_type='named')
def my_sum(a, b):
    print('Функция вычисляется...')
    return a + b


print(my_sum(a=2, b=3))
print(my_sum(a=2, b=3))