# Nth Fibonacci

The Fibonacci sequence is defined as follows: the first number of the sequence
is <code>0</code>, the second number is <code>1</code>, and the nth number is the sum of the (n - 1)th
and (n - 2)th numbers. Write a function that takes in an integer
<code>n</code> and returns the nth Fibonacci number.

Important note: the Fibonacci sequence is often defined with its first two
numbers as <code>F0 = 0</code> and <code>F1 = 1</code>. For the purpose of
this question, the first Fibonacci number is <code>F0</code>; therefore,
<code>getNthFib(1)</code> is equal to <code>F0</code>, <code>getNthFib(2)</code>
is equal to <code>F1</code>, etc..

## Sample Input #1

```python
n = 2
```

## Sample Output #1

```python
20
```

## Sample Input #2

```python
n = 6
```

## Sample Output #2

```javascript
5 // 0, 1, 1, 2, 3, 5
```

<details>
  <summary>Hint 1</summary>

The formula to generate the nth Fibonacci number can be written as follows: F(n) = F(n - 1) + F(n - 2). Think of the case(s) for which this formula doesn't apply (the base case(s)) and try to implement a simple recursive algorithm to find the nth Fibonacci number with this formula.

</details>

<details>
  <summary>Hint 2</summary>

What are the runtime implications of solving this problem as is described in Hint #1? Can you use memoization (caching) to improve the performance of your algorithm?

</details>

<details>
  <summary>Hint 3</summary>

Realize that to calculate any single Fibonacci number you only need to have the two previous Fibonacci numbers. Knowing this, can you implement an iterative algorithm to solve this question, storing only the last two Fibonacci numbers at any given time?

</details>

<details>
  <summary>Optimal Space & Time Complexity</summary>

O(n) time | O(1) space - where n is the input number

</details>

---

## 🔗 Solutions

<div style="text-align: center;">
  <a href="./solution.py" style="display: inline-block; background-color: #4CAF50; color: white; padding: 10px 15px; text-align: center; text-decoration: none; border-radius: 5px; margin-right: 10px;">View Solution</a>
</div>
