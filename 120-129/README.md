#### Problem 120

This problem was asked by Microsoft.

Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances. And in every even call of getInstance(), return the first instance and in every odd call of getInstance(), return the second instance.


---

#### Problem 121

This problem was asked by Google.

Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.


---

#### Problem 122

This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at `matrix[0][0]`, and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix
```
0 3 1 1
2 0 0 4
1 5 3 1
```

The most we can collect is `0 + 2 + 1 + 5 + 3 + 1 = 12` coins.


---

#### Problem 123

This problem was asked by LinkedIn.

Given a string, return whether it represents a number. Here are the different kinds of numbers:
* "10", a positive integer
* "-10", a negative integer
* "10.1", a positive real number
* "-10.1", a negative real number
* "1e5", a number in scientific notation

And here are examples of non-numbers:
* "a"
* "x 1"
* "a -2"
* "-"


---

#### Problem 124

This problem was asked by Microsoft.

You have 100 fair coins and you flip them all at the same time. Any that come up tails you set aside. The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?

Write a function that, given $n$, returns the number of rounds you'd expect to play until one coin remains.


---

#### Problem 125

This problem was asked by Google.

Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

```
    10
   /   \
 5      15
       /  \
     11    15
```

Return the nodes 5 and 15.


---

#### Problem 126

This problem was asked by Facebook.

Write a function that rotates a list by k elements. For example, `[1, 2, 3, 4, 5, 6]` rotated by two becomes `[3, 4, 5, 6, 1, 2]`. Try solving this without creating a copy of the list. How many swap or move operations do you need?


---

#### Problem 127

This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

`1 -> 2 -> 3 -> 4 -> 5`
is the number `54321`.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

`9 -> 9`
`5 -> 2`
return `124 (99 + 25)` as:

`4 -> 2 -> 1`


---

#### Problem 128

The Tower of Hanoi is a puzzle game with three rods and n disks, each a different size.

All the disks start off on the first rod in a stack. They are ordered by size, with the largest disk on the bottom and the smallest one at the top.

The goal of this puzzle is to move all the disks from the first rod to the last rod while following these rules:
* You can only move one disk at a time.
* A move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack.
* You cannot place a larger disk on top of a smaller disk.

Write a function that prints out all the steps necessary to complete the Tower of Hanoi. You should assume that the rods are numbered, with the first rod being 1, the second (auxiliary) rod being 2, and the last (goal) rod being 3.

For example, with n = 3, we can do this in 7 moves:

* Move 1 to 3
* Move 1 to 2
* Move 3 to 2
* Move 1 to 3
* Move 2 to 1
* Move 2 to 3
* Move 1 to 3


---

#### Problem 129

Given a real number n, find the square root of n. For example, given n = 9, return 3.


---

