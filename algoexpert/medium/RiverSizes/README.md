# River Sizes

You're given a two-dimensional array (a matrix) of potentially unequal height
and width containing only <code>0</code>s and <code>1</code>s. Each
<code>0</code> represents land, and each <code>1</code> represents part of a
river. A river consists of any number of <code>1</code>s that are either
horizontally or vertically adjacent (but not diagonally adjacent). The number
of adjacent <code>1</code>s forming a river determine its size.

Note that a river can twist. In other words, it doesn't have to be a straight
vertical line or a straight horizontal line; it can be L-shaped, for example.

Write a function that returns an array of the sizes of all rivers represented
in the input matrix. The sizes don't need to be in any particular order.

## Sample Input

```python
matrix = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0],
]
```

## Sample Output

```javascript
[1, 2, 2, 2, 5] // The numbers could be ordered differently.

// The rivers can be clearly seen here:
// [
//   [1,  ,  , 1,  ],
//   [1,  , 1,  ,  ],
//   [ ,  , 1,  , 1],
//   [1,  , 1,  , 1],
//   [1,  , 1, 1,  ],
// ]
```

<details>
  <summary>Hint 1</summary>

Since you must return the sizes of rivers, which consist of horizontally and vertically adjacent 1s in the input matrix, you must somehow keep track of groups of neighboring 1s as you traverse the matrix. Try treating the matrix as a graph, where each element in the matrix is a node in the graph with up to 4 neighboring nodes (above, below, to the left, and to the right), and traverse it using a popular graph-traversal algorithm like Depth-first Search or Breadth-first Search.

</details>

<details>
  <summary>Hint 2</summary>

By traversing the matrix using DFS or BFS as mentioned in Hint #1, any time that you encounter a 1 you can traverse the entire river that this 1 is a part of (and keep track of its size) by simply iterating through the given node's neighboring nodes and their own neighboring nodes so long as the nodes are 1s.

</details>

<details>
  <summary>Hint 3</summary>

Naturally, many nodes in the graph mentioned in Hint #1 will have overlapping neighboring nodes, and as you traverse the matrix, you will undoubtedly encounter nodes that you have previously visited. In order to prevent mistakenly calculating the same river's size multiple times and to avoid doing needless computational work, try keeping track of every node that you visit in an auxiliary data structure and only performing important computations on unvisited nodes. What data structure would be ideal here?

</details>

<details>
  <summary>Optimal Space & Time Complexity</summary>

O(wh) time | O(wh) space - where w and h are the width and height of the input matrix

</details>

---

## 🔗 Solution

<div style="text-align: center; flex-box: flex">
  <a href="./solution.py" style="display: inline-block; background-color: #4CAF50; color: white; padding: 10px 15px; text-align: center; text-decoration: none; border-radius: 5px;">View Solution</a>
</div>
