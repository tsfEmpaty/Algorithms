# O(n) time | O(n) space


def twoNumberSum(array, targetSum):
    hashtable = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in hashtable:
            return [potentialMatch, num]
        else:
            hashtable[num] = True
    return []


def main():
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10

    print(twoNumberSum(array, targetSum))  # => [-1, 11]


if __name__ == "__main__":
    main()
