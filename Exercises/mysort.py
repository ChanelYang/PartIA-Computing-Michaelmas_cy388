
import random

def mysort(N):
    """Create a randomly ordered list of integers of length N, and return the sorted list"""
    # Create randomly ordered list
    x = random.sample(range(0, N), N)

    # Return sorted list of numbers
    return sorted(x)
