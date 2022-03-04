# **001-Get File Size**

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