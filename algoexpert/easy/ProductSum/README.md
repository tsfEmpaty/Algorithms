# Product Sum

Write a function that takes in a "special" array and returns its product sum.

A "special" array is a non-empty array that contains either integers or other
"special" arrays. The product sum of a "special" array is the sum of its
elements, where "special" arrays inside it are summed themselves and then
multiplied by their level of depth.

The depth of a "special" array is how far nested it is. For instance, the
depth of <code>[]</code> is <code>1</code>; the depth of the inner array in
<code>[[]]</code> is <code>2</code>; the depth of the innermost array in <code>[[[]]]</code> is <code>3</code>.

Therefore, the product sum of <code>[x, y]</code> is <code>x + y</code>; the
product sum of <code>[x, [y, z]]</code> is <code>x + 2 _ (y + z)</code>; the
product sum of <code>[x, [y, [z]]]</code> is <code>x + 2 _ (y + 3z)</code>.

## Sample Input

```python
array= [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
```

## Sample Output

```javascript
12 // calculated as: 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)
```

<details>
  <summary>Hint 1</summary>

Try using recursion to solve this problem.

</details>

<details>
  <summary>Hint 2</summary>

Initialize the product sum of the "special" array to 0. Then, iterate through all of the array's elements; if you come across a number, add it to the product sum; if you come across another "special" array, recursively call the productSum function on it and add the returned value to the product sum. How will you handle multiplying the product sums at a given level of depth?

</details>

<details>
  <summary>Hint 3</summary>

Have the productSum function take in a second parameter: the multiplier, initialized to 1. Whenever you recursively call the productSum function, pass in the multiplier incremented by 1.

</details>

<details>
  <summary>Optimal Space & Time Complexity</summary>

O(n) time | O(d) space - where n is the total number of elements in the array, including sub-elements, and d is the greatest depth of "special" arrays in the array

</details>

---

## 🔗 Solutions

<div style="text-align: center;">
  <a href="./solution.py" style="display: inline-block; background-color: #4CAF50; color: white; padding: 10px 15px; text-align: center; text-decoration: none; border-radius: 5px; margin-right: 10px;">View Solution</a>
</div>
