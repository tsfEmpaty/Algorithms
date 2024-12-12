# O(n^2) time | O(1) space


def twoNumberSum(array, targetSum):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum and array[j] != array[i]:
                return [array[i], array[j]]
    return []


def main():
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10

    print(twoNumberSum(array, targetSum))  # => [-1, 11]


if __name__ == "__main__":
    main()
