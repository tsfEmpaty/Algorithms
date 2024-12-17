# Validate BST

Write a function that takes in a potentially invalid Binary Search Tree (BST)
and returns a boolean representing whether the BST is valid.

Each <code>BST</code> node has an integer <code>value</code>, a
<code>left</code> child node, and a <code>right</code> child node. A node is
said to be a valid <code>BST</code> node if and only if it satisfies the BST
property: its <code>value</code> is strictly greater than the values of every
node to its left; its <code>value</code> is less than or equal to the values
of every node to its right; and its children nodes are either valid
<code>BST</code> nodes themselves or <code>None</code> / <code>null</code>.

A BST is valid if and only if all of its nodes are valid
<code>BST</code> nodes.

## Sample Input

```python
tree =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14
```

## Sample Output

```python
True
```

<details>
  <summary>Hint 1</summary>

Every node in the BST has a maximum possible value and a minimum possible value. In other words, the value of any given node in the BST must be strictly smaller than some value (the value of its closest right parent) and must be greater than or equal to some other value (the value of its closest left parent).

</details>

<details>
  <summary>Hint 2</summary>

Validate the BST by recursively calling the validateBst function on every node, passing in the correct maximum and minimum possible values to each. Initialize those values to be -Infinity and +Infinity.

</details>

<details>
  <summary>Optimal Space & Time Complexity</summary>

O(n) time | O(d) space - where n is the number of nodes in the BST and d is the depth (height) of the BST

</details>

---

## 🔗 Solution

<div style="text-align: center; flex-box: flex">
  <a href="./solution.py" style="display: inline-block; background-color: #4CAF50; color: white; padding: 10px 15px; text-align: center; text-decoration: none; border-radius: 5px;">View Solution</a>
</div>
