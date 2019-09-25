# Python Variables

### Creating Variables
Variables are containers for storing data values.
Unlike other programming languages, Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
```python3
x = 7
y = "Alex "
print(x)
print(y)
```
Variables do not need to be declared with any particular type and can even change type after they have been set.

```python3
x = 4 # x is of type int
x = "rhcp" # x is now of type str
print(x)
```

String variables can be declared either by using single or double quotes:
```python3
x = "John"
# is the same as
x = 'John'
```

### Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
*   A variable name must start with a letter or the underscore character
*   A variable name cannot start with a number
*   A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
*   Variable names are case-sensitive (age, Age and AGE are three different variables)

> **Remember that variable names are case-sensitive**


### Assign Value to Multiple Variables

Python allows you to assign values to multiple variables in one line:
```python3
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```
And you can assign the same value to multiple variables in one line:
```python3
x = y = z = "Orange"
print(x)
print(y)
print(z)
```

### Output Variables

The Python print statement is often used to output variables.
To combine both text and a variable, Python uses the + character:
```
x = "awesome"
print("Python is " + x)
```
You can also use the + character to add a variable to another variable:
```
x = "Python is "
y = "awesome"
z =  x + y
print(z)
```
For numbers, the + character works as a mathematical operator:
```
x = 5
y = 10
print(x + y)
```
If you try to combine a string and a number, Python will give you an error:
```
x = 5
y = "John"
print(x + y)
```

---
---

### Somewhat Advanced
### Random Number

Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

Import the random module, and display a random number between 1 and 9:
import random

print(random.randrange(1,10))
In our Random Module Reference you will learn more about the Random module.

---

## Some What Advanced
### Global Variables

Variables that are created outside of a function (as in all of the s above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.


Create a variable outside of a function, and use it inside the function
```
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
```
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
Create a variable inside a function, with the same name as the global variable

```x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
```

### The global Keyword

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
If you use the global keyword, the variable belongs to the global scope:
```
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```
Also, use the global keyword if you want to change a global variable inside a function.
To change the value of a global variable inside a function, refer to the variable by using the global keyword:
```
x = "awesome"
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```
