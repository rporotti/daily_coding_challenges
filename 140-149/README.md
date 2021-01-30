#### Problem 140

This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array `[2, 4, 6, 8, 10, 2, 6, 10]`, return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?


---

#### Problem 141

This problem was asked by Microsoft.

Implement 3 stacks using a single list:

```
class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass
```


---

#### Problem 142

This problem was asked by Google.

You're given a string consisting solely of `(`, `)`, and `*`. 
`*` can represent either a `(`, `)`, or an empty string. Determine whether the parentheses are balanced.

For example, `(()*` and `(*)` are balanced. `)*(` is not balanced.


---

#### Problem 143

This problem was asked by Amazon.

Given a pivot `x`, and a list `lst`, partition the list into three parts.
* The first part contains all elements in `lst` that are less than `x`
* The second part contains all elements in `lst` that are equal to `x`
* The third part contains all elements in `lst` that are larger than `x`
Ordering within a part can be arbitrary.

For example, given `x = 10` and `lst = [9, 12, 3, 5, 14, 10, 10]`, one partition may be `[9, 3, 5, 10, 10, 12, 14]`


---

#### Problem 144

This problem was asked by Google.

Given an array of numbers and an index `i`, return the index of the nearest larger number of the number at index `i`, where distance is measured in array indices.

For example, given `[4, 1, 3, 5, 6]` and index `0`, you should return `3`.

If two distances to larger numbers are equal, then return any one of them. If the array at `i` doesn't have a nearest larger integer, then return `null`.

Follow-up: If you can preprocess the array, can you do this in constant time?


---

#### Problem 145

This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given `1 -> 2 -> 3 -> 4`, return `2 -> 1 -> 4 -> 3`.


---

#### Problem 146

This question was asked by BufferBox.

Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:
```
   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
```

should be pruned to:
```
   0
  / \
 1   0
    /
   1
```

We do not remove the tree at the root or its left child because it still has a 1 as a descendant.


---

#### Problem 147

Given a list, sort it using this method: `reverse(lst, i, j)`, which sorts `lst` from `i` to `j`.


---

#### Problem 148

This problem was asked by Apple.

Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around. Gray code is common in hardware so that we don't see temporary spurious values during transitions.

Given a number of bits `n`, generate a possible gray code for it.

For example, for `n = 2`, one gray code would be `[00, 01, 11, 10]`.


---

#### Problem 149

This problem was asked by Goldman Sachs.

Given a list of numbers `L`, implement a method `sum(i, j)` which returns the sum from the sublist `L[i:j]` (including i, excluding j).

For example, given `L = [1, 2, 3, 4, 5]`, `sum(1, 3)` should return `sum([2, 3])`, which is `5`.

You can assume that you can do some pre-processing. `sum()` should be optimized over the pre-processing step.


---

