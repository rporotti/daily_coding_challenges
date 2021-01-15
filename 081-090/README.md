
#### Problem 81

This problem was asked by Yelp.

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if `{'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], }` then `"23"` should return `['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']`.


---

#### Problem 82

This problem was asked Microsoft.

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content "Hello world", three read7() returns "Hello w", "orld" and then "".


---

#### Problem 83

This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:
```
    a
   / \
  b   c
 / \  /
d   e f
```

should become:
```
  a
 / \
 c  b
 \  / \
  f e  d
```


---

#### Problem 84

This problem was asked by Amazon.

Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring and their perimeter is surrounded by water.

For example, this matrix has 4 islands.

```
1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
```



---

#### Problem 85

This problem was asked by Facebook.

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.



---

#### Problem 86

This problem was asked by Google.

Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.


---

#### Problem 87

This problem was asked by Uber.

A rule looks like this:

`A NE B`

This means this means point A is located northeast of point B.

`A SW C`

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:
```
A N B
B NE C
C N A
```
does not validate, since A cannot be both north and south of C.

```
A NW B
A N B
```

is considered valid.


---

#### Problem 88

This question was asked by ContextLogic.

Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.


---

#### Problem 89

This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.


---

#### Problem 90

This question was asked by Google.

Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

