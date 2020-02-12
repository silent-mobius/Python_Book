# Python Variables

### Creating Variables

In computer programming, __a `variable` or `scalar` is a storage address (identified by a memory address) paired with an associated symbolic name, which contains some known or unknown quantity of information referred to as a value__. The variable name is the usual way to reference the stored value, in addition to referring to the variable itself, depending on the context.(Essentially, variables are containers for storing data values.) This separation of name and content allows the name to be used independently of the exact information it represents. The identifier in computer source code can be bound to a value during run time, and the value of the variable may thus change during the course of program execution.

As an a example, here is a C language code: (it's fine if you don't know what it means, you have explanation below)

```c

int main(*arg,**kwarg){

  int var;
  float foo;
  var = 3;
  foo = 4.6;

    printf("%d\n %f",var,foo);

return 0;
}

```
It declares variables `var` of type __int__ and `foo` of type __float__. Then the values of 3 and 4.6 are assingned to them respectively. Later we print them to standard output . at the end we exit the main code with `return 0`, meaning that code has been executed successfully and program if finished running.

Unlike C programming languages, Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.

```py
x = 7
y = "Alex "
print(x)
print(y)
```

Variables do not need to be declared with any particular type and can even change type after they have been set.

```py
x = 4 # x is of type int
x = "rhcp" # x is now of type str
print(x)
```

String variables can be declared either by using single or double quotes:

```py
x = "John"
# is the same as
x = 'John'
```

### Variable Names

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
- Variable name must start with a letter or the underscore character.
- Variable name cannot start with a number.
- Variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
- Variable names are case-sensitive (age, Age and AGE are three different variables)

> **Remember that variable names are case-sensitive**

### Assign Value to Multiple Variables

Python allows you to assign values to multiple variables in one line:

```py
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```

And you can assign the same value to multiple variables in one line:

```py
x = y = z = "Orange"
print(x)
print(y)
print(z)
```

### Output Variables

The Python print statement is often used to output variables.
To combine both text and a variable, Python uses the + character:

```py
x = "awesome"
print("Python is " + x)
```

You can also use the + character to add a variable to another variable:

```py
x = "Python is "
y = "awesome"
z =  x + y
print(z)
```

For numbers, the + character works as a mathematical operator:
```py
x = 5
y = 10
print(x + y)
```

If you try to combine a string and a number, Python will give you an error:

```py
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

```py
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
```

If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
Create a variable inside a function, with the same name as the global variable

```py
x = "awesome"

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

```py
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```
Also, use the global keyword if you want to change a global variable inside a function.
To change the value of a global variable inside a function, refer to the variable by using the global keyword:

```py
x = "awesome"
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```


[back to top](#python-syntax)
Or
[back to main](../README.md)