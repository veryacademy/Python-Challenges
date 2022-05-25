# **004-Input Conversion**

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

**Video Tutorial:** 

---
#### **Category:** Data Structures
#### **Difficulty:** Beginner
#### **Tags/Keywords:** 
---

## **Code Challenge:**
Write a programme that accepts a list of numbers or strings separated by commas and generates the input into a tuple, list and dictionary

----

### Code Examples

```python
# 1.0.0

values = input("Please insert new items: ")
new_values = values.split(",")

c_tuple = tuple(new_values)

print(new_values) # list
print(c_tuple) # tuple

keys = range(0,len(new_values))

c_dict = {}

for i in keys:
    c_dict[i] = new_values[i]

print(c_dict)
```

```python
# 1.0.1

c_dict = {i : new_values[i] for i in range(0, len(new_values))}
print(c_dict)
```
```python
# 1.0.2

x = dict(list(enumerate(new_values)))
print(x)
```