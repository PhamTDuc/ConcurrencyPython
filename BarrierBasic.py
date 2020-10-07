import threading
import time


def start_server():
  print("Staring the Server...")
  time.sleep(2)


def server(barrier):
  start_server()
  print("Server is Ready!!")
  if(True):
    barrier.abort()
  barrier.wait()

def client(barrier):
  print("Waiting for Server getting ready...")
  barrier.wait()
  print("Sending request to Server...")


if __name__=="__main__":
  barrier = threading.Barrier(2, timeout=3)
  s = threading.Thread(target=server, args=(barrier,))
  s.start()
  c = threading.Thread(target=client, args=(barrier,))
  c.start()

  s.join()
  c.join()
  print("Done !!!")