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

Logical operators

Logical operators are the and, or, not operators.

Operator | Meaning | Example
------- | -------- | ----------
and |	True if both the operands are true |	x and y
or 	|   True if either of the operands is true 	| x or y
not | 	True if operand is false (complements the operand) | not x

Example : Logical Operators in Python
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
### Truth table for and 

A |	B |	A and B
-- | -- | --- 
True |	True |	True
True |	False |	False
False |	True |	False
False |	False |	False

###  The truth table for or is given below:

Truth table for or
A |	B |	A or B
-- | -- | ---
True | True | True
True | False | True
False | True | True
False | False | False

### The truth table for not is given below:

Truth tabel for not 
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