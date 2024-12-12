# O(n) time | O(h) space - where n is the number of nodes in the Binary Tree and h is the height of the Binary Tree


def nodeDepths(root, depth=0):
    if root is not None:
        return (
            depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
        )
    return 0


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
