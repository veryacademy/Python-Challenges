# **003-Repeating String Characters**

Welcome to Python challenges. Practice your Python Skills daily with Python challenges. In this Python code challenge series we hope to compliment the existing Python courses on this channel. Code challenges are for people looking to sharpen their Python skills first at a beginner's level with the ambition to then move into more advanced challenges as we progress. But most importantly, this was made for the intention to try and just have a little fun with Python.

**Video Tutorial:** 

### **Category:** Strings
#### **Difficulty:** Warm-up/Beginner
#### **Tags/Keywords:** double_char
---

## **Code Challenge:**
Write a new function that passing in a new string. The function should return a string whereby each character of the original string has been repeated once.

#### **Notes/Constraints:**
- Let's not go too crazy, the string might include spaces or other special characters, everything should be repeated.

----

### Code Examples

```python
# ex1.0.1

str = "hello"

def double_char_1(str):
    result = ""
    for char in str:
        result += char * 2
    return result

print(double_char_1(str))

```


---
### **Further reading**
Ulm, G., 2021. Coding Bat: Python. String-2. [online] Gregor Ulm. Available at: <https://gregorulm.com/coding-bat-python-string-2/> [Accessed 10 August 2021].
Docs.python.org. 2021. unittest — Unit testing framework — Python 3.9.6 documentation. [online] Available at: <https://docs.python.org/3/library/unittest.html#> [Accessed 9 August 2021].