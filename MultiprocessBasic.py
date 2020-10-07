# https://www.ellicium.com/python-multiprocessing-pool-process/
from multiprocessing import Process, Value
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

def worker1(value):
  with value.get_lock():
    value.value += 2

def worker2(value):
  with value.get_lock():
    value.value +=3

if __name__ == '__main__':
    # info('main line')
    # p = Process(target=f, args=('bob',))
    # p.start()
    # p.join()
    ctypes_int = Value("i", 0)
    print(f"Value before: {ctypes_int.value}")

    proc1 = Process(target = worker1, args=(ctypes_int,))
    proc2 = Process(target = worker2, args=(ctypes_int,))

    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()

    print(f"Value after: {ctypes_int.value}")