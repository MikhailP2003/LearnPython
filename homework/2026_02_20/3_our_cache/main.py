def cache(func):
    saved = {}

    def wrapper(*args):
        if args in saved:
            return saved[args]

        result = func(*args)
        saved[args] = result
        return result

    return wrapper


@cache
def my_sum(a, b):
    return a + b

print(my_sum(2, 3)) 
print(my_sum(2, 3))  
print(my_sum(4, 1))