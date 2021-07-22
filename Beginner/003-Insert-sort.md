# 002-Insertion Sort

Welcome to Python challenges. Practice your Python Skills daily with Python challenges. 

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
range, sorting, insertion sort

----

### Code Examples

```
# ex1.0.1 Insertion Sort

def insertion_sort(nts):

    for i in range(1, len(nts)):
        current_num = nts[i]

        j = i - 1

        while j >= 0 and nts[j] > current_num:
            nts[j + 1] = nts[j]
            j -= 1

        nts[j + 1] = current_num
---
```
# ex1.0.2 Insertion Sort Comparison

import time
import timeit
from random import randint


def run_sorting(algorithm, nts):
    setup_code = f"from __main__ import {algorithm}"

    stmt = f"{algorithm}({nts})"

    time = timeit.repeat(stmt=stmt, setup=setup_code, repeat=1, number=1)

    print(f"{algorithm}: {min(time)}")


def insertion_sort(nts):

    for i in range(1, len(nts)):
        current_num = nts[i]

        p = i - 1

        while p >= 0 and nts[p] > current_num:
            nts[p + 1] = nts[p]
            p -= 1

        nts[p + 1] = current_num


def bubbleSort(nts):

    nts_len = len(nts)

    for i in range(nts_len):
        for p in range(nts_len - i - 1):
            if nts[p] > nts[p + 1]:
                nts[p], nts[p + 1] = nts[p + 1], nts[p]
    return nts


if __name__ == "__main__":

    nts = [randint(0, 10000) for i in range(5000)]

    run_sorting(algorithm="insertion_sort", nts=nts)
    run_sorting(algorithm="bubbleSort", nts=nts)

```


### **Further reading**
https://realpython.com/sorting-algorithms-python/
https://www.pyscoop.com/sorting-algorithms-implementation-in-python/
https://www.quora.com/Why-is-insertion-sort-faster-than-bubble-sort-while-having-the-same-big-O-notation