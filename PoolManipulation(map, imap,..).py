# "i" in imap, imap_unordered is abbreviation for Iterator
# For imap, imap_unodered, time to generate iterator depends on how func implements quickly or not 

import os
import multiprocessing as mp
from time import perf_counter, sleep

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    sleep(2)
    print("Not waiting anymore!!")
    raise ValueError
    return title


def heavy_calculate(value):
    sleep(1.25)
    return value**2

# If error_callback is specified then it should be a callable which accepts a single argument. If the target function fails, then the error_callback is called with the exception instance.
def error_callback(e): 
    print(f"Exception from Async: ")

def success_callback(value):
  print(f"Success in creation of {value}")
  
if __name__=="__main__":
    start = perf_counter()
    context = mp.get_context("spawn")
    manager = mp.Manager()

    with context.Pool(4) as pool:
        # pool.apply(func=info, args=("Michael",))
        # future = pool.apply_async(func = info, args=("Async",))
        # try:
        #     future.get(1) # Get value when available or raise TimeOutError when timeout seconds pass
        # except mp.TimeoutError:
        #     print("Overtime: FAILED to implement!!") 


        # results = pool.imap(func=heavy_calculate, iterable=range(3,60), chunksize = 8) # Block until the results ready
        # print(results) # Not depends on creation of iterator
        # print(next(results))
        # print(next(results))
        # print(next(results))


        result = pool.apply_async(func=info, args=("Johnny",),callback=success_callback, error_callback=error_callback)
        result.get()
    print(f"Time Elapsed in {perf_counter() - start:f} sec(s).")

