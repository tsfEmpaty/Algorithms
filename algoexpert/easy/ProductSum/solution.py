# O(n) time | O(d) space - where n is the total number of elements in the array, including sub-elements, and d is the greatest depth of "special" arrays in the array


# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth=1):
    return depth * sum(
        productSum(element, depth + 1) if isinstance(element, list) else element
        for element in array
    )
