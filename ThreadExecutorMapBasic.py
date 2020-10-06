from concurrent.futures import ThreadPoolExecutor
import time 

def count_chars(sentence):
  nums = len(sentence)
  print(f"Sentence \"{sentence:.20s}\" has {nums} characters")
  # time.sleep(1)
  return nums

def count_words(sentence):
  nums = len(sentence.split())
  print(f"Sentence \"{sentence:.20s}\" has {nums} words")
  # time.sleep(1)

if __name__=="__main__":
  sentences = ["Python Multiprocessing is an important library for achieving parallel programming", "If a func call raises an exception, then that exception will be raised when its value is retrieved from the iterator", "Signal the executor that it should free any resources that it is using when the currently pending futures are done executing"] * 10
  
  start = time.perf_counter()
  with ThreadPoolExecutor(max_workers = 4) as executor:
    results_1 = executor.map(count_chars, sentences)
    results_2 = executor.map(count_words, sentences)

    for result in results_1:
      print(f"Result: {result}")
    
  print(f"Main Done in {time.perf_counter()-start:f}")

