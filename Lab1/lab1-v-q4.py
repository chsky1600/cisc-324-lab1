# Ethan Chankowsky
# SN: 20361117
# 2024-09-20
# Lab 1 - version for Question 4
# I confirm that this submission is my own work and is consistent with the Queen's
# regulations on Academic Integrity. I am the sole contributor of the modifications done.

import multiprocessing
import os
import time
import psutil

# A function to simulate I/O-bound task with a system call (simulates waiting for I/O)
def io_bound_system_call_worker(name):
    # Shortened output for brevity for this question
    print("Demonstrating an ")
    print(f"I/O-bound task for process {name} (PID: {os.getpid()}) is starting...") 

    # Simulate system call for I/O-bound task
    # TODO-1:
    print(f"Process {name} is entering system mode by a system-call")
    if os.name == 'posix':
        print(f"Process {name} is executing on a Unix-like system")
        os.system('ls')
    else:
        print(f"Process {name} is executing on a Windows system")
        os.system('dir')

    # After system call, simulate additional I/O wait time
    # TODO-2:
    print(f"Process {name} is waiting for more I/O simulated by sleep")
    time.sleep(3)
    print(f"Process {name} with PID {os.getpid()} has finished I/O-bound task")

# A function to simulate CPU-bound task (no waiting for I/O)
def cpu_bound_task(name):
    result = sum(range(1, (10**6) - 1))
    # Shortened output for brevity for this question
    print(f"CPU-bound task for process {name} with PID {os.getpid()} has finished with result {result}")

if __name__ == "__main__":

    start_time = time.time()
    # Measure initial CPU usage before tasks start
    print(f"\n -- Initial CPU usage: {psutil.cpu_percent(interval=1)}% \n")
    # Create a list to hold the process objects
    processes = []

    # To create I/O-bound processes with system call (simulating multiprogramming with I/O waits)
    for i in range(2):  
        process = multiprocessing.Process(target=io_bound_system_call_worker, args=(f'IO-Worker-{i}',))
        # TODO-4:
        processes.append(process)
        process.start()  # Start the I/O-bound process

    # To create CPU-bound processes (simulating CPU work)
    # TODO-5:
    for i in range(100):
        process = multiprocessing.Process(target=cpu_bound_task, args=(f'CPU-Task-{i}',))
        processes.append(process)
        process.start()  # Start the CPU-bound process

    # Wait for all processes to finish
    for process in processes:
        process.join()  # Ensure the main program waits for all processes to complete


    end_time = time.time()
    total_execution_time = end_time - start_time
    # Measure final CPU usage after immediately after processes are complete
    print(f"\n -- Final CPU usage: {psutil.cpu_percent(interval=1)}%\n")
    # TODO-6
    
    print(f"All processes finished. Total execution time: {total_execution_time} seconds")

    
    
