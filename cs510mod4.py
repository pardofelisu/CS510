"""
A program that prints basic CPU and memory details
using psutil library.

The display part is provided, just fill out the first
three functions

Modify as you like, experimentation is fun!
"""

import psutil

def get_cpu_usage():
    """return the current cpu usage percentage, use posutil"""
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent

def get_cpu_count():
    """return the number of logical cpu cores detected on the system"""
    return psutil.cpu_count(logical=True)

def get_memory_stats():
    """
    return the total memory, available memory, and memory used.
    Values returned are in gigabytes for readability.
    Use psutil, get virtual_memory() and then calcularted total, used and available
    """

    BYTES_PER_GB = 1024 ** 3
    memory = psutil.virtual_memory()


    total = memory.total / BYTES_PER_GB
    used = memory.used / BYTES_PER_GB
    available = memory.available / BYTES_PER_GB
    return total, used, available

def display_resource_report():
    "display a formatted report of cpu and memory information"
    mem_total, mem_used, mem_available = get_memory_stats()

    print("\n===== System Resource Report =====")
    print(f"CPU Usage:          {get_cpu_usage():5.1f}%")
    print(f"CPU Cores:            {get_cpu_count()}")
    print(f"Total Memory:        {mem_total:5.2f} GB")
    print(f"Memory Usage:        {mem_used:5.2f} GB")
    print(f"Memory Available:    {mem_available:5.2f} GB")
    print("===================================\n")

def main():
    """program entry point"""
    display_resource_report()

if __name__ == "__main__":
    main()