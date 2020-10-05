import logging
import threading
import time 
import concurrent.futures

def thread_function(name):
  logging.info("Thread %s starting", name)
  time.sleep(2)
  logging.info("Thread %s finished", name)


if __name__=="__main__":
  format = "%(asctime)s: %(message)s"
  logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")


  # threads = []
  # for index in range(3):
  #   logging.info("Main: creating and start thread %d", index)
  #   threads.append(threading.Thread(target = thread_function, args=(index,)))
  #   threads[index].start()

  # for index, th in enumerate(threads):
  #   logging.info("Main    : before joining thread %d.", index)
  #   th.join()
  #   logging.info("Main    : thread %d done", index)

  with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(thread_function, range(3))
  
  logging.info("Main: ALL DONE")

