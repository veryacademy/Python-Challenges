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

import unittest

str = "hello"


def double_char_1(str):
    x = list(str)
    prep = []
    output = ""
    for i in range(len(x)):
        prep.append(x[i])
        prep.append(x[i])

    # Alternative 1
    # for i in range(len(prep)):
    #     output += prep[i]
    # return output

    # Alternative 2
    return "".join(prep)


def double_char_2(str):
    result = ""
    for char in str:
        # Alt 1
        result = result + char + char
        # Alt 2
        # result += char * 2
    return result


# Exotic
def double_char_3(str):
    for x in str:
        yield x * 2


def double_char_4(str):
    return "".join([x + x for x in str])


print(f"1:{double_char_1(str)}")
print(f"2:{double_char_2(str)}")
print(f"3:{''.join(double_char_3(str))}")
print(f"4:{double_char_4(str)}")


class TestDoubleMethod(unittest.TestCase):
    # A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs.
    # unittest provides a base class, TestCase, which may be used to create new test cases.

    # A testcase is created by subclassing unittest.TestCase. The three individual tests
    # are defined with methods whose names start with the letters test.
    # This naming convention informs the test runner about which methods represent tests.

    param_list = [("hello", "hheelllloo"), ("world", "wwoorrlldd")]

    def test_capitals(self):
        for p1, p2 in self.param_list:
            with self.subTest():
                self.assertEqual(double_char_2(p1), p2)


if __name__ == "__main__":
    unittest.main()


```


---
### **Further reading**
Ulm, G., 2021. Coding Bat: Python. String-2. [online] Gregor Ulm. Available at: <https://gregorulm.com/coding-bat-python-string-2/> [Accessed 10 August 2021].
Python, R., 2021. How to Use Generators and yield in Python – Real Python. [online] Realpython.com. Available at: <https://realpython.com/introduction-to-python-generators/> [Accessed 7 August 2021].
Caktusgroup.com. 2021. Subtests are the Best | Caktus Group. [online] Available at: <https://www.caktusgroup.com/blog/2017/05/29/subtests-are-best/> [Accessed 10 August 2021].
Docs.python.org. 2021. unittest — Unit testing framework — Python 3.9.6 documentation. [online] Available at: <https://docs.python.org/3/library/unittest.html#> [Accessed 9 August 2021].