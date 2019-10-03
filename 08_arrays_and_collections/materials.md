<center> Collections </center>
===

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


---
# Python Loops

## Python for Loop

### What is for loop in Python?

The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.
Syntax of for Loop

```py
for val in sequence:
	Body of for
```

Here, val is the variable that takes the value of the item inside the sequence on each iteration.
Loop continues until we reach the last item in the sequence. The body of for loop is separated from the rest of the code using indentation.

#### Example: Python for Loop

```py
# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

# Output: The sum is 48
print("The sum is", sum)
```

### The range() function

We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers).
We can also define the start, stop and step size as range(start,stop,step size). step size defaults to 1 if not provided.
This function does not store all the values in memory, it would be inefficient. So it remembers the start, stop, step size and generates the next number on the go.
To force this function to output all the items, we can use the function list().
The following example will clarify this.

```py
# Output: range(0, 10)
print(range(10))

# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))

# Output: [2, 3, 4, 5, 6, 7]
print(list(range(2, 8)))

# Output: [2, 5, 8, 11, 14, 17]
print(list(range(2, 20, 3)))
```

We can use the range() function in for loops to iterate through a sequence of numbers. It can be combined with the len() function to iterate though a sequence using indexing. Here is an example.

```py
# Program to iterate through a list using indexing

genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genre)):
	print("I like", genre[i])
```

When you run the program, the output will be:

```txt
I like pop
I like rock
​I like jazz
```

## for loop with else

A for loop can have an optional **else** block as well. The else part is executed if the items in the sequence used in for loop exhausts.
**break** statement can be used to stop a for loop. In such case, the else part is ignored.
Hence, a for loop's else part runs if no break occurs.
Here is an example to illustrate this.

```py
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

```

When you run the program, the output will be:

```txt
0
1
5
No items left.
```

Here, the for loop prints items of the list until the loop exhausts. When the for loop exhausts, it executes the block of code in the else and prints

```txt
No items left.
```

---

## Python while Loop

### What is while loop in Python?

The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
We generally use this loop when we don't know beforehand, the number of times to iterate.

Syntax of while Loop in Python:

```py
while test_expression:
    Body of while
```

In while loop, test expression is checked first. The body of the loop is entered only if the test_expression evaluates to True. After one iteration, the test expression is checked again. This process continues until the test_expression evaluates to False.

In Python, the body of the while loop is determined through indentation.
Body starts with indentation and the first unindented line marks the end.
Python interprets any non-zero value as True. None and 0 are interpreted as False

```py
# Program to add natural
# numbers upto 
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)
```

When you run the program, the output will be:

```txt
Enter n: 10
The sum is 55
```
In the above program, the test expression will be True as long as our counter variable i is less than or equal to n.

We need to increase the value of counter variable in the body of the loop. This is very important. Failing to do so will result in an infinite loop (loop that goes on forever).

Finally the result is displayed


### while loop with else

Same as that of for loop, we can have an optional else block with while loop as well.
The **else** part is executed if the condition in the while loop evaluates to False.
The while loop can be terminated with a break statement. In such case, the else part is ignored. Hence, a while loop's else part runs if no break occurs and the condition is false.
Here is an example to illustrate this.
```py
# Example to illustrate
# the use of else statement
# with the while loop

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")
```

Output

```txt
Inside loop
Inside loop
Inside loop
Inside else
```

Here, we use a counter variable to print the string Inside loop three times.
On the forth iteration, the condition in while becomes False. Hence, the else part is executed

---
# Python break and continue

## What is the use of break and continue in Python?

In Python, break and continue statements can alter the flow of a normal loop.
Loops iterate over a block of code until test expression is false, but sometimes we wish to terminate the current iteration or even the whole loop without checking test expression.
The **break** and **continue** statements are used in these cases.

### Python break statement

The **break** statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.
If break statement is inside a nested loop (loop inside another loop), break will terminate the innermost loop.
Syntax of break

```py
break
```
Example: Python break
```py
for val in "string":
    if val == "i":
        break
    print(val)

print("The end")
```

Output
```txt
s
t
r
The end
```

In this program, we iterate through the "string" sequence. We check if the letter is "i", upon which we break from the loop. Hence, we see in our output that all the letters up till "i" gets printed. After that, the loop terminates.

### Python continue statement

The **continue** statement is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.
Syntax of Continue

```py
continue
```

Example: Python continue

```py
for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")
```

Output
```txt
s
t
r
n
g
The end
```

This program is same as the above example except the break statement has been replaced with continue.
We continue with the loop, if the string is "i", not executing the rest of the block. Hence, we see in our output that all the letters except "i" gets printed.

---

# Python pass statement

## What is pass statement in Python?

In Python programming, pass is a null statement. The difference between a comment and pass statement in Python is that, while the interpreter ignores a comment entirely, pass is not ignored.

However, nothing happens when pass is executed. It results into no operation (NOP).
Syntax of pass

```py
pass
```

We generally use it as a placeholder.

Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. They cannot have an empty body. The interpreter would complain. So, we use the pass statement to construct a body that does nothing.

```py
# pass is just a placeholder for
# functionality to be added later.
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass
```



---

# Python Arrays

In programming, an array is a collection of elements of the same type.
Arrays are popular in most programming languages like Java, C/C++, JavaScript and so on. However, in Python, they are not that common. When people talk about Python arrays, more often than not, they are talking about Python lists. If you don't know what lists are, you should definitely check Python list article.

That being said, array of numeric values are supported in Python by the array module.

## Python Lists Vs array Module as Arrays

We can treat lists as arrays. However, we cannot constrain the type of elements stored in a list. For example:

```py
    a = [1, 3.5, "Hello"] 
```

If you create arrays using the array module, all elements of the array must be of the same numeric type.

```py
import array as arr
a = arr.array('d', [1, 3.5, "Hello"])   // Error
```

### How to create arrays?

As you might have guessed from the above example, we need to import array module to create arrays. For example:

```py
    import array as arr
    a = arr.array('d', [1.1, 3.5, 4.5])
    print(a)
```

Here, we created an array of float type. The letter 'd' is a type code. This determines the type of the array during creation.
Commonly used type codes:

Code | C Type | Python Type | Min bytes
---- | ------ | ---------- | --------
'b' | signed char | int | 1
'B' | unsigned char | int | 1
'u' | Py_UNICODE | Unicode | 2
'h' | signed short | int | 2
'H' | unsigned short | int | 2
'i' | signed int | int | 2
'I' | unsigned int | int | 2
'l' | signed long | int | 4
'L' | unsigned long | int | 4
'f' | float | float | 4
'd' | double | float | 8

We will not discuss about different C types in this article. We will use two type codes in this entire article: 'i' for integers and 'd' for floats.

**Note:** The 'u' type code for Unicode characters is deprecated since version 3.3. Avoid using it when possible.

### How to access array elements?

We use indices to access elements of an array:

```py
    import array as arr
    a = arr.array('i', [2, 4, 6, 8])
    print("First element:", a[0])
    print("Second element:", a[1])
    print("Last element:", a[-1])
```

Remember, the index starts from 0 (not 1) similar to lists.

### How to slice arrays?

We can access a range of items in an array by using the slicing operator :.

```py
    import array as arr
    numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
    numbers_array = arr.array('i', numbers_list)
    print(numbers_array[2:5]) # 3rd to 5th
    print(numbers_array[:-5]) # beginning to 4th
    print(numbers_array[5:])  # 6th to end
    print(numbers_array[:])   # beginning to end
```

When you run the program, the output will be:

```txt
array('i', [62, 5, 42])
array('i', [2, 5, 62])
array('i', [52, 48, 5])
array('i', [2, 5, 62, 5, 42, 52, 48, 5])
```

### How to change or add elements?

Arrays are mutable; their elements can be changed in a similar way like lists.

```py
    import array as arr
    numbers = arr.array('i', [1, 2, 3, 5, 7, 10])
    # changing first element
    numbers[0] = 0    
    print(numbers)     # Output: array('i', [0, 2, 3, 5, 7, 10])
    # changing 3rd to 5th element
    numbers[2:5] = arr.array('i', [4, 6, 8])   
    print(numbers)     # Output: array('i', [0, 2, 4, 6, 8, 10])
```

We can add one item to a list using the append() method, or add several items using extend() method.

```py
    import array as arr
    numbers = arr.array('i', [1, 2, 3])
    numbers.append(4)
    print(numbers)     # Output: array('i', [1, 2, 3, 4])
    # extend() appends iterable to the end of the array
    numbers.extend([5, 6, 7]) 
    print(numbers)     # Output: array('i', [1, 2, 3, 4, 5, 6, 7])
```

We can concatenate two arrays using + operator.

```py
    import array as arr
    odd = arr.array('i', [1, 3, 5])
    even = arr.array('i', [2, 4, 6])
    numbers = arr.array('i')   # creating empty array of integer
    numbers = odd + even
    print(numbers)    
```

### How to remove/delete elements?

We can delete one or more items from an array using Python's del statement.

```py
    import array as arr
    number = arr.array('i', [1, 2, 3, 3, 4])
    del number[2] # removing third element
    print(number) # Output: array('i', [1, 2, 3, 4])
    del number # deleting entire array
    print(number) # Error: array is not defined
```

We can use the remove() method to remove the given item, and pop() method to remove an item at the given index.

```py
    import array as arr
    numbers = arr.array('i', [10, 11, 12, 12, 13])
    numbers.remove(12)
    print(numbers)   # Output: array('i', [10, 11, 12, 13])
    print(numbers.pop(2))   # Output: 12
    print(numbers)   # Output: array('i', [10, 11, 13])
```

Check this page to learn more about Python array and array methods:

### When to use arrays?

Lists are much more flexible than arrays. They can store elements of different data types including string. Also, lists are faster than arrays. And, if you need to do mathematical computation on arrays and matrices, you are much better off using something like NumPy library.

Unless you don't really need arrays (array module may be needed to interface with C code), don't use them.
