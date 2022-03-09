# **003-Extract Usernames from Emails**

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
#### **Tags/Keywords:** split, list comprehension
---
## **Code Challenge:**
Write a function that strips and returns a username for any given email address. For example user@org.com, the output should return user.

----

### Code Examples

```python
# ex1.0.1
email = "me@org.com"
emails = ["a@org.com", "b@org.com", "c@org.com"]

single_email = email.split("@")[0]
many_emails = [x.split("@")[0] for x in emails]

print(single_email)
print(many_emails)

```
```python
# ex1.0.2
def return_username(e):
    return e.split("@")[0]

x = input("Enter email address: ")
print(return_username(x))
```
