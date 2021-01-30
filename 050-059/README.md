#### Problem 50

This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

```
    *
   / \
  +    +
 / \  / \
3  2  4  5
```

You should return 45, as it is (3 + 2) * (4 + 5).


---

#### Problem 51

This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.


---

#### Problem 52

This problem was asked by Google.

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.


---

#### Problem 53

This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.


---

#### Problem 54

This problem was asked by Dropbox.

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.


---

#### Problem 55

This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

* shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
* restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?


---

#### Problem 56

This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.


---

#### Problem 57

This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple texts such that each text has a length of k or less. You must break it up so that words don't break across lines. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.


---

#### Problem 58

This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.


---

#### Problem 59

This problem was asked by Google.

Implement a file syncing algorithm for two computers over a low-bandwidth network. What if we know the files in the two computers are mostly the same?


---

