#### Problem 230

This problem was asked by Goldman Sachs.

You are given `N` identical eggs and access to a building with `k` floors. Your task is to find the lowest floor that will cause an egg to break, if dropped from that floor. Once an egg breaks, it cannot be dropped again. If an egg breaks when dropped from the `x`th floor, you can assume it will also break when dropped from any floor greater than `x`.

Write an algorithm that finds the minimum number of trial drops it will take, in the worst case, to identify this floor.

For example, if `N = 1` and `k = 5`, we will need to try dropping the egg at every floor, beginning with the first, until we reach the fifth floor, so our solution will be `5`.


---

#### Problem 231

This problem was asked by IBM.

Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same. If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.


---

#### Problem 232

This problem was asked by Google.

Implement a PrefixMapSum class with the following methods:

`insert(key: str, value: int)`: Set a given key's value in the map. If the key already exists, overwrite the value.
`sum(prefix: str)`: Return the sum of all values of keys that begin with a given prefix.
For example, you should be able to run the following code:

```
mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3
```

```
mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
```


---

#### Problem 233

This problem was asked by Apple.

Implement the function `fib(n)`, which returns the nth number in the Fibonacci sequence, using only `O(1)` space.


---

#### Problem 234

This problem was asked by Microsoft.

Recall that the minimum spanning tree is the subset of edges of a tree that connect all its vertices with the smallest possible total edge weight. Given an undirected graph with weighted edges, compute the maximum weight spanning tree.


---

#### Problem 235

This problem was asked by Facebook.

Given an array of numbers of length `N`, find both the minimum and maximum using less than `2 * (N - 2)` comparisons.


---

#### Problem 236

This problem was asked by Nvidia.

You are given a list of N points `(x1, y1), (x2, y2), ..., (xN, yN)` representing a polygon. You can assume these points are given in order; that is, you can construct the polygon by connecting point 1 to point 2, point 2 to point 3, and so on, finally looping around to connect point N to point 1.

Determine if a new point p lies inside this polygon. (If p is on the boundary of the polygon, you should return False).


---

#### Problem 237

This problem was asked by Amazon.

A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node. The following tree is an example:

```
        4
      / | \
    3   5   3
  /           \
9              9
```

Given a k-ary tree, determine whether it is symmetric.


---

#### Problem 238

This problem was asked by MIT.

Blackjack is a two player card game whose rules are as follows:
* The player and then the dealer are each given two cards.
* The player can then "hit", or ask for arbitrarily many additional cards, so long as their total does not exceed 21.
* The dealer must then hit if their total is 16 or lower, otherwise pass.
* Finally, the two compare totals, and the one with the greatest sum not exceeding 21 is the winner.

For this problem, cards values are counted as follows: each card between 2 and 10 counts as their face value, face cards count as 10, and aces count as 1.

Given perfect knowledge of the sequence of cards in the deck, implement a blackjack solver that maximizes the player's score (that is, wins minus losses).


---

#### Problem 239

This problem was asked by Uber.

One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.

For a pattern to be valid, it must satisfy the following:

All of its keys must be distinct.
It must not connect two keys by jumping over a third key, unless that key has already been used.
For example, `4 - 2 - 1 - 7` is a valid pattern, whereas `2 - 1 - 7` is not.

Find the total number of valid unlock patterns of length N, where `1 <= N <= 9`.


---

