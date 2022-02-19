# **001-Return half a string**

Welcome to Python challenges. Practice your Python Skills daily with Python challenges. In this Python code challenge series we hope to compliment the existing Python courses on this channel. Code challenges are for people looking to sharpen their Python skills first at a beginner's level with the ambition to then move into more advanced challenges as we progress.

## Donations
Very Academy is all about teaching you simple actionable code. We rely on your contributes to keep doing what we do. If you have found value in the content, please consider supporting us.

<a href="https://www.patreon.com/bePatron?u=69834971" data-patreon-widget-type="become-patron-button">Become a Patron!</a>

<a href="https://www.paypal.com/donate?hosted_button_id=W55GVT4UPXPYE" 
target="_blank">
Contribute via PayPal
</a>

## Donations
**Video Tutorial:** https://youtu.be/esHMjvP2-hs

---
#### **Category:** Strings
#### **Difficulty:** Warm-up/Beginner
#### **Tags/Keywords:** slice, true division, floor division, integer division
---

## **Code Challenge:**
Given a string of any length, return 50% or half of the given string.

#### **Constraints:**
- Should a given string have an odd number of letters, round down to the nearest number.

----

### Code Examples

```
# ex1.0.1 

# Floating point division (true division) 
# Floor division (integer division)
def ex_1(str):
    # return len(str) / 2
    return len(str) // 2

print(ex_1("testa"))
```


```
# ex1.0.2 

# Does not return half when odd number of letters
# Slice indexing syntax instead of slice()
# iterable_obj[start:stop:step]
def ex_2(str):
    return str[:int(len(str) / 2)]
```

```
# ex1.0.3 

# floor division operator
def ex_3(str):
    return str[:len(str) // 2]
```

```
# ex1.0.4 Unittest

import unittest

class TestStringMethods(unittest.TestCase):

    param_list = [('return', 'ret'), ('academy', 'aca'), ('zander', 'zan')]

    def test_ex3(self):
        for p1, p2 in self.param_list:
            with self.subTest():
                x = ex_2(p1)
                self.assertEqual(x, p2)

    def test_ex3(self):
        for p1, p2 in self.param_list:
            with self.subTest():
                x = ex_3(p1)
                self.assertEqual(x, p2)

if __name__ == '__main__':
    unittest.main()
```
---
### **Further reading**
Pieters, M. and saffar, a., 2021. What is the difference between int() and floor() in Python 3?. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/31036098/> [Accessed 19 July 2021].

Fooz, M. and Rosenfield, A., 2021. What does if __name__ == "__main__": do?. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/419163/what-does-if-name-main-do> [Accessed 19 July 2021].

freeCodeCamp.org. 2021. Python if __name__ == __main__ Explained with Code Examples. [online] Available at: <https://www.freecodecamp.org/news/if-name-main-python-example/> [Accessed 22 July 2021].
