# **003-Repeating String Characters**

Welcome to Python challenges. Practice your Python Skills daily with Python challenges. In this Python code challenge series we hope to compliment the existing Python courses on this channel. Code challenges are for people looking to sharpen their Python skills first at a beginner's level with the ambition to then move into more advanced challenges as we progress. But most importantly, this was made for the intention to try and just have a little fun with Python.

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

### **Category:** Strings
#### **Difficulty:** Warm-up/Beginner
#### **Tags/Keywords:** masking
---
## **Code Challenge:**
Write a new function that take in a credit card number and returns a masked number. Only show the last 4 digits of the credit card number.

#### **Notes/Constraints:**
- Cards may have different amount of numbers

----

### Code Examples

```python
# ex1.0.1
str = "5655454445441345";

string_length = len(str)
mask = string_length - 4
showstr = str[mask:]

#print(mask)
#print(showstr)

print ("*" * mask + showstr)
```

```python
# ex1.0.2
def masking(number, mask):
    str = ''
    n = mask
    for char in number[:-n]:
        str += '#'
    str += number[-n:]
    return str

print(masking("1111222233334444", 4))
```

```python
# ex1.0.3
str="1234123412341234"
print(str[-4:].rjust(len(str), "*"))
```

```python
# ex1.0.4
str="1234123412341234"
print (str[:4] + '*' * 4 + str[-4:])
```

```python
# ex1.0.5
str="1234123412341234"
print('{:*>16}'.format(str[-4:]))
```

```python
# ex1.0.5
str="1234123412341234"
def masking(number, start_num=0, end_num=0, char="#"):
  number_len = len(number)
  mask_len = number_len - abs(start_num) - abs(end_num)
  return(number[:abs(start_num)] + (char * mask_len) + number[-end_num:])

print(masking(str, 0, 4, "@"))
```

```python
# ex1.0.6
import re
str = "1234123412341234";
print(re.sub('[0-9]', '*', str[:-4]) + str[-4:])

# regular expression pattern
# re.sub(pattern, repl, string, count=0, flags=0);
```