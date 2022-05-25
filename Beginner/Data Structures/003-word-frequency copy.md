# **003-Word Frequency**

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

**Video Tutorial:** https://youtu.be/GKPUPeHcmYY

---
#### **Category:** Data Structures
#### **Difficulty:** Beginner
#### **Tags/Keywords:** 
---

## **Code Challenge:**
Write a programme that counts the frequency of all words from a given input

----

### Code Examples

```python
# 1.0.0

freq = {} 
line = input()

for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
words = sorted(words)

for w in words:
    print (f"{w} = {freq[w]}")
```