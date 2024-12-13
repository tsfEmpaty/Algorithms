# Branch Sums

You're given a <code>Node</code> class that has a <code>name</code> and an
array of optional <code>children</code> nodes. When put together, nodes form
an acyclic tree-like structure.

Implement the <code>depthFirstSearch</code> method on the
<code>Node</code> class, which takes in an empty array, traverses the tree
using the Depth-first Search approach (specifically navigating the tree from
left to right), stores all of the nodes' names in the input array, and returns
it.

If you're unfamiliar with Depth-first Search, we recommend watching the
Conceptual Overview section of this question's video explanation before
starting to code.

## Sample Input

```python
graph = A
     /  |  \
    B   C   D
   / \     / \
  E   F   G   H
     / \   \
    I   J   K
```

## Sample Output

```python
["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
```

<details>
  <summary>Hint 1</summary>

The Depth-first Search algorithm works by traversing a graph branch by branch. In other words, before traversing any Node's sibling Nodes, its children nodes must be traversed. How can you simply and effectively keep track of Nodes' sibling Nodes as you traverse them, all the while retaining the order in which you must traverse them?

</details>

<details>
  <summary>Hint 2</summary>

Start at the root Node and try simply calling the depthFirstSearch method on all of its children Nodes. Then, call the depthFirstSearch method on all children Nodes of each child node. Keep applying this logic until the entire graph has been traversed. Don't forget to add the current Node's name to the input array at every call of depthFirstSearch.

</details>

<details>
  <summary>Optimal Space & Time Complexity</summary>

O(v + e) time | O(v) space - where v is the number of vertices of the input graph and e is the number of edges of the input graph

</details>

---

## 🔗 Solution

<div style="text-align: center; flex-box: flex">
  <a href="./solution.py" style="display: inline-block; background-color: #4CAF50; color: white; padding: 10px 15px; text-align: center; text-decoration: none; border-radius: 5px;">View Solution</a>
</div>
