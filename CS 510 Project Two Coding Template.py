"""
    Class:   CS-510
    Author:  <Tashi Anderson>
    Date:    <June 21, 2026>

    Description:  Each function that needs to be completed has a comment at the top with
                  TODO written in it with instructions.

                  Within the function is a section with the comment #TODO where you will
                  insert your code as per the instructions.
"""  
import os
import psutil  # requires pip install
import sys
import threading

"""
  Three provided Utility functions to use
"""
def printBlankLines(lines: int):
    for i in range(lines):
        print("")

def printMsg1(num):
    print("Thread 1 cubed: {}" .format(num * num * num))


def printMsg2(num):
    print("Thread 2 squared: {}" .format(num * num))


"""
   TODO This function will display information about a file, size and file information.
   You can provide your own or use the projecttwo.txt file.

   Use psutil to get initial file information.
"""
def getFileDiskUsageStatistics() -> None:
    print("Getting Disk Statistics")
    file_name = "./CS 510 Project Two Coding Template.py"  # Change this to your file path if needed

    #TODO INSERT YOUR CODE HERE
    file_stats = psutil.disk_usage(file_name)
    print(f"File: {file_name}")
    print(f"Total: {file_stats.total}")
    print(f"Used: {file_stats.used}")
    print(f"Free: {file_stats.free}")

    printBlankLines(2)

"""
   TODO This should use psutil to retrieve standard and 
   virtual memory statistics
"""
def getMemoryStatistics() -> None:
    print("Getting Memory Statistics")

    #TODO INSERT YOUR CODE HERE
    virtual_memory = psutil.virtual_memory()
    print(f"Total Memory: {virtual_memory.total}")
    print(f"Available Memory: {virtual_memory.available}")

    printBlankLines(2)

"""
   TODO This should use psutil to retrieve CPU statistics, including
   information on processes.
"""
def getCpuStatistics() -> None:
    print("Getting CPU Statistics")
    
    #TODO INSERT YOUR CODE HERE
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")
    processes = psutil.process_iter(['pid', 'name', 'username'])
    for process in processes:
        print(f"PID: {process.info['pid']}, Name: {process.info['name']}, User: {process.info['username']}")

    printBlankLines(2)


"""
   TODO This function will show multi threading capabilities.

   Two threads should be created.
    
   One used to call the function "printMsg1" provided above.

   A second thread should call the function "printMsg2" provided above.
"""
def showThreadingExample() -> None:
    print("Demonstrating Threading")
   
    #TODO INSERT YOUR CODE HERE
    thread1 = threading.Thread(target=printMsg1, args=(5,))
    thread2 = threading.Thread(target=printMsg2, args=(5,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Done With Threading!")

    printBlankLines(2)

"""
   TODO This function shows system error handling.

   Since out of memory, or out of disk space errors are difficult to create,
   we will use a divide by zero error and show the error handling being executed.
"""
def showErrorHandling() -> None:
    print("Demonstrating Error Handling")
    try:
       
       #TODO Insert your code here to cause a divide by zero error
         res = 10 / 0
    
    except ZeroDivisionError:
        print("You can't divide by zero!")
        
    except MemoryError:
        print("Memory Error!")
        
    else:
        print("Result is", res)
        
    finally:
        print("Execution complete.")

    printBlankLines(2)

"""
   Main function, does not require modification.

   This calls the specific functions.
"""
def main() -> int:
    print("Starting Program")
    print("=============================")
   
    getFileDiskUsageStatistics()   
    
    getCpuStatistics()
    
    getMemoryStatistics()

    showThreadingExample()

    showErrorHandling()


if __name__ == '__main__':
    sys.exit(main()) 