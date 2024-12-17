# Longest Peak

Write a function that takes in an array of integers and returns the length of
the longest peak in the array.

A peak is defined as adjacent integers in the array that are <b>strictly</b>
increasing until they reach a tip (the highest value in the peak), at which
point they become <b>strictly</b> decreasing. At least three integers are required to
form a peak.

For example, the integers <code>1, 4, 10, 2</code> form a peak, but the
integers <code>4, 0, 10</code> don't and neither do the integers
<code>1, 2, 2, 0</code>. Similarly, the integers <code>1, 2, 3</code> don't
form a peak because there aren't any strictly decreasing integers after the
<code>3</code>.

## Sample Input

```python
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
```

## Sample Output

```javascript
6 // 0, 10, 6, 5, -1, -3
```

<details>
  <summary>Hint 1</summary>

You can solve this question by iterating through the array from left to right once.

</details>

<details>
  <summary>Hint 2</summary>

Iterate through the array from left to right, and treat every integer as the potential tip of a peak. To be the tip of a peak, an integer has to be strictly greater than its adjacent integers. What can you do when you find an actual tip?

</details>

<details>
  <summary>Hint 3</summary>

As you iterate through the array from left to right, whenever you find a tip of a peak, expand outwards from the tip until you no longer have a peak. Given what peaks look like and how many peaks can therefore fit in an array, realize that this process results in a linear-time algorithm. Make sure to keep track of the longest peak you find as you iterate through the array.

</details>

<details>
  <summary>Optimal Space & Time Complexity</summary>

O(n) time | O(1) space - where n is the length of the input array

</details>

---

## 🔗 Solution

<div style="text-align: center; flex-box: flex">
  <a href="./solution.py" style="display: inline-block; background-color: #4CAF50; color: white; padding: 10px 15px; text-align: center; text-decoration: none; border-radius: 5px;">View Solution</a>
</div>
