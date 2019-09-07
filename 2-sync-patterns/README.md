## Synchronization patterns

**This notes are extracted from [Gunnar Wolf's Operating Systems lectures](http://gwolf.sistop.org/laminas/06-primitivas-sincronizacion.pdf) at the National Autonomous University of Mexico (UNAM) and [Allen B. Downey's The Little Book of Semaphores](http://greenteapress.com/semaphores/LittleBookOfSemaphores.pdf). 

A programming design pattern is a programming structure that tends to look like natural responses in the coding of good programmers. It's convenient to know them and have them in mind to recognize situations in which we could use them. 

### Basic synchronization patterns

#### Signaling 

One thread sends a signal to another thread to indicate that something has happened. Signaling makes it possible to guarantee that a section of code in one thread will run before a section of code in anothe thread. 

#### Rendezvous 

Two threads must wait for each other (rendezvous), in some point, to continue execution and neither is allowed to proceed until both have arrived. 

#### Mutex 

