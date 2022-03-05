# **002-Word Anagrams**

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
#### **Category:** Data Structures
#### **Difficulty:** Beginner
#### **Tags/Keywords:** list, sorted, for loop
---

## **Code Challenge:**
An anagram is a word or phrase made by using the letters of another word or phrase in a different order. For example, Python and Typhon both use the same letters to form two different words. Create a function that checks if a given word is an anagram of another word. Build a funciton that takes 2 parameters, the inital word and the word you want to check is a anagram of the first word. Output True if an anagram was found and False if not.

### Extention challange
Create a small applicaton that asks the users to type in a word and check the users word against a list of existing words.

----

### Code Examples

```python
# 1.0.0

def check_for_anagram(word1, word2):
    word1 = list(str1)
    word1.sort()
    word2 = list(str2)
    word2.sort()

    return (word1 == word2)

print(check_for_anagram("test","tset"))

# 1.0.1

def check_for_anagram(word1, word2):
    word1 = list(str1)
    word2 = list(str2)

    return sorted(word1) == sorted(word2)

print(check_for_anagram("test","tset"))

```

```python
# 2.0.0
user_input = input("Enter a word: ")
library = ['python', 'typhon', 'sunny', 'windy']

for word in library:
    if sorted(user_input) == sorted(word):
        print(word)

```

## References & Further Reading
- None