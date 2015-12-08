#! python
# For floor division on line 16
from __future__ import division
# Import random number generator for testing
import randomNumberGenerator as rndNrs


# The recursive splitting of the arrays
def mergesort_internal(inputlist):
    size = len(inputlist)
    if size < 2:
        # If only one element in list (basecase)
        pass
    else:
        # Divide
        midpoint = size // 2
        lower_half = mergesort_internal(inputlist[:midpoint])
        upper_half = mergesort_internal(inputlist[midpoint:])

        # Conquer
        i, j, k = 0, 0, 0
        while i < len(lower_half) and j < len(upper_half):
            if upper_half[j] < lower_half[i]:
                inputlist[k] = upper_half[j]
                j += 1
            else:
                inputlist[k] = lower_half[i]
                i += 1
            k += 1

        # If upper_half emptied first:
        while i < len(lower_half):
            inputlist[k] = lower_half[i]
            i, k = i + 1, k + 1

        # if lower_half emptied first:
        while j < len(upper_half):
            inputlist[k] = upper_half[j]
            j, k = j + 1, k + 1

    return inputlist


def mergesort(inputlist, start=None, stop=None):
    size = len(inputlist)

    # Check first if whole array should be sorted
    if start is None:
        start = 0
    if stop is None:
        stop = size

    # Check then whether indices are valid
    if stop - start < 1 or size < start - stop:
        return [-1]

    # Perform merge sort
    return mergesort_internal(inputlist[start:stop])

# Code for executing/testing
print("Starting...")

# Get random number of elements to sort
amountOfIntsSorted = rndNrs.random_ints(1, lower=4, upper=100)
amountOfIntsSorted = amountOfIntsSorted[0]

# Get list of random ints
testList = rndNrs.random_ints(amountOfIntsSorted, lower=0, upper=10000)
# testList = [2, 24, 4, 5, 3, 1]
print(testList)

print("Sorting the above list...")
sortedList = mergesort(testList)

print("Sorted list:")
print(sortedList)

# Check if list was sorted correctly, by using python's sorted() as comparison
correctList = sorted(testList)
correctlySorted = True
for x in xrange(amountOfIntsSorted):
    if sortedList[x] != correctList[x]:
        correctlySorted = False

if correctlySorted:
    print("List was sorted correctly!!! =D")
else:
    print("List was sorted incorrectly!!! =(")
