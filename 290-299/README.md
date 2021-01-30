### Problem 290

This problem was asked by Facebook.

On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

For example, given the input `['R', 'G', 'B', 'G', 'B']`, it is possible to end up with a single Qux through the following steps:

```
        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |
```


---

### Problem 291

This problem was asked by Glassdoor.

An imminent hurricane threatens the coastal town of Codeville. If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is `k`, determine how many boats will be needed to save everyone.

For example, given a population with weights `[100, 200, 150, 80]` and a boat limit of `200`, the smallest number of boats required will be three.


---

### Problem 292

This problem was asked by Twitter.

A teacher must divide a class of students into two teams to play dodgeball. Unfortunately, not all the kids get along, and several refuse to be put on the same team as that of their enemies.

Given an adjacency list of students and their enemies, write an algorithm that finds a satisfactory pair of teams, or returns `False` if none exists.

For example, given the following enemy graph you should return the teams `{0, 1, 4, 5}` and `{2, 3}`.
```
students = {
    0: [3],
    1: [2],
    2: [1, 4],
    3: [0, 4, 5],
    4: [2, 3],
    5: [3]
}
```

On the other hand, given the input below, you should return `False`.
```
students = {
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
}
```


---

### Problem 293

This problem was asked by Uber.

You have N stones in a row, and would like to create from them a pyramid. This pyramid should be constructed such that the height of each stone increases by one until reaching the tallest stone, after which the heights decrease by one. In addition, the start and end stones of the pyramid should each be one stone high.

You can change the height of any stone by paying a cost of `1` unit to lower its height by `1`, as many times as necessary. Given this information, determine the lowest cost method to produce this pyramid.

For example, given the stones `[1, 1, 3, 3, 2, 1]`, the optimal solution is to pay 2 to create `[0, 1, 2, 3, 2, 1]`.


---

### Problem 294

This problem was asked by Square.

A competitive runner would like to create a route that starts and ends at his house, with the condition that the route goes entirely uphill at first, and then entirely downhill.

Given a dictionary of places of the form `{location: elevation}`, and a dictionary mapping paths between some of these locations to their corresponding distances, find the length of the shortest route satisfying the condition above. Assume the runner's home is location `0`.

For example, suppose you are given the following input:
```
elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}
```

In this case, the shortest valid path would be `0 -> 2 -> 4 -> 0`, with a distance of `28`.


---

### Problem 295

This problem was asked by Stitch Fix.

Pascal's triangle is a triangular array of integers constructed with the following formula:

The first row consists of the number 1.
For each subsequent row, each element is the sum of the numbers directly above it, on either side.
For example, here are the first few rows:
```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

Given an input `k`, return the `k`th row of Pascal's triangle.

Bonus: Can you do this using only `O(k)` space?


---

### Problem 296

This problem was asked by Etsy.

Given a sorted array, convert it into a height-balanced binary search tree.


---

### Problem 297

This problem was asked by Amazon.

At a popular bar, each customer has a set of favorite drinks, and will happily accept any drink among this set. For example, in the following situation, customer 0 will be satisfied with drinks `0`, `1`, `3`, or `6`.

```
preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
```

A lazy bartender working at this bar is trying to reduce his effort by limiting the drink recipes he must memorize. Given a dictionary input such as the one above, return the fewest number of drinks he must learn in order to satisfy all customers.

For the input above, the answer would be `2`, as drinks `1` and `5` will satisfy everyone.


---

### Problem 298

This problem was asked by Google.

A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion of her path that consists of just two types of apple trees.

For example, given the input `[2, 1, 2, 3, 3, 1, 3, 5]`, the longest portion will involve types `1` and `3`, with a length of four.


---

### Problem 299

This problem was asked by Samsung.

A group of houses is connected to the main water plant by means of a set of pipes. A house can either be connected by a set of pipes extending directly to the plant, or indirectly by a pipe to a nearby house which is otherwise connected.

For example, here is a possible configuration, where A, B, and C are houses, and arrows represent pipes:
`A <--> B <--> C <--> plant`

Each pipe has an associated cost, which the utility company would like to minimize. Given an undirected graph of pipe connections, return the lowest cost configuration of pipes such that each house has access to water.

In the following setup, for example, we can remove all but the pipes from plant to A, plant to B, and B to C, for a total cost of 16.

```python
pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}
```


---

