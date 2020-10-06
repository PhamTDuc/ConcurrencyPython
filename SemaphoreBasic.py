import threading

import time

 

parkRequests    = 0
removeRequests  = 0
 
parked          = 0
removed         = 0

 

parkedLock      = threading.Lock()
removedLock     = threading.Lock()

availbleParkings = threading.Semaphore(10)

 

def ParkCar():
  availbleParkings.acquire()
  with parkedLock:
    global parked
    parked = parked+1
  print("Parked: %d"%(parked))      

   

def RemoveCar():
  availbleParkings.release()
  with removedLock:
    global removed
    removed = removed+1
  print("Removed: %d"%(removed))       

 

# Thread that simulates the entry of cars into the parking lot
def parkingEntry():
  # Creates multiple threads inside to simulate cars that are parked
  while(True):
    time.sleep(1)
    incomingCar = threading.Thread(target=ParkCar)
    incomingCar.start()  

 

# Thread that simulates the exit of cars from the parking lot
def parkingExit():
    # Creates multiple threads inside to simulate cars taken out from the parking lot
    while(True):
      time.sleep(3)
      outgoingCar = threading.Thread(target=RemoveCar)
      outgoingCar.start()

 

# Start the parking eco-system
parkingEntryThread = threading.Thread(target=parkingEntry)
parkingExitThread  = threading.Thread(target=parkingExit)

parkingEntryThread.start()
parkingExitThread.start()
