#!/usr/bin/python3

from threading import Thread, Semaphore
from time import sleep 

sem = Semaphore(0)

def readLine(id):
	while True:
		print("\nreading")
		sem.release()
		sleep(0.1)

def writeLine(id):
	while True:
		sem.acquire()
		print("writing")
		sleep(0.1)

Thread(target=readLine, args=[1]).start()
Thread(target=writeLine, args=[2]).start()
