import multiprocessing
import os
import time

# A function to simulate I/O-bound task with a system call (simulates waiting for I/O)
def io_bound_system_call_worker(name):
    print("Demonstrating an I/O-bound task")
    print(f"Process {name} (PID: {os.getpid()}) is starting (I/O-bound task)...")

    # Simulate system call for I/O-bound task
    # TODO-1:
    # 1- Print "Process {name} is entering system mode by a system-call"
    # 2- Check the type of operating system.If it’s posix, the system is Unix - like(Linux, macOS).
    # If it’s not, assume it’s Windows.
    # 3- execute a system shell command to list directory


    # After system call, simulate additional I/O wait time
    # TODO-2:
    # 4- Print "Process {name} is waiting for more I/O simulated by sleep"
    # 5- delay the process for 5 seconds
    # 6- Print "Process {name} with PID { } has finished I/O-bound task"

# A function to simulate CPU-bound task (no waiting for I/O)
def cpu_bound_task(name):
    print("Demonstrating a CPU-bound task")
    # TODO-3:
    # 7- Print "Process {name} with PID {  } is starting CPU-bound task.."
    # 8- calculates the sum of all integers from 1 to 10^6 −1
    # 9- Print "Process {name} with PID { } has finished CPU-bound task with result {   }"

if __name__ == "__main__":

    start_time = time.time()
    # Create a list to hold the process objects
    processes = []

    # To create I/O-bound processes with system call (simulating multiprogramming with I/O waits)
    for i in range(2):  # Let's create 2 I/O-bound processes with system call
        process = multiprocessing.Process(target=io_bound_system_call_worker, args=(f'IO-Worker-{i}',))
        # TODO-4:
        # 10- Append the process into processes
        # 11- start the I/O-bound process

        processes.append(process)
        process.start()  # Start the I/O-bound process

    # To create CPU-bound processes (simulating CPU work)
    # TODO-5:
    # 12- Create a number of CPU-bound processes
    # 13- Append the process into processes
    # 14- start the CPU-bound process

    # Wait for all processes to finish
    for process in processes:
        process.join()  # Ensure the main program waits for all processes to complete

    # TODO-6
    # 15- Record the end-time of execution
    # 16- Print "All processes finished. Total execution time: {  } seconds"
