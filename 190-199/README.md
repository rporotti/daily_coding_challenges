#### Problem 190

This problem was asked by Facebook.

Given a circular array, compute its maximum subarray sum in `O(n)` time.

For example, given `[8, -1, 3, 4]`, return `15` as we choose the numbers `3`, `4`, and `8` where the `8` is obtained from wrapping around.

Given `[-4, 5, 1, 0]`, return `6` as we choose the numbers `5` and `1`.


---

#### Problem 191

This problem was asked by Stripe.

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as `[0, 1]` and `[1, 2]`, but they won't be considered overlapping.

For example, given the intervals `(7, 9), (2, 4), (5, 8)`, return `1` as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.


---

#### Problem 192

This problem was asked by Google.

You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying to advance to the end. You can advance at most, the number of steps that you're currently on. Determine whether you can get to the end of the array.

For example, given the array `[1, 3, 1, 2, 0, 1]`, we can go from indices `0 -> 1 -> 3 -> 5`, so return `true`.

Given the array `[1, 2, 1, 0, 0]`, we can't reach the end, so return `false`.


---

#### Problem 193

This problem was asked by Affirm.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock. You're also given a number fee that represents a transaction fee for each buy and sell transaction.

You must buy before you can sell the stock, but you can make as many transactions as you like.

For example, given `[1, 3, 2, 8, 4, 10]` and `fee = 2`, you should return `9`, since you could buy the stock at `$1`, and sell at `$8`, and then buy it at `$4` and sell it at `$10`. Since we did two transactions, there is a `$4` fee, so we have `7 + 6 = 13` profit minus `$4` of fees.


---

#### Problem 194

This problem was asked by Facebook.

Suppose you are given two lists of n points, one list `p1, p2, ..., pn` on the line `y = 0` and the other list `q1, q2, ..., qn` on the line `y = 1`. Imagine a set of `n` line segments connecting each point `pi` to `qi`. Write an algorithm to determine how many pairs of the line segments intersect.


---

#### Problem 195

This problem was asked by Google.

Let `M` be an `N` by `N` matrix in which every row and every column is sorted. No two elements of `M` are equal.

Given `i1`, `j1`, `i2`, and `j2`, compute the number of elements of `M` smaller than `M[i1, j1]` and larger than `M[i2, j2]`.


---

#### Problem 196

This problem was asked by Apple.

Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.

For example, given the following tree:

```
  5
 / \
2  -5
```

Return `2` as it occurs twice: once as the left leaf, and once as the sum of `2 + 5 - 5.`


---

#### Problem 197

This problem was asked by Amazon.

Given an array and a number `k` that's smaller than the length of the array, rotate the array to the right `k` elements in-place.


---

#### Problem 198


This problem was asked by Google.

Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset `(i, j)` satisfies either `i % j = 0` or `j % i = 0`.

For example, given the set `[3, 5, 10, 20, 21]`, you should return `[5, 10, 20]`. Given `[1, 3, 6, 24]`, return `[1, 3, 6, 24]`.


---

#### Problem 199

This problem was asked by Facebook.

Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of insertions and deletions. If there are multiple solutions, return any of them.

For example, given `"(()"`, you could return `"(())"`. Given `"))()("`, you could return `"()()()()"`.


---

