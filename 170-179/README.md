#### Problem 170

This problem was asked by Facebook.

Given a start word, an end word, and a dictionary of valid words, find the shortest transformation sequence from start to end such that only one letter is changed at each step of the sequence, and each transformed word exists in the dictionary. If there is no possible transformation, return null. Each word in the dictionary have the same length as start and end and is lowercase.

For example, given `start = "dog"`, `end = "cat"`, and `dictionary = {"dot", "dop", "dat", "cat"}`, return `["dog", "dot", "dat", "cat"]`.

Given `start = "dog"`, `end = "cat"`, and `dictionary = {"dot", "tod", "dat", "dar"}`, return null as there is no possible transformation from dog to cat.


---

#### Problem 171

This problem was asked by Amazon.

You are given a list of data entries that represent entries and exits of groups of people into a building. An entry looks like this:

`{"timestamp": 1526579928, "count": 3, "type": "enter"}`

This means 3 people entered the building. An exit looks like this:

`{"timestamp": 1526580382, "count": 2, "type": "exit"}`

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building. Return it as a pair of `(start, end)` timestamps. You can assume the building always starts off and ends up empty, i.e. with 0 people inside.


---

#### Problem 172

This problem was asked by Dropbox.

Given a string `s` and a list of words `words`, where each word is the same length, find all starting indices of substrings in `s` that is a concatenation of every word in `words` exactly once.

For example, given `s = "dogcatcatcodecatdog"` and `words = ["cat", "dog"]`, return `[0, 13]`, since `"dogcat"` starts at index `0` and `"catdog"` starts at index `13`.

Given `s = "barfoobazbitbyte"` and `words = ["dog", "cat"]`, return `[]` since there are no substrings composed of `"dog"` and `"cat"` in `s`.

The order of the indices does not matter.


---

#### Problem 173

This problem was asked by Stripe.

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

```
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
```

it should become:

```
{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
```

You can assume keys do not contain dots in them, i.e. no clobbering will occur.


---

#### Problem 174

This problem was asked by Microsoft.

Describe and give an example of each of the following types of polymorphism:
* Ad-hoc polymorphism
* Parametric polymorphism
* Subtype polymorphism


---

#### Problem 175

This problem was asked by Google.

You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state `a`, number of steps `5000`, and the following transition probabilities:

```
[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
```
One instance of running this Markov chain might produce `{'a': 3012, 'b': 1656, 'c': 332 }`.


---

#### Problem 176

This problem was asked by Bloomberg.

Determine whether there exists a one-to-one character mapping from one string `s1` to another `s2`.

For example, given `s1 = abc` and `s2 = bcd`, return `true` since we can map `a` to `b`, `b` to `c`, and `c` to `d`.

Given `s1 = foo` and `s2 = bar`, return `false` since the `o` cannot map to two characters.


---

#### Problem 177

This problem was asked by Airbnb.

Given a linked list and a positive integer `k`, rotate the list to the right by `k` places.

For example, given the linked list `7 -> 7 -> 3 -> 5` and `k = 2`, it should become `3 -> 5 -> 7 -> 7`.

Given the linked list `1 -> 2 -> 3 -> 4 -> 5` and `k = 3`, it should become `3 -> 4 -> 5 -> 1 -> 2`.


---

#### Problem 178

This problem was asked by Two Sigma.

Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.


---

#### Problem 179

This problem was asked by Google.

Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

For example, given the sequence `2, 4, 3, 8, 7, 5`, you should construct the following tree:

```
    5
   / \
  3   7
 / \   \
2   4   8
```


---

