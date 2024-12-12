# Non-Constructible Change

Given an array of positive integers representing the values of coins in your
possession, write a function that returns the minimum amount of change (the
minimum sum of money) that you cannot create. The given coins can have
any positive integer value and aren't necessarily unique (i.e., you can have
multiple coins of the same value).

For example, if you're given <b>coins = [1, 2, 5]</b>, the minimum
amount of change that you can't create is <b>4</b>. If you're given no
coins, the minimum amount of change that you can't create is <b>1</b>.

## Sample Input

```python
coins = [5, 7, 1, 1, 2, 3, 22]
```

## Sample Output

```python
20
```

<details>
  <summary>Hint 1</summary>

One approach to solve this problem is to attempt to create every single amount
of change, starting at 1 and going up until you eventually can't create an
amount. While this approach works, there <i>is</i> a better one.

</details>

<details>
  <summary>Hint 2</summary>

Start by sorting the input array. Since you're trying to find the
<b>minimum</b> amount of change that you can't create, it makes sense to
consider the smallest coins first.

</details>

<details>
  <summary>Hint 3</summary>

To understand the trick to this problem, consider the following example:
<code>coins = [1, 2, 4]</code>. With this set of coins, we can create
<code>1, 2, 3, 4, 5, 6, 7</code> cents worth of change. Now, if we were to add
a coin of value <code>9</code> to this set, we <b>would not</b> be able to
create <code>8</code> cents. However, if we were to add a coin of value
<code>7</code>, we <b>would</b> be able to create <code>8</code> cents, and we
would also be able to create all values of change from <code>1</code> to
<code>15</code>. Why is this the case?

</details>

<details>
  <summary>Hint 4</summary>

Create a variable to store the amount of change that you can currently create
up to. Sort all of your coins, and loop through them in ascending order. At
every iteration, compare the current coin to the amount of change that you can
currently create up to. Here are the two scenarios that you'll encounter:

<ul>
  <li>
    The coin value is <b>greater</b> than the amount of change that you can
    currently create plus 1.
  </li>
  <li>
    The coin value is <b>smaller than or equal to</b> the amount of change that
    you can currently create plus 1.
  </li>
</ul>

In the first scenario, you simply return the current amount of change that you
can create plus 1, because you can't create that amount of change. In the
second scenario, you add the value of the coin to the amount of change that
you can currently create up to, and you continue iterating through the coins.
The reason for this is that, if you're in the second scenario, you can create
all of the values of change that you can currently create plus the value of
the coin that you just considered. If you're given coins <code>[1, 2]</code>,
then you can make <code>1, 2, 3</code> cents. So if you add a coin of value
<code>4</code>, then you can make <code>4 + 1</code> cents,
<code>4 + 2</code> cents, and <code>4 + 3</code> cents. Thus, you can make up
to <code>7</code> cents.

</details>

<details>
  <summary>Optimal Space & Time Complexity</summary>

O(nlogn) time | O(1) space - where n is the number of coins

</details>

---

## 🔗 Solutions

<div style="text-align: center;">
  <a href="./solution.py" style="display: inline-block; background-color: #4CAF50; color: white; padding: 10px 15px; text-align: center; text-decoration: none; border-radius: 5px; margin-right: 10px;">View Solution</a>
</div>
