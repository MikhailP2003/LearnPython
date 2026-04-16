from functools import wraps


def retry(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for _ in range(count):
                try:
                    return func(*args, **kwargs)
                except ValueError as e:
                    last_exception = e
                    continue
                except OSError as e:
                    print(f"{func.__name__} raise OsError exception.")
                    last_exception = e
                    continue

            raise last_exception

        return wrapper

    return decorator