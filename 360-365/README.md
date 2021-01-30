### Problem 360

This problem was asked by Spotify.

You have access to ranked lists of songs for various users. Each song is represented as an integer, and more preferred songs appear earlier in each list. For example, the list `[4, 1, 7]` indicates that a user likes song `4` the best, followed by songs `1` and `7`.

Given a set of these ranked lists, interleave them to create a playlist that satisfies everyone's priorities.

For example, suppose your input is `{[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]}`. In this case a satisfactory playlist could be `[2, 1, 6, 7, 3, 9, 5]`.


---

### Problem 361

This problem was asked by Facebook.

Mastermind is a two-player game in which the first player attempts to guess the secret code of the second. In this version, the code may be any six-digit number with all distinct digits.

Each turn the first player guesses some number, and the second player responds by saying how many digits in this number correctly matched their location in the secret code. For example, if the secret code were `123456`, then a guess of `175286` would score two, since `1` and `6` were correctly placed.

Write an algorithm which, given a sequence of guesses and their scores, determines whether there exists some secret code that could have produced them.

For example, for the following scores you should return `True`, since they correspond to the secret code `123456`:
`{175286: 2, 293416: 3, 654321: 0}`

However, it is impossible for any key to result in the following scores, so in this case you should return `False`:
`{123456: 4, 345678: 4, 567890: 4}`


---

### Problem 362

This problem was asked by Twitter.

A strobogrammatic number is a positive number that appears the same after being rotated `180` degrees. For example, `16891` is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.


---

### Problem 363

Write a function, add_subtract, which alternately adds and subtracts curried arguments. Here are some sample operations:

```
add_subtract(7) -> 7
add_subtract(1)(2)(3) -> 1 + 2 - 3 -> 0
add_subtract(-5)(10)(3)(9) -> -5 + 10 - 3 + 9 -> 11
```


---

### Problem 364

This problem was asked by Facebook.

Describe an algorithm to compute the longest increasing subsequence of an array of numbers in `O(n log n)` time.


---

### Problem 365

This problem was asked by Google.

A quack is a data structure combining properties of both stacks and queues. It can be viewed as a list of elements written left to right such that three operations are possible:
- `push(x)`: add a new item `x` to the left end of the list
- `pop()`: remove and return the item on the left end of the list
- `pull()`: remove the item on the right end of the list.

Implement a quack using three stacks and `O(1)` additional memory, so that the amortized time for any push, pop, or pull operation is `O(1)`.


---
