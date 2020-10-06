import concurrent.futures
import urllib.request
import time

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/',
        'https://www.google.com.vn',
        'https://www.blender.org',
        'https://www.daz3d.com/',
        ]

def load(url, timeout):
  with urllib.request.urlopen(url, timeout = timeout) as conn:
    return conn.read()


if __name__=="__main__":
  start = time.perf_counter()
  with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    future_to_url ={executor.submit(load, url, 20): url for url in URLS}

    for future in concurrent.futures.as_completed(future_to_url):
      url = future_to_url[future]
      try:
        data = future.result()
      except Exception as e:
        print(f"%r generated an exception: %s" % (url, e))
      else:
        print('%r page is %d bytes' % (url, len(data)))

  print(f"Main elapsed in {time.perf_counter()-start:f}")


