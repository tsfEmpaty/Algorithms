# O(n) time | O(d) space - where n is the number of nodes in the BST and d is the depth (height) of the BST


def validateBst(tree, leftParent=None, rightParent=None):
    if tree is None:
        return True
    elif leftParent is not None and tree.value >= leftParent.value:
        return False
    elif rightParent is not None and tree.value < rightParent.value:
        return False
    return validateBst(tree.left, tree, rightParent) and validateBst(
        tree.right, leftParent, tree
    )


# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
