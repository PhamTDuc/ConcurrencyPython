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


def producer(queue, prod_ev):
    while not prod_ev.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        queue.put(message, block=True, timeout=None)


def consumer(queue, cons_ev):
    while not cons_ev.is_set():
        message = queue.get()
        logging.info("Consumer storing message: %s (size=%d)", message, queue.qsize())
        queue.task_done()


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    pipeline = Queue(maxsize=5)
    prod_ev = threading.Event()
    cons_ev = threading.Event()

    producer = threading.Thread(target=producer, args=(pipeline, prod_ev))
    consumer1 = threading.Thread(target=consumer, args=(pipeline, cons_ev))
    producer.start()
    consumer1.start()
    time.sleep(0.6)
    prod_ev.set()
    producer.join()
    pipeline.join()
    cons_ev.set()
    consumer1.join()
