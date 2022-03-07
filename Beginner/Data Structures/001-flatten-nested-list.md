# **001-Flatten a List of Lists**

Welcome to Python challenges. Practice your Python Skills daily with Python challenges. In this Python code challenge series we hope to compliment the existing Python courses on this channel. Code challenges are for people looking to sharpen their Python skills first at a beginner's level with the ambition to then move into more advanced challenges as we progress.

---
## Donations
We rely on your contributes to keep doing what we do. If you have found value in the content, please consider supporting us.

<a href="https://www.patreon.com/bePatron?u=69834971" data-patreon-widget-type="become-patron-button">Become a Patron!</a>

<a href="https://www.paypal.com/donate?hosted_button_id=W55GVT4UPXPYE" 
target="_blank">
Donate via PayPal
</a>

---

**Video Tutorial:** https://

---
#### **Category:** Data Structures
#### **Difficulty:** Beginner
#### **Tags/Keywords:** list, flatten
---

## **Code Challenge:**
Write a function that tasks a nested list ex: [[1,2,3,4],["a","b","c"],[5,6,7,8]] and flattens it into a one-dimensional list [1,2,3,4,a,b,c,5,6,7,8]. Your function should take a single parameter and return a flattened list.

----

### Code Examples

```python
# 1.0.0

nl = [[1,2,3,4],["a","b","c"],[5,6,7,8]]

def flatlist(nl):
    flatlist=[]
    for sublist in nl:
        for e in sublist:
                flatlist.append(e)
    return flatlist
print(flatlist(nl))

# 1.0.1

nl = [[[[1]]]]

for a in nl:
    for b in a:
        for c in b:
            for d in c:
                print(d)

# 1.0.2

nested_list = [ [1, ["a","b"], 2, 3], [4, 5] ]
if nested_list[0][1][0]:
   print(nested_list[1][0])
else:
   print(nested_list[1][1])

print(nested_list[0][1][0])

```

```python
# 2.0.0
import itertools

nla = [[1,2,3,4],["a","b","c"],[5,6,7,8]]
nlb = [[1,2,[3,[4]]],["a","b","c"],[5,6,7,8]]

print(list(itertools.chain(*nl)))
print(list(itertools.chain.from_iterable(nl)))
```

```python
# 3.0.0
from functools import reduce

nla = [[1,2,3,4],["a","b","c"],[5,6,7,8]]
print(reduce(lambda a, b: a + b, nla))

```

```python
# 4.0.0
"""
Because you are summing nested lists, you actually get 
[1,2,3,4]+["a","b","c"]+[5,6,7,8] as a result equals 
[1, 2, 3, 4, 'a', 'b', 'c', 5, 6, 7, 8]. 
The append operation on lists forms a Monoid.
"""
nla = [[1,2,3,4],["a","b","c"],[5,6,7,8]]
print(sum(nla, []))


## References & Further Reading
- https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
- https://docs.python.org/3/library/itertools.html#itertools.chain.from_iterable
- https://mathieularose.com/how-not-to-flatten-a-list-of-lists-in-python
```

```python
# 5.0.0
"""
Solution to resolve nested list with recursion.
"""
nln = [[1,2,[3,4]],["a","b","c"],[5,[6],7,8]]

def fun_flatlist(nl):
    flatlist=[]
    for sublist in nl:
        if isinstance(sublist, list):
            flatlist.extend(fun_flatlist(sublist))
        else:
            flatlist.append(sublist)
    return flatlist
print(fun_flatlist(nln))
```
