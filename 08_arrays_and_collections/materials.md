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
