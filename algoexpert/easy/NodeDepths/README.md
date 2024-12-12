# Node Depths

The distance between a node in a Binary Tree and the tree's root is called the
node's depth.

Write a function that takes in a Binary Tree and returns the sum of its nodes'
depths.

Each <code>BinaryTree</code> node has an integer <code>value</code>, a
<code>left</code> child node, and a <code>right</code> child node. Children
nodes can either be <code>BinaryTree</code> nodes themselves or
<code>None</code> / <code>null</code>.

## Sample Input

```python
tree =    1
       /     \
      2       3
    /   \   /   \
   4     5 6     7
 /   \
8     9
```

## Sample Output

```javascript
16
// The depth of the node with value 2 is 1.
// The depth of the node with value 3 is 1.
// The depth of the node with value 4 is 2.
// The depth of the node with value 5 is 2.
// Etc..</span>
// Summing all of these depths yields 16.
```

<details>
  <summary>Hint 1</summary>

As obvious as it may seem, to solve this question, you'll have to figure out how to compute the depth of any given node; once you know how to do that, you can compute all of the depths and add them up to obtain the desired output.

</details>

<details>
  <summary>Hint 2</summary>

To compute the depth of a given node, you need information about its position in the tree. Can you pass this information down from the node's parent?

</details>

<details>
  <summary>Hint 3</summary>

The depth of any node in the tree is equal to the depth of its parent node plus 1. By starting at the root node whose depth is 0, you can pass down to every node in the tree its respective depth, and you can implement the algorithm that does this and that sums up all of the depths either recursively or iteratively.

</details>

<details>
  <summary>Optimal Space & Time Complexity</summary>

Average case: when the tree is balanced
O(n) time | O(h) space - where n is the number of nodes in the Binary Tree and h is the height of the Binary Tree

</details>

---

## 🔗 Solutions

<div style="text-align: center;">
  <a href="./solution_recursive.py" style="display: inline-block; background-color: #4CAF50; color: white; padding: 10px 15px; text-align: center; text-decoration: none; border-radius: 5px; margin-right: 10px;">View First Solution</a>
  <a href="./solution_while_loop.py" style="display: inline-block; background-color: #008CBA; color: white; padding: 10px 15px; text-align: center; text-decoration: none; border-radius: 5px;">View Second Solution</a>
</div>
