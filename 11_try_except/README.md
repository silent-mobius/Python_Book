# Try and Except

In exception handling in Python, we use the try and except statements to catch and handle exceptions. The code within the try clause is executed statement by statement.

If an exception occurs, the rest of the try block is skipped and the except clause is executed.

```py
try:
'apple' + 6
except Exception:
print "Cannot concatenate 'str' and 'int' objects"
```
OUTPUT
```txt
Cannot concatenate 'str' and 'int' objects
```
We avoid the traceback error message elegantly with a simple message like above by using try except statements for exception handling.

In addition to using an except block after the try block, we can also use the finally block. The finally clause is optional. It is intended to define clean-up actions that must be executed under all circumstances

A finally clause is always executed before leaving the try statement, whether an exception has occurred or not.

Actions, like closing a file, GUI or disconnecting from the network, are performed in the finally clause to guarantee execution.

Here is an example of file operations to illustrate finally statement.

```py
try:
f = open("foo.txt",encoding = 'utf-8')
# perform file operations
finally:
f.close()
```
This type of statement makes sure that the file is closed whether an exception occurs or not.