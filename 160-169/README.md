#### Problem 160

This problem was asked by Uber.

Given a tree where each edge has a weight, compute the length of the longest path in the tree.

For example, given the following tree:

```
   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h
```

and the weights: `a-b: 3`, `a-c: 5`, `a-d: 8`, `d-e: 2`, `d-f: 4`, `e-g: 1`, `e-h: 1`, the longest path would be `c -> a -> d -> f`, with a length of `17`.

The path does not have to pass through the root, and each node can have any amount of children.


---

#### Problem 161

This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number `1111 0000 1111 0000 1111 0000 1111 0000`, return `0000 1111 0000 1111 0000 1111 0000 1111`.


---

#### Problem 162

This problem was asked by Square.

Given a list of words, return the shortest unique prefix of each word. For example, given the list:
* dog
* cat
* apple
* apricot
* fish

Return the list:
* d
* c
* app
* apr
* f


---

#### Problem 163

This problem was asked by Jane Street.

Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. For example: `[5, 3, '+']` should return `5 + 3 = 8`.

For example, `[15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']` should return `5`, since it is equivalent to `((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5`.

You can assume the given expression is always valid.


---

#### Problem 164

This problem was asked by Google.

You are given an array of length n + 1 whose elements belong to the set `{1, 2, ..., n}`. By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.


---

#### Problem 165

This problem was asked by Google.

Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array `[3, 4, 9, 6, 1]`, return `[1, 1, 2, 1, 0]`, since:
* There is 1 smaller element to the right of `3`
* There is 1 smaller element to the right of `4`
* There are 2 smaller elements to the right of `9`
* There is 1 smaller element to the right of `6`
* There are no smaller elements to the right of `1`


---

#### Problem 166

This problem was asked by Uber.

Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:
* `next()`: returns the next element in the array of arrays. If there are no more elements, raise an exception.
* `has_next()`: returns whether or not the iterator still has elements left.

For example, given the input `[[1, 2], [3], [], [4, 5, 6]]`, calling `next()` repeatedly should output `1, 2, 3, 4, 5, 6`.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.


---

#### Problem 167

This problem was asked by Airbnb.

Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list `["code", "edoc", "da", "d"]`, return `[(0, 1), (1, 0), (2, 3)]`.


---

#### Problem 168

This problem was asked by Facebook.

Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:
```
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```

you should return:
```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

Follow-up: What if you couldn't use any extra space?


---

#### Problem 169

This problem was asked by Google.

Given a linked list, sort it in `O(n log n)` time and constant space.

For example, the linked list `4 -> 1 -> -3 -> 99` should become `-3 -> 1 -> 4 -> 99`.


---

