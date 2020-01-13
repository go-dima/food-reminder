"""
General utils for python
"""
import functools

def trycatch(func):
    """
    try/catch block decorator
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as ex:
            print(f"Error at {func.__name__}")
            print(ex)
    return wrapper
