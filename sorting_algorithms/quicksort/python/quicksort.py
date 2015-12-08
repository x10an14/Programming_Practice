#! python
from __future__ import division
import random


def random_ints(amount, lower=0, upper=100):
    return [random.randrange(lower, upper + 1) for i in xrange(amount)]


def print_list(array, start_index=None, stop_index=None):
    if start_index is None:
        start_index = 0
    if stop_index is None:
        stop_index = len(array) - 1

    print_string = "["
    for x in xrange(start_index, stop_index - 1):
        print_string += str(array[x]) + ", "
    print_string += str(array[stop_index]) + "]"

    print(print_string)


def quicksort(inputlist, start=None, stop=None):
    size = len(inputlist)

    # Check first if whole array should be sorted
    if start is None:
        start = 0
    if stop is None:
        stop = size - 1

    # Check then whether indices are valid
    if not 0 <= start < stop < len(inputlist):
        return [-1]

    # Perform merge sort
    return quicksort_median(inputlist, start, stop)


def find_index_of_median(array, first_index, mid_index, last_index):
    median_index = None
    if array[first_index] <= array[mid_index]:
        # if array[mid_index] > array[first_index]
        if array[mid_index] <= array[last_index]:
            # if array[last_index] > array[mid_index] > array[first_index]
            median_index = mid_index
        else:
            if array[first_index] <= array[last_index]:
                # if array[mid_index] > array[last_index] > array[first_index]
                median_index = last_index
            else:
                # if array[mid_index] > array[first_index] > array[last_index]
                median_index = first_index
    else:
        # if array[first_index] > array[mid_index]
        if array[first_index] <= array[last_index]:
            # if array[last_index] > array[first_index] > array[mid_index]
            median_index = first_index
        else:
            if array[mid_index] <= array[last_index]:
                # array[first_index] > array[last_index] > array[mid_index]
                median_index = last_index
            else:
                # array[first_index] > array[mid_index] > array[last_index]
                median_index = mid_index
    return median_index


def quicksort_median(array, start_index, stop_index):

    # Check first if there's even enough to find a median
    size = stop_index - start_index + 1
    if size < 3:
        if size > 1 and array[start_index] > array[stop_index]:
            # If the first one is larger than second, switch them
            temp = array[stop_index]
            array[stop_index] = array[start_index]
            array[start_index] = temp
        return

    mid_index = start_index + (stop_index - start_index) // 2
    pivot = find_index_of_median(array, start_index, mid_index, stop_index)

    i, j, pivot = start_index, stop_index, array[pivot]
    while i <= j:
        # Find the next element from the bottom bigger than pivot
        while array[i] < pivot:
            i += 1

        # Find the next element from the top smaller than pivot
        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    if start_index < j:
        quicksort_median(array, start_index, j)

    if i < stop_index:
        quicksort_median(array, i, stop_index)


# Code for executing/testing
print("Starting...")

# Get random number of elements to sort
amountOfIntsSorted = random_ints(1, lower=4, upper=100)
amountOfIntsSorted = amountOfIntsSorted[0]
# amountOfIntsSorted = 6

# Get list of random ints
testList = random_ints(amountOfIntsSorted, lower=0, upper=10000)
# testList = [2, 24, 4, 5, 3, 1]
print(testList)

print("Sorting the above list...")
quicksort(testList)

print("Sorted list:")
print(testList)

# Check if list was sorted correctly, by using python's sorted() as comparison
correctList = sorted(testList)
correctlySorted = True
for x in xrange(amountOfIntsSorted):
    if testList[x] != correctList[x]:
        print("Element {} is wrong. {} != {}".format(x, testList[x], correctList[x]))
        correctlySorted = False

if correctlySorted:
    print("List was sorted correctly!!! =D")
else:
    print("List was sorted incorrectly!!! =(")
