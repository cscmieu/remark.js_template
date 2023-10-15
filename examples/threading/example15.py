#!/usr/bin/env python3

import logging
import threading
import time

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s.%(msecs)03d [%(levelname)s] (%(threadName)s) %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

c = threading.Condition()
def worker(n):
  logging.debug("wait")
  with c:
    c.wait()
    logging.debug("received !")

logging.debug("start")
for i in range(3):
  threading.Thread(name = 'THREAD-%01d' % (i), target = worker, args = (i,)).start()
logging.debug("set condition")

for i in range(3):
  time.sleep(1.0)
  with c:
    logging.debug("notify one thread")
    c.notify()

