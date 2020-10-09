# PAY ATTENTION: 
# Queue.get() only remove and return the last element from Queue
# Should use Queue.put() only once in a process, otherwises it will cause dead lock

import multiprocessing as mp
import time


def foo(queue):
    queue.put(["Hello", "World"])


def bar(queue):
    queue.put(["The", "Duc"])


if __name__ == "__main__":
    DEFAULT_START_METHOD = "spawn"
    context = mp.get_context(DEFAULT_START_METHOD)
    queue = context.Queue(3)
    proc = context.Process(target=foo, args=(queue,))
    proc2 = context.Process(target=bar, args=(queue,))
    proc.start()
    proc2.start()
    # print(queue.get())
    proc.join()
    proc2.join()
    print(queue.get())
