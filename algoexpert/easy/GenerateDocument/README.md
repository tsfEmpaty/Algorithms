# Generate Document

You're given a string of available characters and a string representing a
document that you need to generate. Write a function that determines if you
can generate the document using the available characters. If you can generate
the document, your function should return <code>true</code>; otherwise, it
should return <code>false</code>.

You're only able to generate the document if the frequency of unique
characters in the characters string is greater than or equal to the frequency
of unique characters in the document string. For example, if you're given
<code>characters = "abcabc"</code> and <code>document = "aabbccc"</code> you
<b>cannot</b> generate the document because you're missing one <code>c</code>.

The document that you need to create may contain any characters, including
special characters, capital letters, numbers, and spaces.

Note: you can always generate the empty string (<code>""</code>).

## Sample Input

```python
characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
```

## Sample Output

```python
True
```

<details>
  <summary>Hint 1</summary>

There are multiple ways to the solve this problem, but not all approaches have
an optimal time complexity. Is there any way to solve this problem in better
than <code>O(m _ (n + m))</code> or <code>O(n _ (n + m))</code> time, where
<code>n</code> is the length of the <code>characters</code> string and
<code>m</code> is the length of the <code>document</code> string?

</details>

<details>
  <summary>Hint 2</summary>

One of the simplest ways to solve this problem is to loop through the
<code>document</code> string, one character at a time. At every character, you
can count how many times it occurs in the <code>document</code> string and in
the <code>characters</code> string. If it occurs more times in the
<code>document</code> string than in the <code>characters</code> string, then
you cannot generate the document. What is the time complexity of this
approach?

</details>

<details>
  <summary>Hint 3</summary>

The approach discussed in Hint #2 runs in <code>O(m \* (n + m))</code> time.
Can you use some external space to optimize this time complexity?

</details>

<details>
  <summary>Hint 4</summary>

You can solve this problem in <code>O(n + m)</code> time. To do so, you need
to use a hash table. Start by counting all of the characters in the
<code>characters</code> string and storing these counts in a hash table. Then,
loop through the <code>document</code> string, and check if each character is
in the hash table and has a value greater than zero. If a character isn't in
the hash table or doesn't have a value greater than zero, then you cannot
generate the document. If a character is in the hash table and has a value
greater than zero, then decrement its value in the hash table to indicate that
you've "used" one of these available characters. If you make it through the
entire <code>document</code> string without returning <code>false</code>, then
you can generate the document.

</details>

<details>
  <summary>Optimal Space & Time Complexity</summary>

O(n + m) time | O(c) space - where n is the number of characters, m is the length of the document, and c is the number of unique characters in the characters string

</details>

---

## 🔗 Solutions

<div style="text-align: center;">
  <a href="./solution.py" style="display: inline-block; background-color: #4CAF50; color: white; padding: 10px 15px; text-align: center; text-decoration: none; border-radius: 5px; margin-right: 10px;">View Solution</a>
</div>
