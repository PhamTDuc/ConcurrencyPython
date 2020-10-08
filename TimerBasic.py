import threading
import time


def function():
  print("Hello the world")

if __name__=="__main__":
  start = time.perf_counter()
  t = threading.Timer(18.0, function)
  t.start()
  t.join()
  print(f"Time Elapsed in {time.perf_counter() - start:f}")
