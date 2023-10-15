#!/usr/bin/env python3

import logging
import threading
import time
import queue

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s.%(msecs)03d [%(levelname)s] (%(threadName)s) %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

q = queue.Queue()
def worker(n):
  while True:
    logging.debug("wait for item")
    item = q.get()
    logging.debug("received item %d" % (item))
    time.sleep(0.2) # do something
    q.task_done()
    logging.debug("task done")

logging.debug("start")
for i in range(3):
  t = threading.Thread(name = 'THREAD-%01d' % (i), target = worker, args = (i,))
  t.daemon = True
  t.start()

time.sleep(1.0)
for i in range(5):
  logging.debug("append item %d to queue" % (i))
  q.put(i)

time.sleep(2.0)

