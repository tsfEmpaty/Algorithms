# O(n) time | O(1) space - where n is the input number


def getNthFib(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a
