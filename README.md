## SyncExcercises

**This notes are extracted from [Gunnar Wolf's Operating Systems lectures](http://gwolf.sistop.org/laminas/06-primitivas-sincronizacion.pdf) at the National Autonomous University of Mexico (UNAM) and [Allen B. Downey's The Little Book of Semaphores](http://greenteapress.com/semaphores/LittleBookOfSemaphores.pdf). 



### Synchronization 

In computer systems, synchronization refers to relationships among events, any number of events and any kind of relationship. We often are concerned with **synchronization constraints**: 

1. **Serialization: ** event A must happen before event B. 
2. **Mutal exclusion:** events A and B must NOT happen at the same time. 

To understand software synchronization, we must have a model of how computer programs run. In the simplest model, computers execute one instruction after another in sequence. In this model, synchronization is trivial because we can tell the order of events by looking at the program. If event A comes before event B, it will be executed first. 

However, if the computer has multiple processors running at the same time it is not easy to know if an event on one processor is executed before a statement on another. 

Another possibility is that the processor is running multiple threads of execution. A thread is a sequence of instructions that execute sequentially. If there are multiple threads, then the proceessor can work on one for a while, then switch to another and so on. 

*In general, the programmer has no control over when each thread runs; the operating system (specifically the scheduler) makes those decisions.*

---

#### Concurrency

**Concurrency:** two events are concurrent if we cannot tell by looking at the program which will happen first. 

Concurrent programs are often **non-deterministic**, which means that it's not possible to tell, by looking at the program, what will happen when it executes. 

---

#### Shared variables

Most of the time, variables in most threads are **local**, meaning that they belong to a single thread and no other threads can access them. But there are also times when variables are **shared** among two or more threads. Which is one of the ways thread interact with each other. 

##### Concurrent Updates

An unpdate is an operation that reads the value of a variable, computes a new value based on the old value, and writes the new value. A problem of synchronization might be presented when we have two threads trying to read and update the same variable. 

Some computers provide operations that cannot be interrupted and they're called **atomic** operations. 

##### How can we write concurrent programs ? 

The most common alternative is to make the assumption that all updates and all writes are not atomic, and to use synchronization constraints to control concurrent access to shared variables. 

The most common constraint is called **mutal exclusion (mutex).** Mutual exclusion guarantees that only one thread accesses a shared variable at a time, eliminating the kinds of synchronization errors. 

---



### Semaphores

In real life, a semaphore is a system of signals used to communicate visually. In software, a semaphore is a data structure that is useful for solving a variety of synchronization problems. Semaphores were invented by Edsger Dijkstra. 

#### Definition 

1. When you create a semaphore, you can initialize its value to any integer, but after that, there are only two operations allowed (perform an increment by one or perform a decrement by one). You cannot read the current value of the semaphore. 
2. When a thread decrements the semaphore, if the result is negative, the thread blocks itself and cannot continue until another thread increments the semaphore. 
3. When a thread increments the semaphore, if there are other threads waiting, one of the waiting threads gets unblocked. 

#### Consequences of the definition 

- There is no way to know before a thread decrements a semaphore whether it will block or not. 
- After a thread increments a semaphore and another thread gets woken up, both threads continue running concurrently. 
- When you signal a semaphore, you don't necessarily know whether another thread is waiting.

#### Why semaphores? 

- Impose delibarate constraints that help programmers avoid errors. 
- Solutions using semaphores are often clean and organized.
- Semaphores can be implemented efficiently on many systems, so solutions that use semaphores are portable and usually efficient. 

### 





