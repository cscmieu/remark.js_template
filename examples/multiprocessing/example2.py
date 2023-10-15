#!/usr/bin/env python3

import multiprocessing
import time

def worker():
  print('new worker')
  time.sleep(0.5)
  print('end of worker')

t0 = multiprocessing.Process(target = worker)
t1 = multiprocessing.Process()
t0.daemon = t1.daemon = True
t1.run = worker

print('before')
t0.start()
time.sleep(0.1)
t1.start()
print('after')

