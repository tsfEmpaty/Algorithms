# O(log(n)) time | O(1) space - where n is the length of the input array


def binarySearch(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1
