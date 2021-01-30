### Problem 330

This problem was asked by Dropbox.

A Boolean formula can be said to be satisfiable if there is a way to assign truth values to each variable such that the entire formula evaluates to true.

For example, suppose we have the following formula, where the symbol `¬` is used to denote negation:

```
(¬c OR b) AND (b OR c) AND (¬b OR c) AND (¬c OR ¬a)
```

One way to satisfy this formula would be to let `a = False`, `b = True`, and `c = True`.

This type of formula, with AND statements joining tuples containing exactly one OR, is known as 2-CNF.

Given a 2-CNF formula, find a way to assign truth values to satisfy it, or return `False` if this is impossible.


---

### Problem 331

This problem was asked by LinkedIn.

You are given a string consisting of the letters `x` and `y`, such as `xyxxxyxyy`. In addition, you have an operation called flip, which changes a single `x` to `y` or vice versa.

Determine how many times you would need to apply this operation to ensure that all `x`'s come before all `y`'s. In the preceding example, it suffices to flip the second and sixth characters, so you should return `2`.


---

### Problem 332

This problem was asked by Jane Street.

Given integers `M` and `N`, write a program that counts how many positive integer pairs `(a, b)` satisfy the following conditions:

```
a + b = M
a XOR b = N
```


---

### Problem 333

This problem was asked by Pinterest.

At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity"). To help figure out who this is, you have access to an `O(1)` method called `knows(a, b)`, which returns `True` if person `a` knows person `b`, else `False`.

Given a list of `N` people and the above operation, find a way to identify the celebrity in `O(N)` time.


---

### Problem 334

This problem was asked by Twitter.

The `24` game is played as follows. You are given a list of four integers, each between `1` and `9`, in a fixed order. By placing the operators `+`, `-`, `*`, and `/` between the numbers, and grouping them with parentheses, determine whether it is possible to reach the value `24`.

For example, given the input `[5, 2, 7, 8]`, you should return True, since `(5 * 2 - 7) * 8 = 24`.

Write a function that plays the `24` game.


---

### Problem 335

This problem was asked by Google.

PageRank is an algorithm used by Google to rank the importance of different websites. While there have been changes over the years, the central idea is to assign each site a score based on the importance of other pages that link to that page.

More mathematically, suppose there are `N` sites, and each site `i` has a certain count `Ci` of outgoing links. Then the score for a particular site `Sj` is defined as :

```
score(Sj) = (1 - d) / N + d * (score(Sx) / Cx+ score(Sy) / Cy+ ... + score(Sz) / Cz))
```

Here, `Sx, Sy, ..., Sz` denote the scores of all the other sites that have outgoing links to `Sj`, and `d` is a damping factor, usually set to around `0.85`, used to model the probability that a user will stop searching.

Given a directed graph of links between various websites, write a program that calculates each site's page rank.


---

### Problem 336

This problem was asked by Microsoft.

Write a program to determine how many distinct ways there are to create a max heap from a list of `N` given integers.

For example, if `N = 3`, and our integers are `[1, 2, 3]`, there are two ways, shown below.

```
  3      3
 / \    / \
1   2  2   1
```


---

### Problem 337

This problem was asked by Apple.

Given a linked list, uniformly shuffle the nodes. What if we want to prioritize space over time?


---

### Problem 338

This problem was asked by Facebook.

Given an integer `n`, find the next biggest integer with the same number of `1`-bits on. For example, given the number `6` (`0110` in binary), return `9` (`1001`).


---

### Problem 339

This problem was asked by Microsoft.

Given an array of numbers and a number `k`, determine if there are three entries in the array which add up to the specified number `k`. For example, given `[20, 303, 3, 4, 25]` and `k = 49`, return true as `20 + 4 + 25 = 49`.


---

