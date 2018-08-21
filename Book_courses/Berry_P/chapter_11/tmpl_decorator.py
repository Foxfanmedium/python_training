from functools import wraps


def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        #1. Code to execute before calling the decorator function.
        #2. Вызов декорируемой функции и влзврат полученных от нее результатов
        return func
        #3. Код для выполнения ВМЕСТО вызова декорируемой функции.
        """
    return wrapper









