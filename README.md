# Introduction

The smart-match module contains functions for functions for calculating string similarity.

## Concept

1. $similarity$
A value in a range of [0, 1], which represents how similar the two strings are. 
The larger the value, the more similar the two strings are.

2. $dissimilarity$
A value in a range of [0, 1], which represents how dissimilar the two strings are. 
The larger the value, the more dissimilar the two strings are.
For a pair of strings, $similarity = 1 - dissimilarity$

3. $distance$
How far the two strings are. Notice that not all the methods support distance method.

## Methods

Abbreviation | Full name | similarity | dissimilarity | distance
-------------|-----------|------------|---------------|---------
ED(Default) | Levenshtein |     Yes   |    Yes        |  Yes
DL  | Damerau Levenshtein |     Yes   |    Yes        |  Yes
BD  |    Block Distance   |     Yes   |    Yes        |  Yes
cos  | Cosine Similarity |     Yes   |    Yes        |  No
dice | Dice Similarity |     Yes   |    Yes        |  No


# Installation

```shell
pip install smart-match
```

# Usage

- Default method ED(Levenshtein): It also called edit distance, which is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other

```python
import smart_match
print(smart_match.similarity('hello', 'hero'))
print(smart_match.dissimilarity('hello', 'hero'))
print(smart_match.distance('hello', 'hero'))
```
Output:
```shell
0.6
0.4
2
```

- change to the other methods:

__DL(Damerau Levenshtein)__: It consider the cost of transposition of two adjacent characters to be 1. 

```python
smart_match.use('DL')
print(smart_match.distance('hello', 'ehllo'))
```
Output:
```shell
1
```

__BD(Block Distance)__: It focuses on the differences in the alphabet without considering the order.

```python
smart_match.use('BD')
print(smart_match.distance('hello', 'ehllo'))
```
Output:
```shell
0
```

__cos(Cosine Similarity)__:  It measures the cosine of the angle between two strings projected in a multi-dimensional space.
Mathematically $$cos(X, Y) = \frac{X \cdot Y}{\|X\| \|Y\|}$$

```python
smart_match.use('cos')
print(smart_match.similarity('hello', 'hero'))
```
Output:
```shell
0.5669467095138409
```

__dice(Dice Similarity)__:  It is intended to be applied to discrete data, so the frequencies of characters will be ignored. 
Mathematically $$dice(X, Y) = \frac{2|X \cap Y|}{|X|+|Y|}$$

```python
smart_match.use('dice')
print(smart_match.similarity('hello', 'hero'))
```
Output:
```shell
0.75
```

# License

smart-match is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

See the file COPYING for the full text of GNU General Public License version 2.
