# Python Command Line Input

## Input() Function

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
```sh
python3 demo_input.py
```
Our program will prompt the user for a string:
Enter your name:

```txt
The user now enters a name:
Alex
```
Then, the program prints it to screen with a little message:
> Hello Alex


## Standard File Objects

Like many other languages, there are built-in file objects representing standard input, output, and error. These are in the sys module and are called stdin, stdout, and stderr. There are also immutable copies of these in __stdin__, __stdout__, and __stderr__.

You must import the sys module to use the special stdin, stdout, stderr I/O handles.

```py
import sys
```
For finer control over input, use sys.stdin.read(). In order to implement the UNIX 'cat' program in Python, you could do something like this:

```py
import sys
for line in sys.stdin:
    print line,
```

Note that sys.stdin.read() will read from standard input till EOF. (which is usually Ctrl+D.)

## Parsing command line

Command-line arguments passed to a Python program are stored in `sys.argv` list. The first item in the list is name of the Python program, which may or may not contain the full path depending on the manner of invocation. sys.argv list is modifiable.

Printing all passed arguments except for the program name itself:
```py
import sys
for arg in sys.argv[1:]:
  print arg
```
Parsing passed arguments for passed minus options:
```py
import sys
option_f = False
option_p = False
option_p_argument = ""
i = 1
while i < len(sys.argv):
  if sys.argv[i] == "-f":
    option_f = True
    sys.argv.pop(i)
  elif sys.argv[i] == "-p":
    option_p = True
    sys.argv.pop(i)
    option_p_argument = sys.argv.pop(i)
  else:
    i += 1
```
Above, the arguments at which options are found are removed so that `sys.argv` can be looped for all remaining arguments.

Parsing of command-line arguments is further supported by library modules optparse (deprecated), argparse (since Python 2.7) and getopt (to make life easy for C programmers).


[back to top](#python-command-line-input)
Or
[back to main](../README.md)