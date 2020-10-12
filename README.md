## Concurrency Python

### Which type of concurrency to choose from
* **threading:** The OS decides when to switch tasks external  to Python                  (Processors: 1)
* **asyncio:** The tasks decides when to give up control                                  (Processor: 1)
* **Multiprocessing:** The processes all run at the same time on different processors     (Processor: Many)

	**CPU Bound** => Multi Processing  
	**I/O Bound, Fast I/O, Limited number of Connections** => Multi Threading  
	**I/O Bound, Slow I/O, Many connections** => Asyncio  

### Context and Start Method
Depending on the platform, there are 3 wasy to start a process:  
* **Spawn** The parent process starts a fresh python interpreter process. The child process will only inherit those resources necessary to run the process objects (Available on Unix and Windows. The default on Windows and macOS)  
* **Fork** The child is effectively idnetical to the parent process. Note that forking a multithreaded process is problematic (Available on Unix only, default on Unix)  
* **Forkserver** A server process is started. From then on, whenever a new process is needed, the parent process connects to the server and requests that it fork a new process. The fork server process is single threaded so it is safe for it to use os.fork(). No unnecessary resources are inherited  
```python
import multiprocessing as mp
def foo(queue):
	queue.put("Hello")

if __name__=="__main__":
	context = mp.get_context("spawn")

	# A manager object returned by Manager() controls a server process which holds Python objects and allows other processes to manipulate them using proxies.
	manager = mp.Manager()
	queue = manager.Queue() 
	proc = context.Process(target = foo, args=(queue,)) 
	proc.start()
	print(queue.get())
	proc.join()
```  

### Get current process from a target 
```python
def foo():
	process = multiprocessing.current_process()
	print(f"Process id: {process.pid}")
```

### Using a pool of workers
```python 
import time
import os

def f(x):
    return x*x

if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        print(pool.map(f, range(10)))

        # print same numbers in arbitrary order
        for i in pool.imap_unordered(f, range(10)):
            print(i)

        # evaluate "f(20)" asynchronously
        res = pool.apply_async(f, (20,))      # runs in *only* one process
        print(res.get(timeout=1))             # prints "400"

        # evaluate "os.getpid()" asynchronously
        res = pool.apply_async(os.getpid, ()) # runs in *only* one process
        print(res.get(timeout=1))             # prints the PID of that process

        # launching multiple evaluations asynchronously *may* use more processes
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        # make a single worker sleep for 10 secs
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")

        print("For the moment, the pool remains available for more work")

    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")
```
#### Methods using in Pool 
* **Iterator** (imap, imap_unordered): Return a iterator. when next() is called, it blocks until the result ready.
* **Async** (apply_async, map_async, starmap_async): Return a AsyncResult object with get() and wait() functions 

