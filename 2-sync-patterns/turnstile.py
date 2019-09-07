#!/usr/bin/python3

from threading import Thread, Semaphore
from time import sleep 

#Turnstile
#guarantees that a group of threads pass through a point one by one 

turnstile = Semaphore(0)
mutex = Semaphore(1)
n = 4
count = 0

def a(id):
	global count 
	while True:
		print(str(id) + " entering")
		with mutex:
			count += 1
		if count == n:
			turnstile.release()
		turnstile.acquire()
		turnstile.release()
		print(str(id) + " critical point")
		sleep(5)	

for i in range(n):
	Thread(target=a, args=[i]).start()
