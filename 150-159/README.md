#### Problem 150

This problem was asked by LinkedIn.

Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

For example, given the list of points `[(0, 0), (5, 4), (3, 1)]`, the central point `(1, 2)`, and `k = 2`, return `[(0, 0), (3, 1)]`.


---

#### Problem 151

Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of `(2, 2)`, and `'G'` for green:
```
B B W
W W W
W W W
B B B
```

Becomes
```
B B G
G G G
G G G
B B B
```


---

#### Problem 152

This problem was asked by Triplebyte.

You are given `n` numbers as well as `n` probabilities that sum up to `1`. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers `[1, 2, 3, 4]` and probabilities `[0.1, 0.5, 0.2, 0.2]`, your function should return `1` `10%` of the time, `2` `50%` of the time, and `3` and `4` `20%` of the time.

You can generate random numbers between 0 and 1 uniformly.


---

#### Problem 153

Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world", return 1 because there's only one word "cat" in between the two words.


---

#### Problem 154

This problem was asked by Amazon.

Implement a stack API using only a heap. A stack implements the following methods:
* `push(item)`, which adds an element to the stack
* `pop()`, which removes and returns the most recently added element (or throws an error if there is nothing on the stack)

Recall that a heap has the following operations:
* `push(item)`, which adds a new key to the heap
* `pop()`, which removes and returns the max value of the heap


---

#### Problem 155

Given a list of elements, find the majority element, which appears more than half the times `(> floor(len(lst) / 2.0))`.

You can assume that such an element exists.

For example, given `[1, 2, 1, 1, 3, 4, 0]`, return `1`.


---

#### Problem 156

This problem was asked by Facebook.

Given a positive integer `n`, find the smallest number of squared integers which sum to `n`.

For example, given n = `13`, return `2` since `13 = 3^2 + 2^2 = 9 + 4`.

Given `n = 27`, return `3` since `27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9`.


---

#### Problem 157

This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, `carrace` should return `true`, since it can be rearranged to form `racecar`, which is a palindrome. `daily` should return `false`, since there's no rearrangement that can form a palindrome.


---

#### Problem 158

This problem was asked by Slack.

You are given an `N * M` matrix of `0`s and `1`s. Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down. `0` represents an empty space while `1` represents a wall you cannot walk through.

For example, given the following matrix:

```
[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
```
Return `2`, as there are only two ways to get to the bottom right:
* `Right, down, down, right`
* `Down, right, down, right`

The top left corner and bottom right corner will always be `0`.


---

#### Problem 159

This problem was asked by Google.

Given a string, return the first recurring character in it, or `null` if there is no recurring chracter.

For example, given the string `"acbbac"`, return `"b"`. Given the string `"abcdef"`, return `null`.


---

