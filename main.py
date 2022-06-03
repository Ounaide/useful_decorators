from time import time, sleep
from functools import wraps

def repeat(n=1):
    """modèle decorator avec argument"""
    def decorator(f):
        @wraps(f)
        def wrapper(*args,**kw):
            for _i in range(n):
                res=f(*args,**kw)
            return res
        return wrapper
    return decorator
            

def stopwatch(f):
    """modèle decorator sans arguments"""
    @wraps(f)
    def wrapper(*args,**kw):
        start = time()
        f(*args,**kw)
        end = time()
        print(f"Fonction '{f.__name__}()' terminée en {float(end-start)}s")
    return wrapper

#----------------------
#Exemple:
@stopwatch
@repeat(5)
def hello():
    sleep(1)
    print("Hello world")
    
if __name__ == "__main__":
    try:
        hello()
    except Exception as e:
        print(e)
        
