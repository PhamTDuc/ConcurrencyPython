import math
import time
import concurrent.futures

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__=="__main__":
  start = time.perf_counter()
  with concurrent.futures.ProcessPoolExecutor(max_workers = 3, ) as executor:
    for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
      print("%d is prime: %s" %(number, prime))

  print(f"Main Elapsed {time.perf_counter()-start:f}")
