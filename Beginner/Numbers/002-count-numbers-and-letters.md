# **002-Count Numbers and Letters**

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
Write a program that accepts letters and numbers and returns the quantity of numbers and letters inputed. Extend the program to count and return the quantity of upper and lower case characters inputed

#### **Constraints:**
- None

----

### Code Examples

```python
# 1.0.0
user_input = input()
counted={"Numbers":0,"Letters":0,"Upper":0,"Lower":0}

for i in user_input:
    if i.isalpha():
        counted["Letters"]+=1
    elif i.isdigit():
        counted["Numbers"]+=1 
        
    if i.isupper():
        counted["Upper"]+=1
    elif i.islower():
        counted["Lower"]+=1

print(counted)
```