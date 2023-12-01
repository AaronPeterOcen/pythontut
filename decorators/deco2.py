# why we need decos
# performance decorator example
from time import time


def performance(fn):
    # adding flexibility
    def wrapper(*a, **kw):
        # adding time functionality
        t1 = time()
        result = fn(*a, **kw)
        t2 = time()
        print(f"it took {t2 - t1} s")
        return result

    return wrapper


# import pdb


@performance
def longt():
    # pdb.set_trace()
    for a in range(10**6):
        a * 5


longt()
