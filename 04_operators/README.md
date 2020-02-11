# Python Operators

## What are operators in python?

Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.

For example:
```py
>>> 2+3
5
```

Here, + is the operator that performs addition. 2 and 3 are the operands and 5 is the output of the operation.

### Arithmetic operators

Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication etc.

Operator | Meaning | Example
--------| -------- | ---------
+ | Add two operands or unary plus 	| x + y  +2
- |	Subtract right operand from the left or unary minus | x - y -2
* |	Multiply two operands |	x * y
/ |	Divide left operand by the right one (always results into float) | x / y
% |	Modulus - remainder of the division of left operand by the right | x % y (remainder of x/y)
// | Floor division - division that results into whole number adjusted to the left in the number line | x // y
** | Exponent - left operand raised to the power of right | x**y (x to the power y)

#### Example : Arithmetic operators in Python
``` py
x = 15
y = 4
# Output: x + y = 19
print('x + y =',x+y)
# Output: x - y = 11
print('x - y =',x-y)
# Output: x * y = 60
print('x * y =',x*y)
# Output: x / y = 3.75
print('x / y =',x/y)
# Output: x // y = 3
print('x // y =',x//y)
# Output: x ** y = 50625
print('x ** y =',x**y)
```

When you run the program, the output will be:
```py 
x + y = 19
x - y = 11
x * y = 60
x / y = 3.75
x // y = 3
x ** y = 50625
```
### Comparison operators

Comparison operators are used to compare values. It either returns True or False according to the condition.


Operator | Meaning | Example
-------- | ------- | ------- 
> |	Greater that - True if left operand is greater than the right | x > y
< |	Less that - True if left operand is less than the right | x < y
== |	Equal to - True if both operands are equal 	| x == y
!= |	Not equal to - True if operands are not equal |	x != y
>= |	Greater than or equal to - True if left operand is greater than or equal to the right |	x >= y
<= |	Less than or equal to - True if left operand is less than or equal to the right | x <= y

Example : Comparison operators in Python

```py
x = 10
y = 12
# Output: x > y is False
print('x > y  is',x>y)
# Output: x < y is True
print('x < y  is',x<y)
# Output: x == y is False
print('x == y is',x==y)
# Output: x != y is True
print('x != y is',x!=y)
# Output: x >= y is False
print('x >= y is',x>=y)
# Output: x <= y is True
print('x <= y is',x<=y)
```

### Logical operators

Logical operators are the `and`, `or`, `not` operators.

> Something to remember: If `variable` has a value of `1` in it, then its boolean value it *_True_*, In any other case the boolean value is *_False_*. 
> If value is not defined, then python3 will give you *_NameError_*,

Operator | Meaning | Example
------- | -------- | ----------
and |	True if both the operands are true |	x and y
or 	|   True if either of the operands is true 	| x or y
not | 	True if operand is false (complements the operand) | not x

Example : Logical Operators in Python3

```py
x = True
y = False
# Output: x and y is False
print('x and y is',x and y)
# Output: x or y is True
print('x or y is',x or y)
# Output: not x is False
print('not x is',not x)
```


The truth table for and is given below:

#### The truth table for *_and_* operator

A |	B |	A and B
-- \| -- | --- 
True |	True |	True
True |	False |	False
False |	True |	False
False |	False |	False

####  The truth table for *_or_* operator is given below:

A |	B |	A or B
-- | -- | ---
True | True | True
True | False | True
False | True | True
False | False | False

#### The truth table for *_not_* is given below:

A |	not A
-- | --
True |	False
False |	True

some example of their usage are given below
```py
>>> True and False
False
>>> True or False
True
>>> not False
True
```

### Bitwise operators

Before getting it to this subject, one must first understand several things:
- __binary number__ is a number expressed in the base-2 numeral system or binary numeral system, which uses only two symbols: typically "0" (zero) and "1" (one). 
- __ASCII code__ or  short name for 'The American Standard Code for Information Interchange' uses a 7-bit binary code to represent text and other characters within computers, communications equipment, and other devices. Each letter or symbol is assigned a number from 0 to 127. For example, lowercase "a" is represented by 1100001 as a bit string (which is "97" in decimal).
- __a bitwise operation__ operates on one or more bit patterns or binary numerals at the level of their individual bits. It is a fast and simple action, directly supported by the processor, and is used to manipulate values for comparisons and calculations. 

for more info please read [here](https://en.wikipedia.org/wiki/Binary)

Bitwise operators act on operands as if they were string of binary digits. It operates bit by bit, hence the name.

For example, 2 is 10 in binary and 7 is 111.

In the table below: Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)

Bitwise operators in Python 
Operator | Meaning | What Does It Do? | Example
-------  | ------  | ------------     | --------
& |	Bitwise AND | Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0. 	| x & y = 0 (0000 0000)
\||	Bitwise OR 	| Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.| x \| y = 14 (0000 1110)
>> | Bitwise right shift | Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y. 	| x >> 2 = 2 (0000 0010)
<< | Bitwise left shift  | Returns x with the bits shifted to the right by y places. This is the same as multiplying x by 2**y. 
x	| x << 2 = 40 (0010 1000)
~ |	Bitwise NOT | Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1.| ~x = -11 (1111 0101)
^ |	Bitwise XOR | Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1. | x ^ y = 14 (0000 1110)




<!-- TODO : add descripttion and examples for the bitwise operators-->





### Assignment operators

Assignment operators are used in Python to assign values to variables.

a = 5 is a simple assignment operator that assigns the value 5 on the right to the variable a on the left.

There are various compound operators in Python like a += 5 that adds to the variable and later assigns the same. It is equivalent to a = a + 5.

Assignment operators in Python 

Operator |	Example |	Equivatent to
-------  | ------- | ---------------
= |	x = 5 |	x = 5
+= |	x += 5 |	x = x + 5
-= |	x -= 5 |	x = x - 5
*= |	x *= 5 |	x = x * 5
/= |	x /= 5 |	x = x / 5
%= |	x %= 5 |	x = x % 5
//= |	x //= 5 |	x = x // 5
**= |	x **= 5 | 	x = x ** 5
&= |	x &= 5 |	x = x & 5
|= |	x |= 5 |	x = x | 5
^= |	x ^= 5 |	x = x ^ 5
>>= |	x >>= 5 |	x = x >> 5
<<= |	x <<= 5 |	x = x << 5

### Identity operators

Python language offers some special type of operators like the identity operator or the membership operator. They are described below with examples.
Identity operators

is and is not are the identity operators in Python. They are used to check if two values (or variables) are located on the same part of the memory. Two variables that are equal does not imply that they are identical.


Identity operators in Python 

Operator |	Meaning |	Example
------- | ------- | ---------
is |	True if the operands are identical (refer to the same object)  |	x is True
is not 	| True if the operands are not identical (do not refer to the same object) |	x is not True

Example : Identity operators in Python
``` py
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1) # Output: False

print(x2 is y2)     # Output: True

print(x3 is y3)    # Output: False

```

Here, we see that x1 and y1 are integers of same values, so they are equal as well as identical. Same is the case with x2 and y2 (strings).

But x3 and y3 are list. They are equal but not identical. It is because interpreter locates them separately in memory although they are equal.


### Membership operators

in and not in are the membership operators in Python. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).

In a dictionary we can only test for presence of key, not the value.
Operator | 	Meaning |	Example
------- | --------- | ----------
in |	True if value/variable is found in the sequence |	5 in x
not in |	True if value/variable is not found in the sequence |	5 not in x

Example : Membership operators in Python
```py
x = 'Hello world'
y = {1:'a',2:'b'}
# Output: True
print('H' in x)
# Output: True
print('hello' not in x)
# Output: True
print(1 in y)
# Output: False
print('a' in y)
```
Here, 'H' is in x but 'hello' is not present in x (remember, Python is case sensitive). Similary, 1 is key and 'a' is the value in dictionary y. Hence, 'a' in y returns False.

[back to top](#arithmetic-operators)
Or
[back to main](../README.md)