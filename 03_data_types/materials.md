# Python Data Types

## Built-in Data Types

In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:

Type | Value
------------ | -------------
Text | str
Numeric | int, float, complex
Sequence | list, tuple, range
Mapping | dict
Set | set, frozenset
Boolean | bool
Binary | bytes,bytearray

### Getting the Data Type

You can get the data type of any object by using the type() function:

Print the data type of the variable x:

```py
x = 5
print(type(x))
```

### Setting the Data Type

In Python, the data type is set when you assign a value to a variable:

```py
x = "Hello World" #	str 	
x = 20 	#int 	
x = 20.5 	#float 	 	
x = ["apple", "banana", "cherry"] 	#list 	
x = ("apple", "banana", "cherry") 	#tuple 	
x = range(6) 	#range 	
x = {"name" : "John", "age" : 36} 	#dict 	
x = {"apple", "banana", "cherry"} 	#set 	
x = frozenset({"apple", "banana", "cherry"}) 	#frozenset 	
x = True 	#bool 	
x = b"Hello" 	#bytes 	
x = bytearray(5) 	#bytearray 	
x = memoryview(bytes(5)) 	#memoryview 	
```

### Setting the Specific Data Type

If you want to specify the data type, you can use the following constructor functions:

```py
x = str("Hello World") #	str 	
x = int(20) 	#int 	
x = float(20.5) 	#float 	
x = complex(1j) 	#complex 	
x = list(("apple", "banana", "cherry")) 	#list 	
x = tuple(("apple", "banana", "cherry")) 	#tuple 	
x = range(6) 	#range 	
x = dict(name="John", age=36) 	#dict 	
x = set(("apple", "banana", "cherry")) 	#set 	
x = frozenset(("apple", "banana", "cherry")) 	#frozenset 	
x = bool(5) 	#bool 	
x = bytes(5) 	#bytes 	
x = bytearray(5) 	#bytearray 	
x = memoryview(bytes(5)) 	#memoryview 	
```

---

### Python Numbers

There are three numeric types in Python:

* int
* float
<!--*    complex #We are not going to dive in this too deep -->
Variables of numeric types are created when you assign a value to them:

```py
x = 1    # int
y = 2.8  # float
```
<!-- z = 1j   # complex -->

To verify the type of any object in Python, use the type() function:

```py
print(type(x))
print(type(y))
```

<! -- print(type(z)) -->


### Int

Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

Integers:

```py
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
```

### Float

Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

Floats:

```py
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
```

Float can also be scientific numbers with an "e" to indicate the power of 10.

Floats:

```py
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
```

<!--
Complex

Complex numbers are written with a "j" as the imaginary part:


Complex:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
Type Conversion

You can convert from one type to another with the int(), float(), and complex() methods:
-->

Convert from one type to another:

```py
x = 1 # int
y = 2.8 # float
```

<!-- z = 1j # complex -->

> convert from int to float:
  > a = float(x)


> convert from float to int:
  > b = int(y)

<!--
#convert from int to complex:
c = complex(x)
-->

```py
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
```

> **Note: You cannot convert complex numbers into another number type.**

---

# Python Strings

## What is String in Python?

A string is a sequence of characters.
A character is simply a symbol. For example, the English language has 26 characters.
Computers do not deal with characters, they deal with numbers (binary). Even though you may see characters on your screen, internally it is stored and manipulated as a combination of 0's and 1's.
This conversion of character to a number is called encoding, and the reverse process is decoding. ASCII and Unicode are some of the popular encoding used.
In Python, string is a sequence of Unicode character. Unicode was introduced to include every character in all languages and bring uniformity in encoding. You can learn more about Unicode from here.

## How to create a string in Python?
Strings can be created by enclosing characters inside a single quote or double quotes. Even triple quotes can be used in Python but generally used to represent multiline strings and docstrings.
```py
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)
```

When you run the program, the output will be:

```txt
Hello
Hello
Hello
Hello, welcome to
           the world of Python
```

## How to access characters in a string?

We can access individual characters using indexing and a range of characters using slicing. Index starts from 0. Trying to access a character out of index range will raise an IndexError. The index must be an integer. We can't use float or other types, this will result into **TypeError**.
Python allows negative indexing for its sequences.
The index of -1 refers to the last item, -2 to the second last item and so on. We can access a range of items in a string by using the slicing operator (colon).
```py
str = 'programiz'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])
```

If we try to access index out of the range or use decimal number, we will get errors.

```py
    # index must be in range
    >>> my_string[15]  
    ...
    IndexError: string index out of range
    # index must be an integer
    >>> my_string[1.5] 
    ...
    TypeError: string indices must be integers
```

Slicing can be best visualized by considering the index to be between the elements as shown below.
If we want to access a range, we need the index that will slice the portion from the string.

## How to change or delete a string?

Strings are immutable. This means that elements of a string cannot be changed once it has been assigned. We can simply reassign different strings to the same name.

```py
    >>> del my_string[1]
    ...
    TypeError: 'str' object doesn't support item deletion
    >>> del my_string
    >>> my_string
    ...
    NameError: name 'my_string' is not defined
```

## Python String Operations

There are many operations that can be performed with string which makes it one of the most used datatypes in Python.

### Concatenation of Two or More Strings

Joining of two or more strings into a single one is called concatenation.

The **+** operator does this in Python. Simply writing two string literals together also concatenates them.

The __*__ operator can be used to repeat the string for a given number of times.

```py
str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)
```
Writing two string literals together also concatenates them like + operator.

If we want to concatenate strings in different lines, we can use parentheses.

```py
    >>> # two string literals together
    >>> 'Hello ''World!'
    'Hello World!'
    >>> # using parentheses
    >>> s = ('Hello '
    ...      'World')
    >>> s
    'Hello World'
```

## Iterating Through String
Using for loop we can iterate through a string. Here is an example to count the number of 'l' in a string.

```py
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')
```

## String Membership Test

We can test if a sub string exists within a string or not, using the keyword in.

```py
    >>> 'a' in 'program'
    True
    >>> 'at' not in 'battle'
    False
```

## Built-in functions to Work with Python

Various built-in functions that work with sequence, works with string as well.

Some of the commonly used ones are enumerate() and len(). The enumerate() function returns an enumerate object. It contains the index and value of all the items in the string as pairs. This can be useful for iteration.

Similarly, len() returns the length (number of characters) of the string.

```py
str = 'cold'

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))
```

## Python String Formatting

###Escape Sequence

If we want to print a text like -He said, "What's there?"- we can neither use single quote or double quotes. This will result into SyntaxError as the text itself contains both single and double quotes.

```py
    >>> print("He said, "What's there?"")
    ...
    SyntaxError: invalid syntax
    >>> print('He said, "What's there?"')
    ...
    SyntaxError: invalid syntax
```
One way to get around this problem is to use triple quotes. Alternatively, we can use escape sequences.

An escape sequence starts with a backslash and is interpreted differently. If we use single quote to represent a string, all the single quotes inside the string must be escaped. Similar is the case with double quotes. Here is how it can be done to represent the above text.

```py
# using triple quotes
print('''He said, "What's there?"''')

# escaping single quotes
print('He said, "What\'s there?"')

# escaping double quotes
print("He said, \"What's there?\"")
```
---
## Python List
Python offers a range of compound datatypes often referred to as sequences. List is one of the most frequently used and very versatile datatype used in Python.

### How to create a list?
In Python programming, a list is created by placing all the items (elements) inside a square bracket [ ], separated by commas.
It can have any number of items and they may be of different types (integer, float, string etc.).
```py
    # empty list
    my_list = []
    # list of integers
    my_list = [1, 2, 3]
    # list with mixed datatypes
    my_list = [1, "Hello", 3.4]
```

Also, a list can even have another list as an item. This is called nested list.

```py
# nested list
my_list = ["mouse", [8, 4, 6], ['a']]
```

### How to access elements from a list?

There are various ways in which we can access the elements of a list.

### List Index

We can use the index operator [] to access an item in a list. Index starts from 0. So, a list having 5 elements will have index from 0 to 4.
Trying to access an element other that this will raise an IndexError. The index must be an integer. We can't use float or other types, this will result into TypeError.
Nested list are accessed using nested indexing.

```py
    my_list = ['p','r','o','b','e']
    # Output: p
    print(my_list[0])
    # Output: o
    print(my_list[2])
    # Output: e
    print(my_list[4])
    # Error! Only integer can be used for indexing
    # my_list[4.0]
    # Nested List
    n_list = ["Happy", [2,0,1,5]]
    # Nested indexing
    # Output: a
    print(n_list[0][1])    
    # Output: 5
    print(n_list[1][3])
```

### Negative indexing

Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.
```py
    my_list = ['p','r','o','b','e']
    # Output: e
    print(my_list[-1])
    # Output: p
    print(my_list[-5])
```

### How to slice lists in Python?

We can access a range of items in a list by using the slicing operator (colon).

```py
    my_list = ['p','y','t','h','o','n',' ','c','o','u','r','s','e']
    # elements 3rd to 5th
    print(my_list[2:5])
    # elements beginning to 4th
    print(my_list[:-5])
    # elements 6th to end
    print(my_list[5:])
    # elements beginning to end
    print(my_list[:])
```

Slicing can be best visualized by considering the index to be between the elements as shown below. So if we want to access a range, we need two indices that will slice that portion from the list.

### How to change or add elements to a list?

List are mutable, meaning, their elements can be changed unlike string or tuple.

We can use assignment operator (=) to change an item or a range of items.

```py

    # mistake values
    odd = [2, 4, 6, 8]
    # change the 1st item
    odd[0] = 1
    # Output: [1, 4, 6, 8]
    print(odd)
    # change 2nd to 4th items
    odd[1:4] = [3, 5, 7]  
    # Output: [1, 3, 5, 7]
    print(odd)
```
We can add one item to a list using append() method or add several items using extend() method.

```py
    odd = [1, 3, 5]
    odd.append(7)
    # Output: [1, 3, 5, 7]
    print(odd)
    odd.extend([9, 11, 13])
    # Output: [1, 3, 5, 7, 9, 11, 13]
    print(odd)
```

We can also use + operator to combine two lists. This is also called concatenation.
The * operator repeats a list for the given number of times.

```py
    odd = [1, 3, 5]
    # Output: [1, 3, 5, 9, 7, 5]
    print(odd + [9, 7, 5])
    #Output: ["re", "re", "re"]
    print(["re"] * 3)
```

Furthermore, we can insert one item at a desired location by using the method insert() or insert multiple items by squeezing it into an empty slice of a list.

```py
    odd = [1, 9]
    odd.insert(1,3)
    # Output: [1, 3, 9] 
    print(odd)
    odd[2:2] = [5, 7]
    # Output: [1, 3, 5, 7, 9]
    print(odd)
```
## How to delete or remove elements from a list?

We can delete one or more items from a list using the keyword del. It can even delete the list entirely.
```py
    my_list = ['p','r','o','b','l','e','m']
    # delete one item
    del my_list[2]
    # Output: ['p', 'r', 'b', 'l', 'e', 'm']     
    print(my_list)
    # delete multiple items
    del my_list[1:5]  
    # Output: ['p', 'm']
    print(my_list)
    # delete entire list
    del my_list       
    # Error: List not defined
    print(my_list)
```

We can use remove() method to remove the given item or pop() method to remove an item at the given index.
The pop() method removes and returns the last item if index is not provided. This helps us implement lists as stacks (first in, last out data structure).
We can also use the clear() method to empty a list.

```py
    my_list = ['p','r','o','b','l','e','m']
    my_list.remove('p')
    # Output: ['r', 'o', 'b', 'l', 'e', 'm']
    print(my_list)
    # Output: 'o'
    print(my_list.pop(1))
    # Output: ['r', 'b', 'l', 'e', 'm']
    print(my_list)
    # Output: 'm'
    print(my_list.pop())
    # Output: ['r', 'b', 'l', 'e']
    print(my_list)
    my_list.clear()
    # Output: []
    print(my_list)
```

Finally, we can also delete items in a list by assigning an empty list to a slice of elements.

```py
    >>> my_list = ['p','r','o','b','l','e','m']
    >>> my_list[2:3] = []
    >>> my_list
    ['p', 'r', 'b', 'l', 'e', 'm']
    >>> my_list[2:5] = []
    >>> my_list
    ['p', 'r', 'm']
```

##  List Comprehension: Elegant way to create new List

List comprehension is an elegant and concise way to create new list from an existing list in Python.
List comprehension consists of an expression followed by for statement inside square brackets.
Here is an example to make a list with each item being increasing power of 2.

```py
    pow2 = [2 ** x for x in range(10)]
    # Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    print(pow2)
```

This code is equivalent to
```py
    pow2 = []
    for x in range(10):
       pow2.append(2 ** x)
```

A list comprehension can optionally contain more for or if statements. An optional if statement can filter out items for the new list. Here are some examples.

```py
    >>> pow2 = [2 ** x for x in range(10) if x > 5]
    >>> pow2
    [64, 128, 256, 512]
    >>> odd = [x for x in range(20) if x % 2 == 1]
    >>> odd
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    >>> [x+y for x in ['Python ','C '] for y in ['Language','Programming']]
    ['Python Language', 'Python Programming', 'C Language', 'C Programming']
```


# Other List Operations in Python

## List Membership Test

We can test if an item exists in a list or not, using the keyword in.
```py
    my_list = ['p','r','o','b','l','e','m']
    # Output: True
    print('p' in my_list)
    # Output: False
    print('a' in my_list)
    # Output: True
    print('c' not in my_list)
```

## Iterating Through a List

Using a for loop we can iterate though each item in a list.
```py
    for fruit in ['apple','banana','mango']:
        print("I like",fruit)
```

---
