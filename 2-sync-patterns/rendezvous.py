#!/usr/bin/python3

# Rendezvous pattern
# a1 or b1 must occur before b2 or a2 

from threading import Thread, Semaphore
from time import sleep

sem1 = Semaphore(0)
sem2 = Semaphore(0)

def a_activities():
	while True:
		print("a1")
		sem1.release()
		sem2.acquire()
		print("a2")
		sleep(5)

def b_activities():
	while True:
		print("b1")
		sem2.release()
		sem1.acquire()
		print("b2")
		sleep(5)

Thread(target=a_activities, args=[]).start()
Thread(target=b_activities, args=[]).start()
	
