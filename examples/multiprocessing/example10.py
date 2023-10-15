#!/usr/bin/env python3

import logging
import multiprocessing
import time

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s.%(msecs)03d [%(levelname)s] (%(process)d) %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

l = multiprocessing.Lock()
def worker(n):
  logging.debug("lock.acquire()")
  l.acquire()
  logging.debug(" lock acquired !")
  logging.debug("  lock.acquire() again ?")
  l.acquire()
  logging.debug("   lock acquired !")
  logging.debug("    lock.release()")
  l.release()
  logging.debug("     lock released !")

logging.debug("start - this program should result in a deadlock")
for i in range(3):
  multiprocessing.Process(name = 'THREAD-%01d' % (i), target = worker, args = (i,)).start()
