# **003-Running Total**

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
- write a program that accepts 2 types of inputs, I and O and a value to keep track of quantities entered into the input
- each input should be inputed so to include a value, format example: I-10 O-10, this would return a qty of 0, (10-10=0)
Users should be able to continually enter a input until all inputs have been entered
- after each input the user is shown the quality update

#### **Constraints:**
- None

----

### Code Examples

```python
# 1.0.0
qty = 0
while True:

    x = input()
    if not x:
        break

    n_value = x.split("-")
    process = n_value[0]

    if process=="I":
        qty+=int(n_value[1])
        print(f"New Total: {qty}")
    elif process=="O":
        qty-=int(n_value[1])
        print(f"New Total: {qty}")
    else:
        pass

print(f"Final Quantity:{qty}")
```