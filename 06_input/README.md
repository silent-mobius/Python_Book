# Python Command Line Input

Python allows for command line input.
That means we are able to ask the user for input.
The method is a bit different in Python 3.6 than Python 2.7.

* Python 3.6 uses the input() method.
* Python 2.7 uses the raw_input() method.

The following example asks for the user's name, and when you entered the name, the name gets printed to the screen:

> Python 3.6
```python
print("Enter your name:")
x = input()
print("Hello ", x)
```

```python
Python 2.7
print("Enter your name:")
x = raw_input()
print("Hello ", x)
```

> Save this file as demo_input.py, and load it through the command line/poweshell:
C:\Users\Your Name>python demo_input.py

Our program will prompt the user for a string:
Enter your name:

The user now enters a name:
Alex

Then, the program prints it to screen with a little message:
> Hello Alex


[back to top](#python-command-line-input)
Or
[back to main](../README.md)