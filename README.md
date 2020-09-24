# Introduction

The smart-match module contains functions for functions for calculating string similarity.

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

# License

smart-match is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

See the file COPYING for the full text of GNU General Public License version 2.
