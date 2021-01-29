# Introduction

The smart-match module contains functions for calculating strings/sets similarity.

## Concept

1. __similarity__:
A value in a range of [0, 1], which represents how similar the two strings are. 
The larger the value, the more similar the two strings are.

2. __dissimilarity__:
A value in a range of [0, 1], which represents how dissimilar the two strings are. 
The larger the value, the more dissimilar the two strings are.
For a pair of strings, similarity = 1 - dissimilarity

3. __distance__:
How far the two strings are. Notice that not all the methods support distance method.

4. __score__
The larger the score, the more similar the two strings are. Notice not all the methods have score method.

We support three levels of string matching.

1. __char__:
Similarity computation based on characters in the strings.

2. __term__:
Similarity computation based on terms in the strings.

3. __gram__:
Similarity computation based on q-grams in the strings.


## Methods

We support the following methods.

 Method | similarity | dissimilarity | distance | score
-----------|------------|---------------|----------|------
Levenshtein (default) |     ✅   |    ✅        |  ✅  | ❌
Euclidean |     ✅   |    ✅        |  ✅  | ❌
Damerau Levenshtein |     ✅   |    ✅        |  ✅  | ❌
Block Distance   |     ✅   |    ✅        |  ✅  | ❌
Cosine |   ✅   |    ✅        |  ❌ | ❌
Tanimoto Coefficient | ✅ | ✅ | ❌ | ❌
Dice |     ✅   |    ✅        |  ❌ | ❌
Simon White | ✅ | ✅ | ❌ | ❌
Longest Common Substring | ✅ | ✅ | ✅ | ✅
Longest Common SubSequence | ✅ | ✅ | ✅ | ✅
Overlap Coefficient | ✅ | ✅ | ❌ | ❌
Generalized Overlap Coefficient | ✅ | ✅ | ❌ | ❌
Jaccard     |  ✅ | ✅ | ❌ | ❌
Generalized Jaccard | ✅ | ✅ | ❌ | ❌
Hamming | ✅ | ✅ | ✅ | ❌
Jaro | ✅ | ✅ | ❌ | ❌
Jaro Winkler | ✅ | ✅ | ❌ | ❌
Needleman Wunch | ✅ | ✅ | ❌ | ✅
Smith Waterman | ✅ | ✅ | ❌ | ✅
Smith Waterman Gotoh | ✅ | ✅ | ❌ | ✅
Monge Elkan  |  ✅ | ✅ | ❌ | ❌

# Installation

```shell
pip install smart-match
```

# Usage

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

Check [Wiki](https://github.com/jiayingwang/smart-match/wiki) for more details.

# License

smart-match is a free software. See the file LICENSE for the full text.

# Authors

![qrcode_for_wechat_official_account](https://wx3.sinaimg.cn/mw1024/bdb7558bly1gjo23b3jrmj207607674r.jpg)

