import threading
import time
from concurrent.futures import ThreadPoolExecutor

def ParkCar(semaphore, mutex, idx):
  with semaphore:
    with mutex:
      global in_parks 
      in_parks += 1
    print(f"Parking car {idx} done (in total = {in_parks})")
    time.sleep(0.2)

def RemoveCar(semaphore, mutex, idx):
  with semaphore:
    with mutex:
      global in_parks 
      in_parks -= 1
    print(f"Remove car {idx} from parking (in total = {in_parks})")


if __name__=="__main__":
  in_parks = 0
  cars_idx = range(100)
  semaphore = threading.Semaphore(10)
  mutex = threading.Lock()
  threads=[]
  
  start = time.perf_counter()
  for car in cars_idx:
    threads.append(threading.Thread(target=ParkCar, args=(semaphore, mutex, car)))
    threads[-1].start()
  
  for th in threads:
    th.join()
  print(f"Total car parks: {in_parks}")
  print(f"Time Elapsed: {time.perf_counter()-start:f}")



