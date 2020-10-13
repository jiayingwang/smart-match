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

Abbreviation | Full name | similarity | dissimilarity | distance | score
-------------|-----------|------------|---------------|----------|------
LE(Default) | Levenshtein |     ✅   |    ✅        |  ✅  | ❌
ED  | EuclideanDistance   |     ✅   |    ✅        |  ✅  | ❌
DL  | Damerau Levenshtein |     ✅   |    ✅        |  ✅  | ❌
BD  |    Block Distance   |     ✅   |    ✅        |  ✅  | ❌
cos  | Cosine Similarity |     ✅   |    ✅        |  ❌ | ❌
TC | TanimotoCoefficient | ✅ | ✅ | ❌ | ❌
dice | Dice Similarity |     ✅   |    ✅        |  ❌ | ❌
simon | SimonWhite | ✅ | ✅ | ❌ | ❌
LCST | LongestCommonSubstring | ✅ | ✅ | ✅ | ✅
LCSQ | LongestCommonSubSequence | ✅ | ✅ | ✅ | ✅
OC | OverlapCoefficient | ✅ | ✅ | ❌ | ❌
GOC | GeneralizedOverlapCoefficient | ✅ | ✅ | ❌ | ❌
jac  | Jaccard     |  ✅ | ✅ | ❌ | ❌
gjac | GeneralizedJaccard | ✅ | ✅ | ❌ | ❌
HD | HammingDistance | ✅ | ✅ | ✅ | ❌
jaro | Jaro | ✅ | ✅ | ❌ | ❌
JW | JaroWinkler | ✅ | ✅ | ❌ | ❌
NW | NeedlemanWunch | ✅ | ✅ | ❌ | ✅
SW | SmithWaterman | ✅ | ✅ | ❌ | ✅
SWG | SmithWatermanGotoh | ✅ | ✅ | ❌ | ✅
MK   | MongeElkan  |  ✅ | ✅ | ❌ | ❌


# Installation

```shell
pip install smart-match
```

# Usage

- Default method LE(Levenshtein): It is also called edit distance, which is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other.

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

__ED(EuclideanDistance)__: It calculate the euclidean distance of the two stings.

```python
smart_match.use('ED')
print(smart_match.distance('hello', 'hero'))
```
Output:
```shell
0.34921514788478913
```

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
Mathematically 

<img src="https://render.githubusercontent.com/render/math?math=cos(X, Y) = \frac{X \cdot Y}{\|X\| \|Y\|}">

```python
smart_match.use('cos')
print(smart_match.similarity('hello', 'hero'))
```
Output:
```shell
0.5669467095138409
```

__TC(TanimotoCoefficient)__: Tanimoto coefficient is similar to Cosine similarity, but the occurrence of an entry will be taken into consideration.

```python
smart_match.use('TC')
print(smart_match.similarity('test', 'test string1'))
```
Output:
```shell
0.5773502691896257
```

__dice(Dice Similarity)__:  The similarity between two strings s1 and s2 is twice the number of character pairs that are common to both strings divided by the sum of the number of character pairs in the two strings. It is intended to be applied to discrete data, so the occurrence of an entry will be ignored. 
Mathematically

<img src="https://render.githubusercontent.com/render/math?math=dice(X, Y) = \frac{2|X \cap Y|}{|X|%2B|Y|}">

```python
smart_match.use('dice')
print(smart_match.similarity('hello', 'hero'))
```
Output:
```shell
0.75
```

__simon(Simon White)__:  The similarity between two strings s1 and s2 is twice the number of character pairs that are common to both strings divided by the sum of the number of character pairs in the two strings. The occurrence of an entry will be taken into consideration.

```python
smart_match.use('simon')
print(smart_match.similarity('hello', 'hollow'))
```
Output:
```shell
0.7272727272727273
```

__jac(Jaccard)__: The Jacquard coefficient  is defined as the ratio between the intersection size and the union size of two strings/sets.
Mathematically

<img src="https://render.githubusercontent.com/render/math?math=jaccard(X, Y) = \frac{|X \cap Y|}{|X| \cup |Y|}">

```python
smart_match.use('jac')
print(smart_match.similarity('hello', 'helo'))
print(smart_match.similarity('hello', 'hero'))
print(jaccard.similarity('hello world', 'hello world hello world'))
```
Output:
```shell
1
0.6
1.0
```

__gjac(GeneralizedJaccard)__: The Jacquard coefficient is defined as the ratio between the intersection size and the union size of two strings/sets. Different from Jacquard method, the occurrence of an entry is taken into account.

```python
smart_match.use('gjac')
print(smart_match.similarity('hello', 'helo'))
print(smart_match.similarity('hello', 'hero'))
print(jaccard.similarity('hello world', 'hello world hello world'))
```
Output:
```shell
0.8
0.5
0.4782608695652174
```

__OC(OverlapCoefficient)__: The Overlap coefficient is a similarity measure that measures the overlap between two finite strings/sets.
Mathematically

<img src="https://render.githubusercontent.com/render/math?math=overlap(X, Y) = \frac{|X \cap Y|}{\min(|X|, |Y|)}">

```python
smart_match.use('gjac')
print(smart_match.similarity('hello', 'hero'))
```
Output:
```shell
0.75
```

__GOC(GeneralizedOverlapCoefficient)__: The Overlap coefficient is a similarity measure that measures the overlap between two finite strings/sets. Different from OverlapCoefficient method, the occurrence of an entry is taken into account.

```python
smart_match.use('GOC')
print(smart_match.similarity('hello', 'hollow'))
```
Output:
```shell
0.8
```

__LCST(LongestCommonSubstring)__: The longest common substring is a similarity based on finding longest string that is a substring of two strings.

```python
smart_match.use('LCST')
print(smart_match.similarity('hello', 'low'))
```
Output:
```shell
0.4
```

__LCSQ(LongestCommonSubsequence)__: The longest common subsequence is a similarity based on finding longest subsequence that is a subsequence of two strings.

```python
smart_match.use('LCSQ')
print(smart_match.similarity('hello', 'hill'))
```
Output:
```shell
0.6
```

__HD(HammingDistance)__: Hamming distance is the number of different characters in the corresponding positions of two strings. The two strings must be the same length.

```python
smart_match.use('HD')
print(smart_match.similarity('12211','11111'))
```
Output:
```shell
2
```

__jaro(Jaro Similarity)__: The Jaro Similarity of two given strings is 

<img src="https://render.githubusercontent.com/render/math?math=sim(x%2C%20y)%3D%5Cbegin%7Bcases%7D%0A0%20%26%20%5Ctext%7Bif%20m%20%3D%200%7D%5C%5C%0A%5Cfrac%7B1%7D%7B3%7D(%5Cfrac%7Bm%7D%7B%7Cx%7C%7D%20%2B%20%5Cfrac%7Bm%7D%7B%7Cy%7C%7D%20%2B%20%5Cfrac%7Bm-t%7D%7Bm%7D)%20%26%20%5Ctext%7Botherwise%7D%0A%5Cend%7Bcases%7D">

in which |x| represent the length of string x, m is the number of matching characters, t is half the number of transpositions. 

```python
smart_match.use('jaro')
print(smart_match.similarity('CRATE','TRACE'))
```
Output:
```shell
0.7333333333333334
```

__JW(JaroWinkler Similarity)__: The JaroWinkler Similarity uses a prefix scale p which gives more favorable ratings to strings that match from the beginning for exact matching prefix l.
Mathematically

<img src="https://render.githubusercontent.com/render/math?math=JD(x%2C%20y)%20%3D%20jaro(x%2C%20y)%20%2B%20lp(1-jaro(x%2C%20y))">

```python
smart_match.use('JW')
print(smart_match.similarity('TRATE', 'TRACE'))
```
Output:
```shell
0.9066666666666667
```

__NW(NeedlemanWunch)__: Applies the NeedlemanWunch algorithm to calculate the similarity between two strings.

```python
smart_match.use('NW')
print(smart_match.similarity('test string1', 'test string2'))
```
Output:
```shell
0.9583333333333334
```

__SW(SmithWaterman)__: Applies the Smith-Waterman algorithm to calculate the similarity between two strings.
Mathematically

<img src="https://render.githubusercontent.com/render/math?math=%24score_%7Bi%2C%20j%7D%20%3D%20%5Cmax%20%5Cbegin%7Bcases%7D%0A0%20%5C%5C%0Ascore_%7Bi-1%2C%20j-1%7D%20%2B%20compare(s_i%2C%20t_j)%20%5C%5C%0A%5Cmax_%7B1%20%5Cleq%20k%20%5Cleq%20i%7D(score_%7Bi-k%2C%20j%7D%20%2B%20gap%5E*%20%2B%20(k-1)%20%5Ctimes%20gap)%20%5C%5C%0A%5Cmax_%7B1%20%5Cleq%20k%20%5Cleq%20j%7D(score_%7Bi%2C%20j-k%7D%20%2B%20gap%5E*%20%2B%20(k-1)%20%5Ctimes%20gap)%20%5C%5C%0A%5Cend%7Bcases%7D%24">

in which 

<img src="https://render.githubusercontent.com/render/math?math=%24compare(s_i%2C%20t_j)%20%3D%20%5Cbegin%7Bcases%7D%0Amatch%20%26%20%5Ctext%7Bif%20%7D%20s_i%20%3D%20t_j%20%5C%5C%0Amismatch%20%26%20%5Ctext%7Botherwise%7D%0A%5Cend%7Bcases%7D%24">

```python
smart_match.use('SW')
print(smart_match.similarity('Web Aplications', 'Web Application Development With PHP'))
```
Output:
```shell
0.8666666666666667
```

__SWG(SmithWatermanGotoh)__: Applies the Smith-Waterman algorithm to calculate the similarity between two strings. This implementation uses optimizations proposed by Osamu Gotoh.
Mathematically

<img src="https://render.githubusercontent.com/render/math?math=%24score_%7Bi%2C%20j%7D%20%3D%20%5Cmax%20%5Cbegin%7Bcases%7D%0A0%20%5C%5C%0Ascore_%7Bi-1%2C%20j-1%7D%20%2B%20compare(s_i%2C%20t_j)%20%5C%5C%0Ascore_%7Bi-1%2C%20j%7D%20%2B%20gap%20%5C%5C%0Ascore_%7Bi%2C%20j-1%7D%20%2B%20gap%20%5C%5C%0A%5Cend%7Bcases%7D%24">

in which 

<img src="https://render.githubusercontent.com/render/math?math=%24compare(s_i%2C%20t_j)%20%3D%20%5Cbegin%7Bcases%7D%0Amatch%20%26%20%5Ctext%7Bif%20%7D%20s_i%20%3D%20t_j%20%5C%5C%0Amismatch%20%26%20%5Ctext%7Botherwise%7D%0A%5Cend%7Bcases%7D%24">

```python
smart_match.use('SWG')
print(smart_match.similarity('GGTTGACTA', 'TGTTACGG'))
```
Output:
```shell
0.3125
```


__ME(MongeElkan)__: The Monge-Elkan similarity measure is a type of hybrid similarity measure that combines the benefits of sequence-based and set-based methods. It uses the other similarity method as inner method to consider similarity for each string pair in two string collections.

```python
smart_match.use('ME')
print(smart_match.similarity(['Hello', 'world'], ['Hero', 'world']))
smart_match.use('ME', 'cos')
print(smart_match.similarity(['Hello', 'world'], ['Hero', 'world']))
```
Output:
```shell
0.8
0.7834733547569204
```

# License

smart-match is a free software. See the file LICENSE for the full text.

# Authors

![qrcode_for_gh_b6c8ce1565a0_258][qrcode_for_gh_b6c8ce1565a0_258]

[qrcode_for_gh_b6c8ce1565a0_258]:data:image/jpg;base64,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

- Jiaying Wang (jiaying@sjzu.edu.cn)
- Jing Shan (shanjing@sjzu.edu.cn)
- Kaiwei Li
- Xiuzi Zhang
- YuQiang Feng
- XianFeng Du
- Zifan Guo
- JingLin Wu
- Mingyang Shao
- Yaxin Li
- Xueqing Xin
