import logging
import random
import threading
import time
from queue import Queue


class Pipeline(Queue):
    def __init__(self, *args, **kwargs):
        super(Pipeline, self).__init__(*args, **kwargs)

    def get_message(self, name):
        logging.debug("%s about to get from queue", name)
        value = self.get()
        logging.debug("%s go %d from queue", name, value)

    def set_message(self, name, value):
        logging.debug("%s about to add %d to queue", name, value)
        self.put(value)
        logging.deub("%s add %d to queue", name, value)


def producer(queue, prod_ev, idx):
    while not prod_ev.is_set():
        message = random.randint(1, 101)
        logging.info("Producer %d got message: %s", idx, message)
        queue.put(message, block=True, timeout=None)


def consumer(queue, cons_ev, idx):
    while True:
        message = queue.get()
        logging.info("Consumer %d storing message: %s (size=%d)", idx, message, queue.qsize())
        queue.task_done()
    # logging.info("Consumer %d DONE", idx)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    pipeline = Queue(maxsize=5)
    prod_ev = threading.Event()
    cons_ev = threading.Event()

    prods=[]
    for i in range(3):
      prod = threading.Thread(target=producer, args=(pipeline, prod_ev, i))
      prods.append(prod)

    cons=[]
    for i in range(2):
      th = threading.Thread(target=consumer, args=(pipeline, cons_ev, i), daemon= True)
      cons.append(th)

    start = time.perf_counter()

    for th in prods:
      th.start()

    for th in cons:
      th.start()

    time.sleep(0.6)
    prod_ev.set()
    for th in prods:
      th.join()
    pipeline.join()
    print(f"Time elapsed: {time.perf_counter()-start-0.6:f}")

