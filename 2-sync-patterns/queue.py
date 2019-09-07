#!/usr/bin/python3

from threading import Semaphore, Thread
from time import sleep 

leadersQ = Semaphore(0)
followersQ = Semaphore(0)

def leader():
	while True:
		followersQ.release()
		leadersQ.acquire()
		print("l dancing")
		sleep(2)

def follower():
	while True:
		leadersQ.release()
		followersQ.acquire()
		print("f dancing")	
		sleep(2)

for i in range(1):
	Thread(target=leader, args=[]).start()
	Thread(target=follower, args=[]).start()
