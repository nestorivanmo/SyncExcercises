#!/usr/bin/python3

from threading import Thread, Semaphore
from time import sleep 

sem = Semaphore(0)

def readLine(id):
	global line
	while True:
		print("\nreading")
		sem.release()
		sleep(0.1)

def writeLine(id):
	global line 
	while True:
		sem.acquire()
		print("writing")
		sleep(0.1)

Thread(target=readLine, args=[1]).start()
Thread(target=writeLine, args=[2]).start()
