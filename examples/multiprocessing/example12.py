#!/usr/bin/env python3

import logging
import multiprocessing
import time

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s.%(msecs)03d [%(levelname)s] (%(process)d) %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

s = multiprocessing.Event()
def worker(n):
  logging.debug("waiting for signal")
  s.wait()
  logging.debug("signal received")

logging.debug("start")
for i in range(3):
  multiprocessing.Process(name = 'THREAD-%01d' % (i), target = worker, args = (i,)).start()
logging.debug("send signal")
s.set()
