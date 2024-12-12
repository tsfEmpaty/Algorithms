# O(n) time | O(1) space


def isValidSubsequence(array, sequence):
    for element in array:
        if element == sequence[0]:
            sequence.pop(0)
            if not sequence:
                return True
    return False


def main():
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]

    print(isValidSubsequence(array, sequence))  # => True


if __name__ == "__main__":
    main()
