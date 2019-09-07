#!/usr/bin/python3

from threading import Thread, Semaphore
from time import sleep 

#Barrier pattern 
# a1 or b1 or c1 must occur before c2 or a2 or b2 

sem = Semaphore(0)
sem2 = Semaphore(1)
mutex = Semaphore(1)
count = 0
n = 10 

def a(id):
	global count 
	while True:
		print("------%d" % id) #Rendezvous 
		with mutex:
			count += 1
			if count == 10: 		#All threads have arrived
				sem2.acquire()	#Lock the 2nd turnstile 
				sem.release()	#Unlock the 1st turnstile 
		#First turnstile
		sem.acquire()		
		sem.release()
		print("---%d" % id)	#Critical point 		
		with mutex:		
			count -= 1 
			if count == 0:		
				sem.acquire() 	#Lock the 1st turnstile
				sem2.release() 	#Unlock the 2nd turnstile 
		#Second turnstile
		sem2.acquire()		
		sem2.release()
		sleep(0.1)		


for i in range(n):
	Thread(target=a, args=[i]).start()
