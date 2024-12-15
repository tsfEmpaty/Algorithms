# Best: O(n) time | O(1) space - where n is the length of the input array
# Average: O(n^2) time | O(1) space - where n is the length of the input array
# Worst: O(n^2) time | O(1) space - where n is the length of the input array


def bubbleSort(array):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
    return array
