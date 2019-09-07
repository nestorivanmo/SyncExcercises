#!/usr/bin/python3

from threading import Thread, Semaphore
from time import sleep 

#Barrier pattern 
# a1 or b1 or c1 must occur before c2 or a2 or b2 

sem = Semaphore(0)
mutex = Semaphore(1)
count = 0
n = 3 

def a(id):
	global count 
	while True:
		print("%d - i" % id)
		mutex.acquire()
		count += 1
		mutex.release()
		if count == n:
			sem.release()
		sem.acquire()	
		sem.release()
		print("%d - f" % id)
		sleep(5)		


for i in range(3):
	Thread(target=a, args=[i]).start()
