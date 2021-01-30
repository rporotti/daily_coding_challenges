### Problem 340

This problem was asked by Google.

Given a set of points `(x, y)` on a 2D cartesian plane, find the two closest points. For example, given the points `[(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]`, return `[(-1, -1), (1, 1)]`.


---

### Problem 341

This problem was asked by Google.

You are given an N by N matrix of random letters and a dictionary of words. Find the maximum number of words that can be packed on the board from the given dictionary.

A word is considered to be able to be packed on the board if:
- It can be found in the dictionary
- It can be constructed from untaken letters by other words found so far on the board
- The letters are adjacent to each other (vertically and horizontally, not diagonally).
- Each tile can be visited only once by any word.

For example, given the following dictionary:
```
{ 'eat', 'rain', 'in', 'rat' }
```

and matrix:
```
[['e', 'a', 'n'],
 ['t', 't', 'i'],
 ['a', 'r', 'a']]
```

Your function should return 3, since we can make the words 'eat', 'in', and 'rat' without them touching each other. We could have alternatively made 'eat' and 'rain', but that would be incorrect since that's only 2 words.


---

### Problem 342

This problem was asked by Stripe.

`reduce` (also known as `fold`) is a function that takes in an array, a combining function, and an initial value and builds up a result by calling the combining function on each element of the array, left to right. For example, we can write `sum()` in terms of reduce:

```python
def add(a, b):
    return a + b
```

```python
def sum(lst):
    return reduce(lst, add, 0)
```

This should call add on the initial value with the first element of the array, and then the result of that with the second element of the array, and so on until we reach the end, when we return the sum of the array.

Implement your own version of reduce.


---

### Problem 343

This problem was asked by Google.

Given a binary search tree and a range `[a, b]` (inclusive), return the sum of the elements of the binary search tree within the range.

For example, given the following tree:
```
    5
   / \
  3   8
 / \ / \
2  4 6  10
```

and the range `[4, 9]`, return `23 (5 + 4 + 6 + 8)`.


---

### Problem 344

This problem was asked by Adobe.

You are given a tree with an even number of nodes. Consider each connection between a parent and child node to be an "edge". You would like to remove some of these edges, such that the disconnected subtrees that remain each have an even number of nodes.

For example, suppose your input was the following tree:
```
   1
  / \ 
 2   3
    / \ 
   4   5
 / | \
6  7  8
```

In this case, removing the edge `(3, 4)` satisfies our requirement.

Write a function that returns the maximum number of edges you can remove while still satisfying this requirement.


---

### Problem 345

This problem was asked by Google.

You are given a set of synonyms, such as `(big, large)` and `(eat, consume)`. Using this set, determine if two sentences with the same number of words are equivalent.

For example, the following two sentences are equivalent:
- "He wants to eat food."
- "He wants to consume food."

Note that the synonyms `(a, b)` and `(a, c)` do not necessarily imply `(b, c)`: consider the case of `(coach, bus)` and `(coach, teacher)`.

Follow-up: what if we can assume that `(a, b)` and `(a, c)` do in fact imply `(b, c)`?


---

### Problem 346

This problem was asked by Airbnb.

You are given a huge list of airline ticket prices between different cities around the world on a given day. These are all direct flights. Each element in the list has the format `(source_city, destination, price)`.

Consider a user who is willing to take up to `k` connections from their origin city `A` to their destination `B`. Find the cheapest fare possible for this journey and print the itinerary for that journey.

For example, our traveler wants to go from JFK to LAX with up to 3 connections, and our input flights are as follows:

```
[
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]
```

Due to some improbably low flight prices, the cheapest itinerary would be JFK -> ATL -> ORD -> LAX, costing $440.


---

### Problem 347

This problem was asked by Yahoo.

You are given a string of length `N` and a parameter `k`. The string can be manipulated by taking one of the first `k` letters and moving it to the end.

Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.

For example, suppose we are given the string `daily` and `k = 1`. The best we can create in this case is `ailyd`.


---

### Problem 348

This problem was asked by Zillow.

A ternary search tree is a trie-like data structure where each node may have up to three children. Here is an example which represents the words `code`, `cob`, `be`, `ax`, `war`, and `we`.
```
       c
    /  |  \
   b   o   w
 / |   |   |
a  e   d   a
|    / |   | \ 
x   b  e   r  e
```

The tree is structured according to the following rules:
- left child nodes link to words lexicographically earlier than the parent prefix
- right child nodes link to words lexicographically later than the parent prefix
- middle child nodes continue the current word

For instance, since code is the first word inserted in the tree, and `cob` lexicographically precedes `cod`, `cob` is represented as a left child extending from `cod`.

Implement insertion and search functions for a ternary search tree.


---

### Problem 349

This problem was asked by Grammarly.

Soundex is an algorithm used to categorize phonetically, such that two names that sound alike but are spelled differently have the same representation.

Soundex maps every name to a string consisting of one letter and three numbers, like `M460`.

One version of the algorithm is as follows:
- Remove consecutive consonants with the same sound (for example, change `ck -> c`).
- Keep the first letter. The remaining steps only apply to the rest of the string.
- Remove all vowels, including `y`, `w`, and `h`.
- Replace all consonants with the following digits:
    ```
    b, f, p, v -> 1
    c, g, j, k, q, s, x, z -> 2
    d, t -> 3
    l -> 4
    m, n -> 5
    r -> 6
    ```

If you don't have three numbers yet, append zeros until you do. Keep the first three numbers.
Using this scheme, `Jackson` and `Jaxen` both map to `J250`.

Implement Soundex.


---

