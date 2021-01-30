#### Problem 130

This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given `k = 2` and the array `[5, 2, 4, 0, 1]`, you should return `3`.


---

#### Problem 131

This question was asked by Snapchat.

Given the head to a singly linked list, where each node also has a 'random' pointer that points to anywhere in the linked list, deep clone the list.


---

#### Problem 132

This question was asked by Riot Games.

Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:
* `record(timestamp)`: records a hit that happened at timestamp
* `total()`: returns the total number of hits recorded
* `range(lower, upper)`: returns the number of hits that occurred between timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?


---

#### Problem 133

This problem was asked by Amazon.

Given a node in a binary tree, return the next bigger element, also known as the inorder successor.
(NOTE: I'm assuming this is a binary search tree, because otherwise, the problem makes no sense at all)

For example, the inorder successor of 22 is 30.

```
   10
  /  \
 5    30
     /  \
   22    35
```
You can assume each node has a parent pointer.


---

#### Problem 134

This problem was asked by Facebook.

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:
* `init(arr, size)`: initialize with the original large array and size.
* `set(i, val)`: updates index at i with val.
* `get(i)`: gets the value at index i.


---

#### Problem 135

This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is `[10, 5, 1, -1]`, which has sum 15.

```
  10
 /  \
5    5
 \     \
   2    1
       /
     -1
```


---

#### Problem 136

This question was asked by Google.

Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

```
[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
```

Return 4.


---

#### Problem 137

This problem was asked by Amazon.

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.
* init(size): initialize the array with size
* set(i, val): updates index at i with val where val is either 1 or 0.
* get(i): gets the value at index i.


---

#### Problem 138

This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.


---

#### Problem 139

This problem was asked by Google.

Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface, which also implements peek(). peek shows the next element that would be returned on next().

Here is the interface:

```
class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
```


---

