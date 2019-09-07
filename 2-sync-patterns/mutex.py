#!/usr/bin/python3

from threading import Thread, Semaphore
from time import sleep 

mutex = Semaphore(1)
count = 0

def a_activity():
	global count 
	while True:
		print("E a: %d" % count)
		mutex.acquire()
		count = count + 1 
		mutex.release()
		print("L a: %d" % count)
		sleep(1)
		
def b_activity(): 
	global count 
	while True: 
		print("E b: %d" % count)
		mutex.acquire()
		count = count + 1
		mutex.release() 
		print("L b: %d" % count)
		sleep(1)

Thread(target=a_activity, args=[]).start()
Thread(target=b_activity, args=[]).start()
