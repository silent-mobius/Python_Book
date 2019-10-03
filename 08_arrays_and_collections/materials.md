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

Note: The 'u' type code for Unicode characters is deprecated since version 3.3. Avoid using it when possible.
How to access array elements?

We use indices to access elements of an array:

    import array as arr
    a = arr.array('i', [2, 4, 6, 8])
    print("First element:", a[0])
    print("Second element:", a[1])
    print("Last element:", a[-1])

Remember, the index starts from 0 (not 1) similar to lists.
How to slice arrays?

We can access a range of items in an array by using the slicing operator :.

    import array as arr
    numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
    numbers_array = arr.array('i', numbers_list)
    print(numbers_array[2:5]) # 3rd to 5th
    print(numbers_array[:-5]) # beginning to 4th
    print(numbers_array[5:])  # 6th to end
    print(numbers_array[:])   # beginning to end

When you run the program, the output will be:

array('i', [62, 5, 42])
array('i', [2, 5, 62])
array('i', [52, 48, 5])
array('i', [2, 5, 62, 5, 42, 52, 48, 5])

How to change or add elements?

Arrays are mutable; their elements can be changed in a similar way like lists.

    import array as arr
    numbers = arr.array('i', [1, 2, 3, 5, 7, 10])
    # changing first element
    numbers[0] = 0    
    print(numbers)     # Output: array('i', [0, 2, 3, 5, 7, 10])
    # changing 3rd to 5th element
    numbers[2:5] = arr.array('i', [4, 6, 8])   
    print(numbers)     # Output: array('i', [0, 2, 4, 6, 8, 10])

We can add one item to a list using the append() method, or add several items using extend() method.

    import array as arr
    numbers = arr.array('i', [1, 2, 3])
    numbers.append(4)
    print(numbers)     # Output: array('i', [1, 2, 3, 4])
    # extend() appends iterable to the end of the array
    numbers.extend([5, 6, 7]) 
    print(numbers)     # Output: array('i', [1, 2, 3, 4, 5, 6, 7])

We can concatenate two arrays using + operator.

    import array as arr
    odd = arr.array('i', [1, 3, 5])
    even = arr.array('i', [2, 4, 6])
    numbers = arr.array('i')   # creating empty array of integer
    numbers = odd + even
    print(numbers)    

How to remove/delete elements?

We can delete one or more items from an array using Python's del statement.

    import array as arr
    number = arr.array('i', [1, 2, 3, 3, 4])
    del number[2] # removing third element
    print(number) # Output: array('i', [1, 2, 3, 4])
    del number # deleting entire array
    print(number) # Error: array is not defined

We can use the remove() method to remove the given item, and pop() method to remove an item at the given index.

    import array as arr
    numbers = arr.array('i', [10, 11, 12, 12, 13])
    numbers.remove(12)
    print(numbers)   # Output: array('i', [10, 11, 12, 13])
    print(numbers.pop(2))   # Output: 12
    print(numbers)   # Output: array('i', [10, 11, 13])

Check this page to learn more about Python array and array methods:
When to use arrays?

Lists are much more flexible than arrays. They can store elements of different data types including string. Also, lists are faster than arrays. And, if you need to do mathematical computation on arrays and matrices, you are much better off using something like NumPy library.

Unless you don't really need arrays (array module may be needed to interface with C code), don't use them.
