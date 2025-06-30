print("string in pyhton are in mutable")


# find endswith count center index isalnum
# isalpha islower isprintable issapce istitle
#isupper isswap title

apple = '''
lower()	Converts string to lowercase	'HELLO'.lower() → 'hello'
upper()	Converts string to uppercase	'hello'.upper() → 'HELLO'
title()	Capitalizes each word in the string	'hello world'.title() → 'Hello World'
capitalize()	Capitalizes the first letter of the string	'hello'.capitalize() → 'Hello'
swapcase()	Swaps the case of all letters in the string	'Hello'.swapcase() → 'hELLO'
strip()	Removes leading and trailing whitespace	' hello '.strip() → 'hello'
replace()	Replaces a substring with another	'hello world'.replace('world', 'Python') → 'hello Python'
split()	Splits the string into a list of substrings	'hello world'.split() → ['hello', 'world']
join()	Joins elements of an iterable with a string	' '.join(['hello', 'world']) → 'hello world'
find()	Finds the index of the first occurrence of a substring	'hello'.find('o') → 4
count()	Counts occurrences of a substring	'hello'.count('l') → 2
startswith()	Checks if the string starts with a substring	'hello'.startswith('he') → True
endswith()	Checks if the string ends with a substring	'hello'.endswith('lo') → True
isalnum()	Checks if all characters are alphanumeric	'hello123'.isalnum() → True
isdigit()	Checks if all characters are digits	'12345'.isdigit() → True
isalpha()	Checks if all characters are alphabetic	'hello'.isalpha() → True
'''
text = "Hello"
print(text.lower())  # Output: "hello"
text = "Hello"
print(text.upper())  # Output: "HELLO"
text = "hello world"
print(text.title())  # Output: "Hello World"
text = "hello"
print(text.capitalize())  # Output: "Hello"
text = "Hello World"
print(text.swapcase())  # Output: "hELLO wORLD"
text = "  hello  "
print(text.strip())  # Output: "hello"
text = "  hello  "
print(text.lstrip())  # Output: "hello  "
text = "  hello  "
print(text.rstrip())  # Output: "  hello"
text = "hello world"
print(text.replace("world", "Python"))  # Output: "hello Python"
text = "hello world"
print(text.split())  # Output: ['hello', 'world']
words = ["hello", "world"]
print(" ".join(words))  # Output: "hello world"
text = "hello world"
print(text.find("world"))  # Output: 6
print(text.find("python"))  # Output: -1
text = "hello world hello"
print(text.rfind("hello"))  # Output: 12
text = "hello world"
print(text.index("world"))  # Output: 6
# print(text.index("python"))  # Raises ValueError
text = "hello world hello"
print(text.rindex("hello"))  # Output: 12
text = "hello world hello"
print(text.count("hello"))  # Output: 2
text = "hello world hello"
print(text.count("hello"))  # Output: 2
text = "hello world"
print(text.startswith("hello"))  # Output: True
print(text.startswith("world"))  # Output: False
text = "hello world"
print(text.endswith("world"))  # Output: True
print(text.endswith("hello"))  # Output: False
text = "hello"
print(text.isalpha())  # Output: True

text = "hello123"
print(text.isalpha())  # Output: False

text = "12345"
print(text.isdigit())  # Output: True

text = "123a45"
print(text.isdigit())  # Output: False

text = "hello123"
print(text.isalnum())  # Output: True

text = "hello 123"
print(text.isalnum())  # Output: False

text = "hello"
print(text.islower())  # Output: True

text = "Hello"
print(text.islower())  # Output: False

text = "HELLO"
print(text.isupper())  # Output: True

text = "Hello"
print(text.isupper())  # Output: False


text = "12345"
print(text.isnumeric())  # Output: True

text = "42"
print(text.zfill(5))  # Output: "00042"

text = "Hello {}"
print(text.format("World"))  # Output: "Hello World"
























