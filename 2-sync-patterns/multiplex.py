#!/usr/bin/python3

from time import sleep
from random import randint 
from threading import Semaphore, Thread 

limit = Semaphore(5)
alive = []
mutex_remaining = Semaphore(1)

def entering(n):
	global alive
	print("%d waiting" % n)
	limit.acquire()
	mutex_remaining.acquire()
	alive.append(n)
	print("I'm %d, inside we are: %s" % (n,alive))
	mutex_remaining.release()
	sleep(randint(0,5))
	print("%d out!" % n)
	mutex_remaining.acquire()
	alive.remove(n)
	mutex_remaining.release()
	limit.release()

for i in range(20):
	Thread(target=entering, args=[i]).start()

