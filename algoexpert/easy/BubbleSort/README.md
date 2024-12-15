# Bubble Sort

Write a function that takes in an array of integers and returns a sorted
version of that array. Use the Bubble Sort algorithm to sort the array.

If you're unfamiliar with Bubble Sort, we recommend watching the Conceptual
Overview section of this question's video explanation before starting to code.

## Sample Input

```python
array = [8, 5, 2, 9, 5, 6, 3]
```

## Sample Output

```python
[2, 3, 5, 5, 6, 8, 9]
```

<details>
  <summary>Hint 1</summary>

Traverse the input array, swapping any two numbers that are out of order and keeping track of any swaps that you make. Once you arrive at the end of the array, check if you have made any swaps; if not, the array is sorted and you are done; otherwise, repeat the steps laid out in this hint until the array is sorted.

</details>

<details>
  <summary>Optimal Space & Time Complexity</summary>

Best: O(n) time | O(1) space - where n is the length of the input array
Average: O(n^2) time | O(1) space - where n is the length of the input array
Worst: O(n^2) time | O(1) space - where n is the length of the input array

</details>

---

## 🔗 Solution

<div style="text-align: center; flex-box: flex">
  <a href="./solution.py" style="display: inline-block; background-color: #4CAF50; color: white; padding: 10px 15px; text-align: center; text-decoration: none; border-radius: 5px;">View Solution</a>
</div>
