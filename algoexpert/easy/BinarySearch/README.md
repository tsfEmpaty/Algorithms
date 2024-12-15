# Binary Search

Write a function that takes in a sorted array of integers as well as a target
integer. The function should use the Binary Search algorithm to determine if
the target integer is contained in the array and should return its index if it
is, otherwise <code>-1</code>.

If you're unfamiliar with Binary Search, we recommend watching the Conceptual
Overview section of this question's video explanation before starting to code.

## Sample Input

```python
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
```

## Sample Output

```python
3
```

<details>
  <summary>Hint 1</summary>

The Binary Search algorithm works by finding the number in the middle of the input array and comparing it to the target number. Given that the array is sorted, if this middle number is smaller than the target number, then the entire left part of the array is no longer worth exploring since the target number can no longer be in it; similarly, if the middle number is greater than the target number, then the entire right part of the array is no longer worth exploring. Applying this logic recursively eliminates half of the array until the number is found or until the array runs out of numbers.

</details>

<details>
  <summary>Hint 2</summary>

Write a helper function that takes in two additional arguments: a left pointer and a right pointer representing the indices at the extremities of the array (or subarray) that you are applying Binary Search on. The first time this helper function is called, the left pointer should be zero and the right pointer should be the final index of the input array. To find the index of the middle number mentioned in Hint #1, simply round down the number obtained from: (left + right) / 2. Apply this logic recursively until you find the target number or until the left pointer becomes greater than the right pointer.

</details>

<details>
  <summary>Hint 3</summary>

Can you implement this algorithm iteratively? Are there any advantages to doing so?

</details>

<details>
  <summary>Optimal Space & Time Complexity</summary>

O(log(n)) time | O(1) space - where n is the length of the input array

</details>

---

## 🔗 Solution

<div style="text-align: center; flex-box: flex">
  <a href="./solution.py" style="display: inline-block; background-color: #4CAF50; color: white; padding: 10px 15px; text-align: center; text-decoration: none; border-radius: 5px;">View Solution</a>
</div>
