# **001-Get File Size**

Welcome to Python challenges. Practice your Python Skills daily with Python challenges. In this Python code challenge series we hope to compliment the existing Python courses on this channel. Code challenges are for people looking to sharpen their Python skills first at a beginner's level with the ambition to then move into more advanced challenges as we progress.

**Video Tutorial:** https://

---
#### **Category:** Files
#### **Difficulty:** Beginner
#### **Tags/Keywords:** file size
---

## **Code Challenge:**
File the size of a given file

#### **Constraints:**
- None

----

### Code Examples

```python
# 1.0.0

import os
  
path = '/file.txt'
  
# Get file size (in bytes)
size = os.path.getsize(path)
print(f"Size in bytes: {size}")

```
```python
# 1.0.1

import os
  
# statinfo = os.stat('a2.py')
statinfo = os.stat('a2.py').st_size
print statinfo

```
```python
# 1.0.2

import os
  
path = '/file.txt'
  
try:
    size = os.path.getsize(path)

except OSError:
    print("File error")
    sys.exit()

print(f"Size in bytes: {size}")

```

## References
- https://docs.python.org/3/library/stat.html
- https://github.com/python/cpython/blob/main/Lib/genericpath.py