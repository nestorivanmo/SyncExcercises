## Synchronization patterns

**This notes are extracted from [Gunnar Wolf's Operating Systems lectures](http://gwolf.sistop.org/laminas/06-primitivas-sincronizacion.pdf) at the National Autonomous University of Mexico (UNAM) and [Allen B. Downey's The Little Book of Semaphores](http://greenteapress.com/semaphores/LittleBookOfSemaphores.pdf). 

A programming design pattern is a programming structure that tends to look like natural responses in the coding of good programmers. It's convenient to know them and have them in mind to recognize situations in which we could use them. 

### Basic synchronization patterns

#### Signaling 

One thread sends a signal to another thread to indicate that something has happened. Signaling makes it possible to guarantee that a section of code in one thread will run before a section of code in anothe thread. 

#### Rendezvous 

Two threads must wait for each other (rendezvous), in some point, to continue execution and neither is allowed to proceed until both have arrived. 

#### Mutex 

A second common use for semaphores is to enforce mutual exclusion (mutex). The mutex guarantees that only one thread accesses the shared variable at a time. 

A mutex is like a token that passes from one thread to another, allowing one thread at a time to proceed. In order for a thread to access a shared variable, it has to *get* the mutex; when its done, it *releases* the mutex. Only one thread can hold the mutex at a time. 

#### Multiplex

This pattern allows multiple threads to run in the critical section at the same time, but it enforces an upper limit on the number of concurrent threads. No more than ```n``` threads can run in the critical section at the same time. 

#### Barrier

Generalize the rendezvous solution to run several threads (not only two). The synchronization requirement is that no thread executes critical point until after all threads have executed rendezvous. 

#### Reusable barrier 

Often a set of cooperating 

