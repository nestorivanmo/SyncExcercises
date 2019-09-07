#!/usr/bin/python3

from threading import Thread, Semaphore
from time import sleep
from random import randint 

#Santa Claus in the North Pole sleeps all year until:
	#1. 3 of Santa Claus' elves have a problem. If another elf has a problem, she/he cannot interrupt Santa Claus until he has finished solving the previous 3 elves' problems.
	#2. Santa Claus' 9 raindeer are on vacation on the Caribe; but when theydecide to return to the North Pole, Santa Claus knows its time to start delivering gifts. 


santa = Semaphore(0) 		#Semaphore for Santa Claus 
elves_limit = Semaphore(3)	#Semaphore for allowing only 3 elves' problems
mutex = Semaphore(1)		#mutex to protect num of elf_problems 
elf_problems = 0 		#variable of num of problems elves have
raindeer = 0			#variable to denote num of raindeer that have returned from vacation

def working(id):
	global elf_problems
	while True:
		elves_limit.acquire()
		print("Elf #%d working..." % id)
		with mutex:
			elf_problems += 1 
			if elf_problems == 3:
				print("--- num of p: %d" % (elf_problems))
				santa.release()	
		sleep(1)

def returning(id):
	global raindeer 
	with mutex:
		raindeer += 1
		if raindeer == 9:
			print("\nAll 9 raindeer have returned from vacation.")
			santa.release()
	
def santa_claus():
	global elf_problems, raindeer
	while True:
		santa.acquire()		#if no one has called you, go to sleep
		print("\nSanta Claus is now waking up...")
		with mutex:
			if raindeer == 9:
				beginJourney()			
			elif elf_problems == 3:
				help_elves()
		sleep(1)

def beginJourney():
	global raindeer
	raindeer = 0
	print("TIME TO START DELIVERING GIFTS...\n")
	
def help_elves():
	global elf_problems
	print("TIME TO HELP 3 ELVES")
	sleep(2)
	elf_problems = 0
	print("Finished helping elves. Now, num of problems are: %d\n" % elf_problems)
	for i in range(3):
		elves_limit.release()


	
#---FACTORY----
Thread(target=santa_claus, args=[]).start()		#SANTA CLAUS
for i in range(5):					#ELVES
	Thread(target=working, args=[i]).start()
for i in range(9):					#RAINDEER
	Thread(target=returning, args=[i]).start()
