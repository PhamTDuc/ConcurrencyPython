import logging
import time
import concurrent.futures
import threading

class FakeDataBase(object):
  def __init__(self):
    self.data = 0
    self._lock = threading.Lock()
  
  def update(self, name):
    logging.info("Threads %s: starting update", name)
    with self._lock:
      local_copy = self.data
      local_copy += 1
      time.sleep(0.1)
      self.data = local_copy
    logging.info("Thread %s: finishing update", name)

    
if __name__=="__main__":
  format = "%(asctime)s: %(message)s"
  logging.basicConfig(format=format, level=logging.INFO,                     datefmt="%H:%M:%S")
  database = FakeDataBase()

  logging.info("Testing update. Starting value is %d.", database.data)

  with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    for index in range(2):
      executor.submit(database.update, index)

  logging.info("Testing update. Ending value is %d", database.data)
