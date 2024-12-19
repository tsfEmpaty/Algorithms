# O(n) time | O(1) space - where n is the length of the array


def maximizeExpression(array):
    a = b = c = d = float("-inf")
    if len(array) < 4:
        return 0
    for x in array:
        A = max(a, x)
        B = max(b, a - x)
        C = max(c, b + x)
        D = max(d, c - x)
        a, b, c, d = A, B, C, D
    return d
