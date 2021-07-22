# 001-Bubble Sort

Welcome to Python challenges. Practice your Python Skills daily with Python challenges. 

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

## ***Code Challenge:***
Given a list of numbers sort the numbers from lowest to highest.

#### **Constraints:**
- None

----
#### **Prerequisites:**
- Level: Beginner
- Python 3.5+

----
### Tags/Keywords
range, sorting, bubble sort

----

### Code Examples

```
# ex1.0.1 Using Python sorted()

if __name__ == "__main__":
    nts = [2, 23, 1, 52, 22, 10, 100]
    print(sorted(nts))
```
```
# ex1.0.2 Generating a list

from random import randint

if __name__ == "__main__":
    nts = [randint(0, 100) for i in range(100)]
    print(nts)
    print(sorted(nts))
```
```
# ex1.0.3 Bubble sort example

from random import randint


def bubbleSort(nts):

    nts_len = len(nts)

    for i in range(nts_len):
        for p in range(nts_len - i - 1):
            if nts[p] > nts[p + 1]: # change to < for descending
                nts[p], nts[p + 1] = nts[p + 1], nts[p]
    return nts


if __name__ == "__main__":

    nts = [randint(0, 100) for i in range(100)]
    sorted = bubbleSort(nts)

    print(f"Unsorted: {nts}")
    print(f"sorted: {sorted}")

```
```
# ex1.0.4 Measuring algorithm performance

import time
import timeit
from random import randint


def run_sorting(algorithm, nts):
    setup_code = f"from __main__ import {algorithm}"

    stmt = f"{algorithm}({nts})"

    # repeat specifies the number of samples to take
    # number specifies the number of times to repeat the code for each sample.
    time = timeit.repeat(stmt=stmt, setup=setup_code, repeat=1, number=1)

    print(f"Quickest execution time: {min(time)}")


def bubbleSort(nts):

    nts_len = len(nts)

    for i in range(nts_len):
        for p in range(nts_len - i - 1):
            if nts[p] > nts[p + 1]:
                nts[p], nts[p + 1] = nts[p + 1], nts[p]


if __name__ == "__main__":

    nts = [randint(0, 10000) for i in range(5000)]
    run_sorting(algorithm="bubbleSort", nts=nts)
```
---
### **Further reading**
https://realpython.com/sorting-algorithms-python/
https://www.pyscoop.com/sorting-algorithms-implementation-in-python/