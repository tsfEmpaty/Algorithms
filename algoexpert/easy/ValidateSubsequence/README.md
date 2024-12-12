# Validate Subsequence

Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent
in the array but that are in the same order as they appear in the array. For
instance, the numbers <code>[1, 3, 4]</code> form a subsequence of the array
<code>[1, 2, 3, 4]</code>, and so do the numbers <code>[2, 4]</code>. Note
that a single number in an array and the array itself are both valid
subsequences of the array.

## Sample Input

```python
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
```

## Sample Output

```plaintext
true
```

<details>
  <summary>Hint 1</summary>

You can solve this question by iterating through the main input array once.

</details>

<details>
  <summary>Hint 2</summary>

Iterate through the main array, and look for the first integer in the potential subsequence. If you find that integer, keep on iterating through the main array, but now look for the second integer in the potential subsequence. Continue this process until you either find every integer in the potential subsequence or you reach the end of the main array.

</details>

<details>
  <summary>Hint 3</summary>

To actually implement what Hint #2 describes, you'll have to declare a variable holding your position in the potential subsequence. At first, this position will be the 0th index in the sequence; as you find the sequence's integers in the main array, you'll increment the position variable until you reach the end of the sequence.

</details>

<details>
  <summary>Optimal Space & Time Complexity</summary>

O(n) time | O(1) space - where n is the length of the array

</details>

---

## 🔗 Solutions

<div style="text-align: center;">
  <a href="./solution_while_loop.py" style="display: inline-block; background-color: #4CAF50; color: white; padding: 10px 15px; text-align: center; text-decoration: none; border-radius: 5px; margin-right: 10px;">View First Solution</a>
  <a href="./solution_for_loops.py" style="display: inline-block; background-color: #008CBA; color: white; padding: 10px 15px; text-align: center; text-decoration: none; border-radius: 5px;">View Second Solution</a>
</div>
