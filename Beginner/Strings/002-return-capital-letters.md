# **002-Returning Capital Letters**

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
**Video Tutorial:** https://youtu.be/ZnrjWPjF6Xs

### **Category:** Strings
#### **Difficulty:** Warm-up/Beginner
#### **Tags/Keywords:** slice, true division, floor division, integer division
---

## **Code Challenge:**
Write a function named capitals. The function should takes a single parameter which you can name word. Your function should return a list of all the capital letters letters in the string.

#### **Notes/Constraints:**
- None

----

### Code Examples

```python
# ex1.0.1 Using a generator

def capitals(word):

    x = []

    test = [char for char in word if char.isupper()]
    yield test


print(next(capitals("AbCdE")))
```

```python
# ex1.0.2 

import unittest

def capitals(word):

    x = []

    for char in word:
        if char.isupper():
            x.append(char)
    return x

print(capitals("AbCdE"))

class TestCapitalMethod(unittest.TestCase):

  param_list = [("AbCdE", "ACE"), ("aBcDe", "BD")]

  def test_capitals(self):
    for p1, p2 in self.param_list:
      with self.subTest():
        str1 = "".join(capitals(p1))
        self.assertEqual(str1, p2)

if __name__ == "__main__":
  unittest.main()
```

---
### **Further reading**
Python, R., 2021. How to Use Generators and yield in Python – Real Python. [online] Realpython.com. Available at: <https://realpython.com/introduction-to-python-generators/> [Accessed 7 August 2021].

Docs.python.org. 2021. unittest — Unit testing framework — Python 3.9.6 documentation. [online] Available at: <https://docs.python.org/3/library/unittest.html#> [Accessed 9 August 2021].