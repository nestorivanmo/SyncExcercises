#!/usr/bin/python3

from threading import Thread, Semaphore
from time import sleep
from random import randint 


santa = Semaphore(0)
elves = Semaphore(1)
reindeerReturning = Semaphore(1)
mutex = Semaphore(1)
problems = 0
problematicElves = []
reindeer = 0

def santaClaus():
	global problems, reindeer
	while True:
		santa.acquire()
		print("\nSanta is now ready to work.")
		with mutex:
			if reindeer == 9:
				print("\t\tNow leaving the North Pole to deliver gifts...")
				reindeer = 0
				sleep(randint(2,3))
				print("Now entering the Nort Pole to sleep. Reindeer going on vacations\n")
				sleep(2)
				reindeerReturning.release()
			elif problems == 3:
				print("\t\t\tNow helping elves: %s" % problematicElves)
				problems = 0	
				del problematicElves[0:3]
				sleep(randint(2,3))
				print("Finished helping elves.\n\tRemaining elves to help: %d\n" % len(problematicElves))
				sleep(2)
				elves.release()


def elvesWorking(id):
	global problems
	while True:
		elves.acquire()
		print("Elf #%d working" % id)
		sleep(1)
		if randint(0,500) <= 250:	
			print("\t\t\t this elf has a problem.")
			with mutex:
				problematicElves.append(id)
				problems += 1
				if problems == 3:
					print("Now there are 3 elves with problems")
					sleep(1.5)
					santa.release()
				else:
					elves.release()
		else:
			elves.release()
		sleep(2)
	

def reindeerLeaving(id):
	global reindeer
	while True:
		reindeerReturning.acquire()
		if randint(20,40) <= 30:
			print("\t\t\t\t\t\tReindeer #%d ready!" % id)	
			with mutex:
				reindeer += 1
				if reindeer == 9:
					print("\t\t\t\t\t\t\t\t9 reindeer ready to work!")
					sleep(1.5)
					santa.release()
				else:
					reindeerReturning.release()
		else: 
			reindeerReturning.release()
		sleep(3)


Thread(target=santaClaus, args=[]).start()
for i in range(40):
	Thread(target=elvesWorking, args=[i]).start()
for i in range(9):
	Thread(target=reindeerLeaving, args=[i]).start()
