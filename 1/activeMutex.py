#!/usr/bin/python3
import threading
import time 

mostrar = 0 
candado = threading.Lock() 

def par(num):
	global mostrar
	while True: 
		candado.acquire() 
		print('%d-%s' % (mostrar,num))
		mostrar = 1
		candado.release() 
		time.sleep(0.5)

def impar(num):
	global mostrar
	while True:
		candado.acquire()
		print('%d-%s' % (mostrar,num))
		mostrar = 0 
		candado.release()
		time.sleep(0.5)


threading.Thread(target=par, args=['par']).start()
threading.Thread(target=impar, args=['impar']).start()
