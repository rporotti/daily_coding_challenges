### Problem 310

This problem was asked by Pivotal.

Write an algorithm that finds the total number of set bits in all integers between `1` and `N`.


---

### Problem 311

This problem was asked by Sumo Logic.

Given an unsorted array, in which all elements are distinct, find a "peak" element in `O(log N)` time.

An element is considered a peak if it is greater than both its left and right neighbors. It is guaranteed that the first and last elements are lower than all others.


---

### Problem 312

This problem was asked by Wayfair.

You are given a `2 x N` board, and instructed to completely cover the board with the following shapes:
- Dominoes, or `2 x 1` rectangles.
- Trominoes, or L-shapes.

For example, if `N = 4`, here is one possible configuration, where A is a domino, and B and C are trominoes.

```
A B B C
A B C C
```

Given an integer N, determine in how many ways this task is possible.


---

### Problem 313

This problem was asked by Citrix.

You are given a circular lock with three wheels, each of which display the numbers `0` through `9` in order. Each of these wheels rotate clockwise and counterclockwise.

In addition, the lock has a certain number of "dead ends", meaning that if you turn the wheels to one of these combinations, the lock becomes stuck in that state and cannot be opened.

Let us consider a "move" to be a rotation of a single wheel by one digit, in either direction. Given a lock initially set to `000`, a target combination, and a list of dead ends, write a function that returns the minimum number of moves required to reach the target state, or `None` if this is impossible.


---

### Problem 314

This problem was asked by Spotify.

You are the technical director of WSPT radio, serving listeners nationwide. For simplicity's sake we can consider each listener to live along a horizontal line stretching from `0` (west) to `1000` (east).

Given a list of `N` listeners, and a list of `M` radio towers, each placed at various locations along this line, determine what the minimum broadcast range would have to be in order for each listener's home to be covered.

For example, suppose `listeners = [1, 5, 11, 20]`, and `towers = [4, 8, 15]`. In this case the minimum range would be `5`, since that would be required for the tower at position `15` to reach the listener at position `20`.


---

### Problem 315

This problem was asked by Google.

In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.

Here is an example:
```
1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2
```

Write a program to determine whether a given input is a Toeplitz matrix.


---

### Problem 316

This problem was asked by Snapchat.

You are given an array of length `N`, where each element `i` represents the number of ways we can produce `i` units of change. For example, `[1, 0, 1, 1, 2]` would indicate that there is only one way to make `0`, `2`, or `3` units, and two ways of making `4` units.

Given such an array, determine the denominations that must be in use. In the case above, for example, there must be coins with value `2`, `3`, and `4`.


---

### Problem 317

This problem was asked by Yahoo.

Write a function that returns the bitwise `AND` of all integers between `M` and `N`, inclusive.


---

### Problem 318

This problem was asked by Apple.

You are going on a road trip, and would like to create a suitable music playlist. The trip will require `N` songs, though you only have `M` songs downloaded, where `M < N`. A valid playlist should select each song at least once, and guarantee a buffer of `B` songs between repeats.

Given `N`, `M`, and `B`, determine the number of valid playlists.


---

### Problem 319

This problem was asked by Airbnb.

An 8-puzzle is a game played on a `3 x 3` board of tiles, with the ninth tile missing. The remaining tiles are labeled `1` through `8` but shuffled randomly. Tiles may slide horizontally or vertically into an empty space, but may not be removed from the board.

Design a class to represent the board, and find a series of steps to bring the board to the state `[[1, 2, 3], [4, 5, 6], [7, 8, None]]`.


---

