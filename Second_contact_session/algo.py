# Quick sort algorithm
import random
def quicksort(array):
    if len(array) <= 1:
        return array

    # Choose a random pivot element
    pivot = random.choice(array)

    # Partition the array around the pivot element
    less, greater = [], []
    for element in array:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            greater.append(element)

    # Recursively sort the subarrays
    return quicksort(less) + [pivot] + quicksort(greater)