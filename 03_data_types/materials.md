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

Here is a list of all the escape sequence supported by Python.

#### Escape Sequence in Python

Escape Sequence | Description
-------------- | -------------------
\newline | Backslash and newline ignored
\\ | Backslash
\' | Single quote
\" | Double quote
\a | ASCII Bell
\b | ASCII Backspace
\f | ASCII Formfeed
\n | ASCII Linefeed
\r | ASCII Carriage Return
\t |ASCII Horizontal Tab
\v | ASCII Vertical Tab
\ooo | Character with octal value ooo
\xHH | Character with hexadecimal value HH

Here are some examples
```py
    >>> print("\\")
    \
    >>> print("This is printed\nin two lines")
    This is printed
    in two lines
    >>> print("This is \x48\x45\x58 representation")
    This is HEX representation
```

### Raw String to ignore escape sequence

Sometimes we may wish to ignore the escape sequences inside a string. To do this we can place r or R in front of the string. This will imply that it is a raw string and any escape sequence inside it will be ignored.

```py
   >>> print("This is \x41 \ngood example")
    This is A
    good example
   >>> print(r"This is \x41 \ngood example")
    This is \x41 \ngood example
```

### The format() Method for Formatting Strings

The format() method that is available with the string object is very versatile and powerful in formatting strings. Format strings contains curly braces {} as placeholders or replacement fields which gets replaced.

We can use positional arguments or keyword arguments to specify the order.

```py
# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)
```

The format() method can have optional format specifications. They are separated from field name using colon. For example, we can left-justify <, right-justify > or center ^ a string in the given space. We can also format integers as binary, hexadecimal etc. and floats can be rounded or displayed in the exponent format. There are a ton of formatting you can use. Visit here for all the string formatting available with the format() method.

```py
    >>> # formatting integers
    >>> "Binary representation of {0} is {0:b}".format(12)
    'Binary representation of 12 is 1100'
    >>> # formatting floats
    >>> "Exponent representation: {0:e}".format(1566.345)
    'Exponent representation: 1.566345e+03'
    >>> # round off
    >>> "One third is: {0:.3f}".format(1/3)
    'One third is: 0.333'
    >>> # string alignment
    >>> "|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham')
    '|butter    |  bread   |       ham|'
```
### Old style formatting

We can even format strings like the old sprintf() style used in C programming language. We use the % operator to accomplish this.
```py
    >>> x = 12.3456789
    >>> print('The value of x is %3.2f' %x)
    The value of x is 12.35
    >>> print('The value of x is %3.4f' %x)
    The value of x is 12.3457
```

### Common Python String Methods

There are numerous methods available with the string object. The format() method that we mentioned above is one of them. Some of the commonly used methods are lower(), upper(), join(), split(), find(), replace() etc. Here is a complete list of all the built-in methods to work with strings in Python.

```py
    >>> "PrOgRaMiZ".lower()
    'programiz'
    >>> "PrOgRaMiZ".upper()
    'PROGRAMIZ'
    >>> "This will split all words into a list".split()
    ['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']
    >>> ' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
    'This will join all words into a string'
    >>> 'Happy New Year'.find('ew')
    7
    >>> 'Happy New Year'.replace('Happy','Brilliant')
    'Brilliant New Year'
```

---

# Python List

Python offers a range of compound datatypes often referred to as sequences. List is one of the most frequently used and very versatile datatype used in Python.

## How to create a list?

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

## How to access elements from a list?

There are various ways in which we can access the elements of a list.

## List Index

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

## Negative indexing

Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.

```py
    my_list = ['p','r','o','b','e']
    # Output: e
    print(my_list[-1])
    # Output: p
    print(my_list[-5])
```

## How to slice lists in Python?

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

## How to change or add elements to a list?

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

## List Comprehension: Elegant way to create new List

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

# Python Tuple

A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas, in a list, elements can be changed.

## Creating a Tuple

A tuple is created by placing all the items (elements) inside parentheses (), separated by commas. The parentheses are optional, however, it is a good practice to use them.

A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).

```py
    # Empty tuple
    my_tuple = ()
    print(my_tuple)  # Output: ()

    # Tuple having integers
    my_tuple = (1, 2, 3)
    print(my_tuple)  # Output: (1, 2, 3) 

    # tuple with mixed datatypes
    my_tuple = (1, "Hello", 3.4)
    print(my_tuple)  # Output: (1, "Hello", 3.4)  

    # nested tuple
    my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

    # Output: ("mouse", [8, 4, 6], (1, 2, 3)) 
    print(my_tuple)
```

A tuple can also be created without using parentheses. This is known as tuple packing.

```py
    my_tuple = 3, 4.6, "dog"
    print(my_tuple)   # Output: 3, 4.6, "dog" 

    # tuple unpacking is also possible
    a, b, c = my_tuple

    print(a)      # 3
    print(b)      # 4.6 
    print(c)      # dog 
```
Creating a tuple with one element is a bit tricky.

Having one element within parentheses is not enough. We will need a trailing comma to indicate that it is, in fact, a tuple.

```py
    my_tuple = ("hello")
    print(type(my_tuple))  # <class 'str'>

    # Creating a tuple having one element
    my_tuple = ("hello",)  
    print(type(my_tuple))  # <class 'tuple'> 

    # Parentheses is optional
    my_tuple = "hello",
    print(type(my_tuple))  # <class 'tuple'> 
```

## Access Tuple Elements

There are various ways in which we can access the elements of a tuple.
### 1. Indexing

We can use the index operator [] to access an item in a tuple where the index starts from 0.

So, a tuple having 6 elements will have indices from 0 to 5. Trying to access an element outside of tuple (for example, 6, 7,...) will raise an IndexError.

The index must be an integer; so we cannot use float or other types. This will result in TypeError.

Likewise, nested tuples are accessed using nested indexing, as shown in the example below.

```py
    my_tuple = ('p','e','r','m','i','t')

    print(my_tuple[0])   # 'p' 
    print(my_tuple[5])   # 't'

    # IndexError: list index out of range
    # print(my_tuple[6])

    # Index must be an integer
    # TypeError: list indices must be integers, not float
    # my_tuple[2.0]

    # nested tuple
    n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

    # nested index
    print(n_tuple[0][3])       # 's'
    print(n_tuple[1][1])       # 4
```

### 2. Negative Indexing

Python allows negative indexing for its sequences.

The index of -1 refers to the last item, -2 to the second last item and so on.

```py
    my_tuple = ('p','e','r','m','i','t')

    # Output: 't'
    print(my_tuple[-1])

    # Output: 'p'
    print(my_tuple[-6])
```

### 3. Slicing

We can access a range of items in a tuple by using the slicing operator - colon ":".

```py
    my_tuple = ('p','y','t','h','o','n',' ','c','o','u','r','s','e')

    # elements 2nd to 4th
    # Output: ('r', 'o', 'g')
    print(my_tuple[1:4])

    # elements beginning to 2nd
    # Output: ('p', 'r')
    print(my_tuple[:-7])

    # elements 8th to end
    # Output: ('i', 'z')
    print(my_tuple[7:])

    # elements beginning to end
    # Output: ('p','y','t','h','o','n',' ','c','o','u','r','s','e')
    print(my_tuple[:])
```

Slicing can be best visualized by considering the index to be between the elements as shown below. So if we want to access a range, we need the index that will slice the portion from the tuple.


## Changing a Tuple

Unlike lists, tuples are immutable.

This means that elements of a tuple cannot be changed once it has been assigned. But, if the element is itself a mutable datatype like list, its nested items can be changed.

We can also assign a tuple to different values (reassignment).

```py
my_tuple = (4, 2, 3, [6, 5])


# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 9

# However, item of mutable element can be changed
my_tuple[3][0] = 9    # Output: (4, 2, 3, [9, 5])
print(my_tuple)

# Tuples can be reassigned
my_tuple = ('p','y','t','h','o','n',' ','c','o','u','r','s','e')

# Output: ('p','y','t','h','o','n',' ','c','o','u','r','s','e')
print(my_tuple)
```

We can use + operator to combine two tuples. This is also called concatenation.

We can also repeat the elements in a tuple for a given number of times using the * operator.

Both + and * operations result in a new tuple.

```py
# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)
```

### Deleting a Tuple

As discussed above, we cannot change the elements in a tuple. That also means we cannot delete or remove items from a tuple.

But deleting a tuple entirely is possible using the keyword del.

```py
my_tuple = ('p','y','t','h','o','n',' ','c','o','u','r','s','e')

# can't delete items
# TypeError: 'tuple' object doesn't support item deletion
# del my_tuple[3]

# Can delete an entire tuple
del my_tuple

# NameError: name 'my_tuple' is not defined
print(my_tuple)
```

## Tuple Methods

Methods that add items or remove items are not available with tuple. Only the following two methods are available.

### Python Tuple Method

Method | Description
------ | -----------
count(x) | Returns the number of items x
index(x) | Returns the index of the first item that is equal to x

Some examples of Python tuple methods:

```py
my_tuple = ('a','p','p','l','e',)

print(my_tuple.count('p'))  # Output: 2
print(my_tuple.index('l'))  # Output: 3
```

## Other Tuple Operations

### 1. Tuple Membership Test

We can test if an item exists in a tuple or not, using the keyword in.

```py
my_tuple = ('a','p','p','l','e',)

# In operation
# Output: True
print('a' in my_tuple)

# Output: False
print('b' in my_tuple)

# Not in operation
# Output: True
print('g' not in my_tuple)
```

### 2. Iterating Through a Tuple

Using a for loop we can iterate through each item in a tuple.

```py
# Output: 
# Hello John
# Hello Kate
for name in ('John','Kate'):
     print("Hello",name)
```

## Advantages of Tuple over List

Since tuples are quite similar to lists, both of them are used in similar situations as well.

However, there are certain advantages of implementing a tuple over a list. Below listed are some of the main advantages:

* We generally use tuple for heterogeneous (different) datatypes and list for homogeneous (similar) datatypes.
* Since tuples are immutable, iterating through tuple is faster than with list. So there is a slight performance boost.
* Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
* If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

---

# Python Sets

## What is a set in Python?

A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed). However, the set itself is mutable. We can add or remove items from it. Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.

## How to create a set?

A set is created by placing all the items (elements) inside curly braces {}, separated by comma or by using the built-in function set().
It can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have a mutable element, like list, set or dictionary, as its element.

```py
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)
```

Try the following examples as well.

```py
# set do not have duplicates
# Output: {1, 2, 3, 4}
my_set = {1,2,3,4,3,2}
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# If you uncomment line #12,
# this will cause an error.
# TypeError: unhashable type: 'list'

#my_set = {1, 2, [3, 4]}

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1,2,3,2])
print(my_set)
```

Creating an empty set is a bit tricky.

Empty curly braces {} will make an empty dictionary in Python. To make a set without any elements we use the set() function without any argument.

```py
# initialize a with {}
a = {}

# check data type of a
# Output: <class 'dict'>
print(type(a))

# initialize a with set()
a = set()

# check data type of a
# Output: <class 'set'>
print(type(a))
```

## How to change a set in Python?

Sets are mutable. But since they are unordered, indexing have no meaning.
We cannot access or change an element of set using indexing or slicing. Set does not support it.
We can add single element using the add() method and multiple elements using the update() method. The update() method can take tuples, lists, strings or other sets as its argument. In all cases, duplicates are avoided.

```py
# initialize my_set
my_set = {1,3}
print(my_set)

# if you uncomment line 9,
# you will get an error
# TypeError: 'set' object does not support indexing

#my_set[0]

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2,3,4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4,5], {1,6,8})
print(my_set)
```

## How to remove elements from a set?

A particular item can be removed from set using methods, discard() and remove().

The only difference between the two is that, while using discard() if the item does not exist in the set, it remains unchanged. But remove() will raise an error in such condition.

The following example will illustrate this.

```py
# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# If you uncomment line 27,
# you will get an error.
# Output: KeyError: 2

#my_set.remove(2)
```

Similarly, we can remove and return an item using the pop() method.

Set being unordered, there is no way of determining which item will be popped. It is completely arbitrary.

We can also remove all items from a set using clear().

```py
# initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# pop another element
# Output: random element
my_set.pop()
print(my_set)

# clear my_set
#Output: set()
my_set.clear()
print(my_set)
```

## Python Set Operations

Sets can be used to carry out mathematical set operations like union, intersection, difference and symmetric difference. We can do this with operators or methods.

Let us consider the following two sets for the following operations.

```py
    >>> A = {1, 2, 3, 4, 5}
    >>> B = {4, 5, 6, 7, 8}
```

## Different Python Set Methods

There are many set methods, some of which we have already used above. Here is a list of all the methods that are available with set objects.
Python Set Methods 
Method |	Description
------ |    -----------
add() |	Adds an element to the set
clear() |	Removes all elements from the set
copy() |	Returns a copy of the set
difference() |	Returns the difference of two or more sets as a new set
difference_update() |	Removes all elements of another set from this set
discard() |	Removes an element from the set if it is a member. (Do nothing if the element is not in set)
intersection() |	Returns the intersection of two sets as a new set
intersection_update() |	Updates the set with the intersection of itself and another
isdisjoint() |	Returns True if two sets have a null intersection
issubset() |	Returns True if another set contains this set
issuperset() |	Returns True if this set contains another set
pop() |	Removes and returns an arbitary set element. Raise KeyError if the set is empty
remove() |	Removes an element from the set. If the element is not a member, raise a KeyError
symmetric_difference() |	Returns the symmetric difference of two sets as a new set
symmetric_difference_update() |	Updates a set with the symmetric difference of itself and another
union() |	Returns the union of sets in a new set
update() |	Updates the set with the union of itself and others

## Other Set Operations

### Set Membership Test

We can test if an item exists in a set or not, using the keyword in.

```py
# initialize my_set
my_set = set("apple")

# check if 'a' is present
# Output: True
print('a' in my_set)

# check if 'p' is present
# Output: False
print('p' not in my_set)
```

## Iterating Through a Set

Using a for loop, we can iterate though each item in a set.

```py
    >>> for letter in set("apple"):
    ...     print(letter)
    ...    
    a
    p
    e
    l
```

## Built-in Functions with Set

Built-in functions like all(), any(), enumerate(), len(), max(), min(), sorted(), sum() etc. are commonly used with set to perform different tasks.
Built-in Functions with Set
Function |	Description
-------- |  ------------
all() |	Return True if all elements of the set are true (or if the set is empty).
any() |	Return True if any element of the set is true. If the set is empty, return False.
enumerate() |	Return an enumerate object. It contains the index and value of all the items of set as a pair.
len() |	Return the length (the number of items) in the set.
max() |	Return the largest item in the set.
min() |	Return the smallest item in the set.
sorted() |	Return a new sorted list from elements in the set(does not sort the set itself).
sum() |	Retrun the sum of all elements in the set.

---

# Python Frozenset

Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. While tuples are immutable lists, frozensets are immutable sets.
Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are hashable and can be used as keys to a dictionary.

Frozensets can be created using the function frozenset().

This datatype supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), symmetric_difference() and union(). Being immutable it does not have method that add or remove elements.

```py
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
```

Try these examples on Python shell.

```py
    >>> A.isdisjoint(B)
    False
    >>> A.difference(B)
    frozenset({1, 2})
    >>> A | B
    frozenset({1, 2, 3, 4, 5, 6})
    >>> A.add(3)
    ...
    AttributeError: 'frozenset' object has no attribute 'add'
```

---

# Python Dictionary

Python dictionary is an unordered collection of items. While other compound data types have only value as an element, a dictionary has a **key: value** pair.

Dictionaries are optimized to retrieve values when the key is known.
## How to create a dictionary?

Creating a dictionary is as simple as placing items inside curly braces {} separated by comma.
An item has a key and the corresponding value expressed as a pair, **key: value**.
While values can be of any data type and can repeat, keys must be of immutable type (string, number or tuple with immutable elements) and must be unique.

```py
# empty dictionary
my_dict = {}
# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
# using dict()
my_dict = dict({1:'apple', 2:'ball'})
# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
```

As you can see above, we can also create a dictionary using the built-in function dict().

## How to access elements from a dictionary?

While indexing is used with other container types to access values, dictionary uses keys. Key can be used either inside square brackets or with the get() method.
The difference while using get() is that it returns None instead of KeyError, if the key is not found.
```py
my_dict = {'name':'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# my_dict.get('address')
# my_dict['address']
```

## How to change or add elements in a dictionary?

Dictionary are mutable. We can add new items or change the value of existing items using assignment operator.
If the key is already present, value gets updated, else a new key: value pair is added to the dictionary.

```py
my_dict = {'name':'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'  

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)
```

## How to delete or remove elements from a dictionary?

We can remove a particular item in a dictionary by using the method pop(). This method removes as item with the provided key and returns the value.
The method, popitem() can be used to remove and return an arbitrary item (key, value) form the dictionary. All the items can be removed at once using the clear() method.
We can also use the del keyword to remove individual items or the entire dictionary itself.

```py
# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}  

# remove a particular item
# Output: 16
print(squares.pop(4))  

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item
# Output: (1, 1)
print(squares.popitem())

# Output: {2: 4, 3: 9, 5: 25}
print(squares)

# delete a particular item
del squares[5]  

# Output: {2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# Throws Error
# print(squares)
```

## Python Dictionary Methods

Methods that are available with dictionary are tabulated below. Some of them have already been used in the above examples.
Python Dictionary Methods 
Method |	Description
------ |    ----------
clear() |	Remove all items form the dictionary.
copy() |	Return a shallow copy of the dictionary.
fromkeys(seq[, v]) |	Return a new dictionary with keys from seq and value equal to v (defaults to None).
get(key[,d]) |	Return the value of key. If key doesnot exit, return d (defaults to None).
items() |	Return a new view of the dictionary's items (key, value).
keys() |	Return a new view of the dictionary's keys.
pop(key[,d]) |	Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises KeyError.
popitem() |	Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty.
setdefault(key[,d]) |	If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None).
update([other]) |	Update the dictionary with the key/value pairs from other, overwriting existing keys.
values() |	Return a new view of the dictionary's values

Here are a few example use of these methods.

```py
marks = {}.fromkeys(['Math','English','Science'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
print(marks)

for item in marks.items():
    print(item)

# Output: ['English', 'Math', 'Science']
list(sorted(marks.keys()))
```

