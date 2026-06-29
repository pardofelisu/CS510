"""
A multithreaded program template.
"""

import threading

def functionOne():
    """
    enhance this function to perform some function
    """
    #creates a triangle pattern of asterisks
    for i in range(5):
        print("*" * (i + 1))
    print("function 1")

def functionTwo():
    """
    enhance this function to perform some function
    """
    #creates a square pattern of asterisks
    for i in range(5):
        print("*" * 5)
    print("function 2")

def functionThree():
    """
    enhance this function to perform some function
    """
    #creates a diamond pattern of asterisks
    for i in range(5):
        print(" " * (4 - i) + "*" * (2 * i + 1))
    for i in range(3, -1, -1):
        print(" " * (4 - i) + "*" * (2 * i + 1))
    print("function 3")

lambda_function = lambda: print("completed all threads")

def main():
    """
    Entry point of the program:  Create, start and join threads
    """

    #Build thread objects that map to distinct functions
    one_thread = threading.Thread(
        target=functionOne,
        name="one-thread"
    )

    two_thread = threading.Thread(
        target=functionTwo,
        name="two-thread"
    )

    three_thread = threading.Thread(
        target=functionThree,
        name="three-thread"
    )

    #Start threads concurrently
    one_thread.start()
    two_thread.start()
    three_thread.start()

    #Wait for all threads to finish execution
    one_thread.join()
    two_thread.join()
    three_thread.join()
    lambda_function()

if __name__ == "__main__":
    main()