"""
1. Find and Replace:

Replace all occurrences of the word "apple" with "orange" in the given string: "I have an apple, and the apple is red."
Raw String Usage:

Answer:-
"""
'I have an apple, and the apple is red'.replace("apple", "orange")

"""

2. Create a formatted string that displays the result of multiplying 15 by 3 using an f-string.

Answer:-
"""
f'{15*3} is the result of 15 times 3'

"""
3. Slicing and Indexing:

Extract the last three characters of a string without using the len() function.

Answer:-
"""
"Hello, World!"[-3:]

"""

Count Method:

Write a function to count the number of occurrences of the word "Python" in a given text.

Answer:-
"""
text = "your msg..."

def countToken(passedText) {
    text = passedText
    return text.count("Python")
}

print(countToken(text))

"""
Find Method:

Use the find() method to locate the first occurrence of the word "error" in the string: "An error occurred in the program."
Replacing with a Limit:

Replace only the first two occurrences of the word "red" with "blue" in the string: "The red car and the red house."
Using Slice for Reversal:

Reverse the characters of a string using slicing in a single line of code.
Count Digits:

Write a function to count the number of digits in a given numeric string.
Find and Replace with Case Sensitivity:

Replace all occurrences of the word "apple" (case-sensitive) with "orange" in the string: "I have an Apple, and the apple is red."
Formatted String for Decimal Places:

Create a formatted string that displays the value of Pi (3.14159265) with only two decimal places.
Slice and Concatenate:

Given two strings "Hello" and "World", use slicing to create a new string: "HrWl".
Using r"..." for File Paths:

Explain why using a raw string (r"...") is beneficial when working with file paths in Python.
Find and Replace Whole Words:

Replace only the whole word "cat" with "dog" in the sentence: "The cat is catching a caterpillar."
Formatted String with Variable:

Given a variable name = "Alice", create a formatted string to greet Alice: "Hello, Alice!".
Slicing for Every Nth Character:

Using slicing, create a new string that includes every third character from the original string.
Count Method for Overlapping Substrings:
"""


"""

Write a function to count the number of occurrences of the substring "ab" in the string: "ababababab".
Answer:-
"""


"""
Find and Replace with Regular Expression:

Use a regular expression to replace all occurrences of digits with "X" in the string: "The price is $25.99"

Answer:-
"""


"""
Formatted String for Binary Representation:

Given an integer num = 42, create a formatted string that displays its binary representation.

Answer:-
"""


"""
Slicing for Skipping Characters:

Using slicing, create a new string that includes every second character starting from the second character of the original string.

Answer:- 
"""
text[1::2]