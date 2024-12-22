# Shift Linked List

Write a function that takes in the head of a Singly Linked List and an integer
<code>k</code>, shifts the list in place (i.e., doesn't create a brand new
list) by k positions, and returns its new head.

Shifting a Linked List means moving its nodes forward or backward and wrapping
them around the list where appropriate. For example, shifting a Linked List
forward by one position would make its tail become the new head of the linked
list.

Whether nodes are moved forward or backward is determined by whether
<code>k</code> is positive or negative.

Each <code>LinkedList</code> node has an integer <code>value</code> as well as
a <code>next</code> node pointing to the next node in the list or to
<code>None</code> / <code>null</code> if it's the tail of the list.

Each <code>LinkedList</code> node has an integer <code>value</code> as well as
a <code>next</code> node pointing to the next node in the list or to
<code>None</code> / <code>null</code> if it's the tail of the list.

## Sample Input

```javascript
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 // the head node with value 0
k = 2
```

## Sample Output

```javascript
4 -> 5 -> 0 -> 1 -> 2 -> 3 // the new head node with value 4
```

<details>
  <summary>Hint 1</summary>

Putting aside the cases where k is a negative integer, where k is 0, or where k is larger than the length of the linked list, what does shifting the linked list by k positions entail exactly?

</details>

<details>
  <summary>Hint 2</summary>

Putting aside the cases mentioned in Hint #1, shifting the linked list by k positions means moving the last k nodes in the linked list to the front of the linked list. What nodes in the linked list will you actually need to mutate?

</details>

<details>
  <summary>Hint 3</summary>

There are four nodes that really matter in this entire process: the original tail of the linked list, which will point to the original head of the linked list, the original head of the linked list, which will be pointed to by the original tail of the linked list, the new tail of the linked list, and the new head of the linked list. Note that the new head is the node that the new tail points to in the original, unshifted linked list.

</details>

<details>
  <summary>Hint 4</summary>

You can find the original tail of the linked list by simply traversing the linked list, starting at the original head of the linked list that you're given. You can find the new tail of the linked list by moving k positions from the original tail if k is positive (which means moving to the (lengthOfList - k)th position in the list, and you can easily count the length of the list as you traverse it to find its original tail). You can access the new head of the linked list once you've found its new tail, since it's the new tail's original next node. How will you handle the trickier values of k?

</details>

<details>
  <summary>Optimal Space & Time Complexity</summary>

O(n) time | O(1) space - where n is the number of nodes in the Linked List

</details>

---

## 🔗 Solution

<div style="text-align: center; flex-box: flex">
  <a href="./solution.py" style="display: inline-block; background-color: #4CAF50; color: white; padding: 10px 15px; text-align: center; text-decoration: none; border-radius: 5px;">View Solution</a>
</div>
